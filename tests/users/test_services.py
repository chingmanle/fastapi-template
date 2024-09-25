# tests/test_user.py
import pytest
from app.users.models import User, UserCreate
from app.users.services import UserService  # Example service function
from unittest.mock import Mock



def test_create_user(mock_db):
    # Arrange
    mock_user = User(id=1, name="John Doe", email="john@example.com")
    mock_db.add = Mock()  
    mock_db.commit = Mock()
    mock_db.refresh = Mock(side_effect=lambda user: setattr(user, 'id', 1))  # Simulate the DB setting the ID after refresh
    
    # Act
    user_service = UserService(db=mock_db)
    result = user_service.create_user(mock_user)
    
    # Assertions
    mock_db.add.assert_called_once_with(mock_user)  # Ensure add was called with the correct object
    mock_db.commit.assert_called_once()  # Ensure commit was called once
    mock_db.refresh.assert_called_once_with(mock_user)  # Ensure refresh was called with the correct object
    
    # Assert
    assert result.name == mock_user.name  # Compare with mock_user
    assert result.email == mock_user.email  # Compare with mock_user
    assert result.id == mock_user.id  # Ensure the ID was set correctly



def test_get_user(client, mock_db):
    # Arrange
    mock_user = User(id=1, name="Jane Doe", email="john@example.com")
    mock_db.get.return_value = mock_user

    # Act
    user_service = UserService(db=mock_db)
    result = user_service.get_user(user_id=1)

    # Assert
    assert result.name == mock_user.name  # Compare with mock_user
    assert result.email == mock_user.email  # Compare with mock_user
    assert result.id == mock_user.id  # Compare with mock_user
