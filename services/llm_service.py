
import random
import time

class LLMService:
    def generate(self, prompt: str) -> str:
        time.sleep(0.5)
        if "分解" in prompt or "子问题" in prompt:
            return """
            1. 这是一个模拟的子问题1。
            2. 这是一个模拟的子问题2。
            3. 这是一个模拟的子问题3。
            """
        elif "聚合" in prompt:
            return "这是基于子问题聚合后的模拟答案。整体来看，该项目旨在构建一个智能问答系统。"
        else:
            return f"这是对问题 '{prompt[:20]}...' 的模拟回答。由于我是Mock服务，只能提供通用回复。"

class EmbeddingService:
    def embed(self, text: str) -> list:
        return [random.random() for _ in range(1536)]

llm_service = LLMService()
embedding_service = EmbeddingService()
