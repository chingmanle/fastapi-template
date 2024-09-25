# tests/conftest.py
import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Fixture to set up the database, if needed."""
    pass  # You can leave this empty or implement a real database setup if necessary.

@pytest.fixture
def mock_db():
    """Fixture to mock the database session."""
    mock_db = MagicMock()
    yield mock_db

@pytest.fixture
def client(mock_db):
    """Create a test client using the FastAPI app with mocked DB."""
    app.dependency_overrides[get_db] = lambda: mock_db
    with TestClient(app) as test_client:
        yield test_client
