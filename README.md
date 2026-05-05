
# Tech-Doc-QA-Agent

智能技术文档问答 Agent (最小可行产品)。基于 FastAPI, LangChain, 向量数据库模拟构建。

## 功能特性
- 文档上传与解析 (PDF, MD, HTML)
- 向量化存储 (模拟)
- 自然语言问答 (含模拟长链推理)
- 多 Agent 协作 (模拟)

## 快速开始

1. 安装依赖:
   ```
   pip install -r requirements.txt
   ```
2. 运行项目:
   ```
   uvicorn main:app --reload
   ```
3. 访问 API 文档:
   http://localhost:8000/docs

## 项目结构
- `api/`: 路由接口定义
- `agents/`: 核心 Agent 逻辑
- `services/`: 外部服务封装 (LLM, DB, Embedding)
- `schemas/`: Pydantic 数据模型
- `db/`: 数据库模拟与操作
- `utils/`: 工具函数
