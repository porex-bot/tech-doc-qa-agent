
import time
from services.vector_db_service import vector_db_service

class DocumentParserAgent:
    def process(self, file_path: str, file_content: str, metadata: dict):
        print(f"[DocumentParserAgent] Processing file: {file_path}")
        
        time.sleep(1)
        
        chunks = self._split_content(file_content)
        
        for i, chunk in enumerate(chunks):
            chunk_metadata = {
                **metadata,
                "source": file_path,
                "chunk_index": i
            }
            vector_db_service.add(chunk, chunk_metadata)
            
        print(f"[DocumentParserAgent] Indexed {len(chunks)} chunks.")
        return len(chunks)

    def _split_content(self, content: str) -> list:
        return [content[i:i+500] for i in range(0, len(content), 500)]

document_parser_agent = DocumentParserAgent()
