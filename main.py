
from fastapi import FastAPI
from api import documents, qa
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Tech-Doc-QA-Agent",
    description="智能技术文档问答 Agent MVP",
    version="1.0.0"
)

app.include_router(documents.router, prefix="/api/v1", tags=["Documents"])
app.include_router(qa.router, prefix="/api/v1", tags=["QA"])
app.include_router(stats.router, prefix="/api/v1", tags=["Stats"])

@app.get("/")
async def root():
    return {"message": "Welcome to Tech-Doc-QA-Agent MVP"}
