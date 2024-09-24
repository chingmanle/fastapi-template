from sqlmodel import SQLModel, Field
from typing import Optional


class UserBase(SQLModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: Optional[int]


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
