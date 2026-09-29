import pytest
from fastapi.testclient import TestClient
from app.main import app, MOCK_INVENTORY, MOCK_USERNAME, MOCK_PASSWORD, MOCK_TOKEN


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


@pytest.mark.parametrize(
    "username,password,expected_status,expected_token",
    [
        (MOCK_USERNAME, MOCK_PASSWORD, 200, MOCK_TOKEN),
        ("wronguser", MOCK_PASSWORD, 401, None),
        (MOCK_USERNAME, "wrongpass", 401, None),
        ("", "", 422, None),  # Validation error from FastAPI/Pydantic for missing fields
    ],
)
def test_login(username, password, expected_status, expected_token):
    response = client.post("/login", json={"username": username, "password": password})
    assert response.status_code == expected_status
    if expected_status == 200:
        data = response.json()
        assert data["access_token"] == expected_token
        assert data["token_type"] == "bearer"
    else:
        # On error response check detail message exists
        data = response.json()
        assert "detail" in data


@pytest.mark.parametrize(
    "tenant_id,expected_status,expected_len",
    [
        (1, 200, 2),
        (2, 200, 1),
        (3, 200, 0),  # Tenant with no items returns empty list
        (0, 400, None),  # Invalid tenant_id: less than or equal 0
        (-1, 400, None),
    ],
)
def test_list_inventory(tenant_id, expected_status, expected_len):
    response = client.get(f"/tenants/{tenant_id}/inventory")
    assert response.status_code == expected_status
    if expected_status == 200:
        data = response.json()
        assert isinstance(data, list)
        if expected_len is not None:
            assert len(data) == expected_len


@pytest.mark.parametrize(
    "tenant_id,item_id,expected_status,expected_name",
    [
        (1, 1, 200, "Red Widget"),
        (1, 2, 200, "Blue Widget"),
        (2, 1, 200, "Green Widget"),
        (1, 999, 404, None),  # Non-existing item_id
        (3, 1, 404, None),  # Tenant with no inventory returns 404
        (0, 1, 400, None),  # Invalid tenant_id
        (1, 0, 422, None),  # Invalid item_id min=1 validation
        (1, -1, 422, None),
    ],
)
def test_get_inventory_item(tenant_id, item_id, expected_status, expected_name):
    response = client.get(f"/tenants/{tenant_id}/inventory/{item_id}")
    assert response.status_code == expected_status
    if expected_status == 200:
        data = response.json()
        assert data["name"] == expected_name


def test_verify_tenant_id_path_param_invalid():
    # Directly test the dependency function for invalid tenant ID
    from app.main import verify_tenant_id
    import pytest
    from fastapi import HTTPException

    with pytest.raises(HTTPException) as excinfo:
        verify_tenant_id(0)
    assert excinfo.value.status_code == 400

    with pytest.raises(HTTPException) as excinfo:
        verify_tenant_id(-5)
    assert excinfo.value.status_code == 400


def test_root_redirect():
    response = client.get("/")
    # The endpoint performs a redirect to /docs
    assert response.status_code in (307, 308)
    assert response.headers["location"] == "/docs"