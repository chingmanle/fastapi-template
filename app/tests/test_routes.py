from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/", json={"name": "Alice", "email": "alice@example.com"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"


def test_get_user():
    response = client.post(
        "/users/", json={"name": "Bob", "email": "bob@example.com"}
    )
    created_user = response.json()

    response = client.get(f"/users/{created_user['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Bob"
