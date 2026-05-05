
import uuid
from datetime import datetime
from typing import Dict, List, Any

class InMemoryDB:
    def __init__(self):
        self.documents: Dict[str, dict] = {}
        self.qa_history: List[dict] = []
        self.vectors: List[dict] = [] 

    def add_document(self, doc: dict) -> str:
        doc_id = str(uuid.uuid4())
        doc["id"] = doc_id
        doc["created_at"] = datetime.now()
        doc["updated_at"] = datetime.now()
        self.documents[doc_id] = doc
        return doc_id

    def get_document(self, doc_id: str) -> dict:
        return self.documents.get(doc_id)

    def get_all_documents(self) -> List[dict]:
        return list(self.documents.values())

    def add_qa_record(self, record: dict):
        self.qa_history.append(record)

    def get_qa_history(self) -> List[dict]:
        return self.qa_history

    def add_vector(self, vector_data: dict):
        self.vectors.append(vector_data)

    def search_vectors(self, query_vector: List[float], top_k: int = 5) -> List[dict]:
        return self.vectors[:top_k]

db = InMemoryDB()
