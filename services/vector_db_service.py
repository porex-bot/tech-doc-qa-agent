
from db.database import db
from services.embedding_service import embedding_service

class VectorDBService:
    def add(self, content: str, metadata: dict):
        vector = embedding_service.embed(content)
        db.add_vector({
            "content": content,
            "embedding": vector,
            "metadata": metadata
        })

    def search(self, query: str, top_k: int = 5):
        query_vector = embedding_service.embed(query)
        return db.search_vectors(query_vector, top_k)

vector_db_service = VectorDBService()
