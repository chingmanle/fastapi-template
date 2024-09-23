from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class DocumentBase(SQLModel):
    title: str
    content: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class DocumentCreate(DocumentBase):
    pass

class DocumentResponse(DocumentBase):
    id: Optional[int]

class Document(DocumentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
