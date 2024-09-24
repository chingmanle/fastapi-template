from sqlmodel import Session
from typing import Optional
from app.users.models import User, UserCreate


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserCreate) -> User:
        new_user = User(name=user_data.name, email=user_data.email)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user(self, user_id: int) -> Optional[User]:
        return self.db.get(User, user_id)
