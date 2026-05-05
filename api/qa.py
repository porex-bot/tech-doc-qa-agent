
from fastapi import APIRouter
from schemas.models import QARequest, QAResponse
from agents.qa_agent import qa_agent
from db.database import db

router = APIRouter()

@router.post("/qa/query", response_model=QAResponse)
async def create_query(req: QARequest):
    result = qa_agent.answer(
        req.question,
        enable_reasoning=req.options.enable_reasoning
    )
    db.add_qa_record(result)
    return result

@router.get("/qa/history")
async def get_history():
    return db.get_qa_history()
