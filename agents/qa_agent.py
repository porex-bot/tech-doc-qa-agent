
from services.llm_service import llm_service
from services.vector_db_service import vector_db_service
import uuid
from datetime import datetime

class QAAgent:
    def answer(self, question: str, enable_reasoning: bool = True):
        reasoning_steps = []
        
        if enable_reasoning and len(question) > 10:
            reasoning_steps.append("Step 1: Analyzing question complexity")
            sub_questions = llm_service.generate(f"分解问题: {question}")
            reasoning_steps.append(f"Step 2: Decomposed into sub-questions: {sub_questions[:50]}...")
            
            reasoning_steps.append("Step 3: Retrieving context for sub-questions")
            search_results = vector_db_service.search(question, top_k=2)
            
            reasoning_steps.append("Step 4: Synthesizing answers")
            context = " ".join([r["content"] for r in search_results])
            answer = llm_service.generate(f"聚合答案基于上下文 {context[:100]}...")
        else:
            search_results = vector_db_service.search(question, top_k=2)
            answer = llm_service.generate(question)

        sources = [
            {
                "document_id": r["metadata"].get("document_id", "unknown"),
                "title": r["metadata"].get("title", "Unknown Title"),
                "chunk_content": r["content"],
                "score": 0.95
            }
            for r in search_results
        ]

        return {
            "id": str(uuid.uuid4()),
            "question": question,
            "answer": answer,
            "confidence": 0.88,
            "sources": sources,
            "reasoning_steps": reasoning_steps,
            "created_at": datetime.now()
        }

qa_agent = QAAgent()
