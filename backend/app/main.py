from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends, Path, Body, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import logging

# Initialize logger
logger = logging.getLogger("uvicorn.error")

app = FastAPI(title="Minimal Multi-Tenant Inventory API")

# CORS permissive for localhost only
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#### SCHEMAS

class HealthResponse(BaseModel):
    status: str = Field("ok", description="Health check status")


class LoginRequest(BaseModel):
    username: str = Field(..., description="Username for login")
    password: str = Field(..., description="Password for login")


class TokenResponse(BaseModel):
    access_token: str = Field(..., description="Mock access token")
    token_type: str = Field("bearer", description="Token type")


class InventoryItem(BaseModel):
    id: int = Field(..., description="Unique ID for the inventory item")
    tenant_id: int = Field(..., description="Tenant identifier")
    name: str = Field(..., description="Name of the inventory item")
    description: Optional[str] = Field(None, description="Description of the item")
    quantity: int = Field(..., ge=0, description="Available quantity")


#### MOCK DATA

MOCK_USERNAME = "testuser"
MOCK_PASSWORD = "testpass"
MOCK_TOKEN = "mocked-jwt-token-123"

# Sample inventory items keyed by tenant_id
MOCK_INVENTORY = {
    1: [
        InventoryItem(id=1, tenant_id=1, name="Red Widget", description="A red widget", quantity=10),
        InventoryItem(id=2, tenant_id=1, name="Blue Widget", description="A blue widget", quantity=5),
    ],
    2: [
        InventoryItem(id=1, tenant_id=2, name="Green Widget", description="A green widget", quantity=7),
    ],
}


#### DEPENDENCIES

def verify_tenant_id(tenant_id: int = Path(..., description="Tenant identifier")) -> int:
    """
    Verify tenant_id is valid (for example check if integer positive).
    In a real app, you would verify tenant existence and authorization.
    """
    if tenant_id <= 0:
        logger.warning(f"Invalid tenant_id received: {tenant_id}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid tenant ID")
    return tenant_id


#### ENDPOINTS

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health() -> HealthResponse:
    """
    Health check endpoint.

    Returns:
        HealthResponse: status ok if service is running.
    """
    logger.debug("Health check requested")
    return HealthResponse(status="ok")


@app.post("/login", response_model=TokenResponse, tags=["Auth"])
async def login(login_req: LoginRequest = Body(...)) -> TokenResponse:
    """
    Login endpoint accepting mock credentials.

    Args:
        login_req (LoginRequest): username and password.

    Returns:
        TokenResponse: mock access token on successful login.
    """
    logger.debug(f"Login attempt for user {login_req.username}")
    if login_req.username == MOCK_USERNAME and login_req.password == MOCK_PASSWORD:
        logger.info(f"User {login_req.username} logged in successfully.")
        return TokenResponse(access_token=MOCK_TOKEN, token_type="bearer")

    logger.warning(f"Failed login attempt for user {login_req.username}")
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")


@app.get(
    "/tenants/{tenant_id}/inventory",
    response_model=List[InventoryItem],
    tags=["Inventory"],
)
async def list_inventory(tenant_id: int = Depends(verify_tenant_id)) -> List[InventoryItem]:
    """
    List all inventory items for a given tenant.

    Args:
        tenant_id (int): tenant id path parameter.

    Returns:
        List[InventoryItem]: list of inventory items belonging to the tenant.
    """
    logger.debug(f"Inventory list requested for tenant_id={tenant_id}")
    items = MOCK_INVENTORY.get(tenant_id)
    if items is None:
        logger.info(f"No inventory found for tenant_id={tenant_id}, returning empty list")
        return []
    return items


@app.get(
    "/tenants/{tenant_id}/inventory/{item_id}",
    response_model=InventoryItem,
    tags=["Inventory"],
)
async def get_inventory_item(
    tenant_id: int = Depends(verify_tenant_id),
    item_id: int = Path(..., ge=1, description="Inventory item identifier"),
) -> InventoryItem:
    """
    Get a specific inventory item by tenant and item ID.

    Args:
        tenant_id (int): tenant id path parameter.
        item_id (int): inventory item id path parameter.

    Returns:
        InventoryItem: requested inventory item.
    """
    logger.debug(f"Inventory item requested for tenant_id={tenant_id}, item_id={item_id}")
    items = MOCK_INVENTORY.get(tenant_id)
    if not items:
        logger.warning(f"Tenant {tenant_id} not found or has no inventory")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant inventory not found")

    for item in items:
        if item.id == item_id:
            return item

    logger.warning(f"Inventory item {item_id} not found for tenant {tenant_id}")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found")

#### DOCUMENTATION

@app.get("/", include_in_schema=False)
async def root_redirect():
    """
    Default root - redirect to docs.
    """
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/docs")

# Notes for future upgrade (to replace mock):
"""
To replace the mock data:

- Implement authentication and token generation with proper security.
- Replace MOCK_INVENTORY with calls to a database repository supporting multi-tenant isolation.
- Ensure tenant authorization is performed based on the token.
- Use async database calls with SQLAlchemy async or your choice of ORM.
- Replace the verify_tenant_id check with authorization middleware or dependency extraction from the token.

"""