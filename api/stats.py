
from fastapi import APIRouter
from db.database import db

router = APIRouter()

@router.get("/stats/overview")
async def get_overview():
    return {
        "total_documents": len(db.get_all_documents()),
        "total_queries": len(db.get_qa_history()),
        "success_rate": 0.98
    }
