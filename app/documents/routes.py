from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.documents.models import DocumentCreate, DocumentResponse
from app.documents.services import DocumentService
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=DocumentResponse)
def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    service = DocumentService(db)
    return service.create_document(document)


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, db: Session = Depends(get_db)):
    service = DocumentService(db)
    document = service.get_document(document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
