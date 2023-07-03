from ..main import app
from typing import AsyncIterator
import httpx
import pytest 

@pytest.fixture
async def client() -> AsyncIterator[httpx.AsyncClient]:
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        yield client

@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"

from fastapi.testclient import TestClient

@pytest.mark.anyio
async def test_read_root(client: httpx.AsyncClient):
    response = await client.get('/')
    assert response.status_code == 200
