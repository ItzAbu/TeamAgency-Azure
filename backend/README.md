# Minimal Multi-Tenant Inventory API

## Description
A minimal FastAPI backend exposing a simple multi-tenant API with:
- /health endpoint (GET): returns service health status
- /login endpoint (POST): accepts mock credentials and returns a mock token
- /tenants/{tenant_id}/inventory (GET): lists sample inventory items per tenant
- /tenants/{tenant_id}/inventory/{id} (GET): returns single inventory item by id

Supports tenant isolation via path parameter and data scoped by `tenant_id`. The data is mocked/static for UI/frontend testing.

CORS is permissive for localhost origins.

## How to Run

### Prerequisites
- Docker installed _or_
- Python >= 3.11 environment with `pip` installed

### Using Docker (Recommended)