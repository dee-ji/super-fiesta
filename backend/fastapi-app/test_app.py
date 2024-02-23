import pytest
from httpx import AsyncClient
from main import app
from databases import Database


# Use pytest-asyncio for async test functions
@pytest.mark.asyncio
async def test_create_contact():
    async with AsyncClient(app=app, base_url="http://localhost") as ac:
        response = await ac.post("/contact/", json={"name": "John Doe", "email": "john@example.com", "message": "Hello, World!"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

@pytest.mark.asyncio
async def test_read_contacts():
    async with AsyncClient(app=app, base_url="http://localhost") as ac:
        response = await ac.get("/contacts/")
    assert response.status_code == 200
    contacts = response.json()
    assert len(contacts) > 0

@pytest.mark.asyncio
async def test_update_contact():
    contact_id = 1  # Assuming there's at least one contact; you might need to adjust this based on your test DB setup
    async with AsyncClient(app=app, base_url="http://localhostt") as ac:
        response = await ac.put(f"/contacts/{contact_id}", json={"name": "Jane Doe", "email": "jane@example.com", "message": "Hi there!"})
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

@pytest.mark.asyncio
async def test_delete_contact():
    contact_id = 1  # Assuming this contact exists; adjust as necessary
    async with AsyncClient(app=app, base_url="http://localhost") as ac:
        response = await ac.delete(f"/contacts/{contact_id}")
    assert response.status_code == 204
