from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.users.models import UserCreate, UserResponse
from app.users.services import UserService
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
