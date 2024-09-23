from sqlmodel import Session
from app.documents.models import Document, DocumentCreate

class DocumentService:
    def __init__(self, db: Session):
        self.db = db

    def create_document(self, document_data: DocumentCreate) -> Document:
        new_document = Document(title=document_data.title, content=document_data.content)
        self.db.add(new_document)
        self.db.commit()
        self.db.refresh(new_document)
        return new_document

    def get_document(self, document_id: int) -> Document:
        return self.db.get(Document, document_id)
