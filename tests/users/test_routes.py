from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Alice"
    assert response.json()["email"] == "alice@example.com"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
