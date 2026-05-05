
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DocumentBase(BaseModel):
    title: str
    category: Optional[str] = None
    tags: List[str] = []

class DocumentCreate(DocumentBase):
    pass

class DocumentResponse(DocumentBase):
    id: str
    file_type: str
    status: str
    progress: int
    created_at: datetime

    class Config:
        from_attributes = True

class QAOptions(BaseModel):
    top_k: int = 5
    enable_reasoning: bool = True
    include_sources: bool = True

class QARequest(BaseModel):
    question: str
    options: QAOptions = QAOptions()

class SourceInfo(BaseModel):
    document_id: str
    title: str
    chunk_content: str
    score: float

class QAResponse(BaseModel):
    id: str
    question: str
    answer: str
    confidence: float
    sources: List[SourceInfo] = []
    reasoning_steps: List[str] = []
    created_at: datetime
