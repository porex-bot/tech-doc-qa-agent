
from fastapi import APIRouter, UploadFile, File, Form
from typing import List, Optional
from schemas.models import DocumentCreate, DocumentResponse
from db.database import db
from agents.document_parser_agent import document_parser_agent
from datetime import datetime

router = APIRouter()

@router.post("/documents", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    title: Optional[str] = Form(None),
    category: Optional[str] = Form(None),
    tags: Optional[str] = Form(None)
):
    content = await file.read()
    content_str = content.decode("utf-8", errors="ignore")
    
    doc_data = {
        "title": title or file.filename,
        "file_type": file.filename.split(".")[-1],
        "status": "completed",
        "progress": 100,
        "category": category,
        "tags": tags.split(",") if tags else []
    }
    
    doc_id = db.add_document(doc_data)
    doc_data["id"] = doc_id
    doc_data["created_at"] = datetime.now()
    
    import threading
    threading.Thread(
        target=document_parser_agent.process,
        args=(file.filename, content_str, {**doc_data, "document_id": doc_id})
    ).start()
    
    return doc_data

@router.get("/documents", response_model=List[DocumentResponse])
async def list_documents():
    return db.get_all_documents()

@router.get("/documents/{doc_id}", response_model=DocumentResponse)
async def get_document(doc_id: str):
    return db.get_document(doc_id)
