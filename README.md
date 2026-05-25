# enterprise-ai-agent-platform
ai-workflow-document-intelligence
# Enterprise AI Agent Platform

Production-style multi-agent AI workflow platform for enterprise document intelligence, validation, and retrieval-augmented reasoning.

---

## Features

- Multi-agent workflow orchestration
- Retrieval-Augmented Generation (RAG)
- Document ingestion pipeline
- Validation and groundedness checking
- Evaluation system for AI responses
- FastAPI backend
- Streamlit frontend
- Modular enterprise-style architecture

---
## UI Preview

### Initial UI

![Initial UI](docs/screenshots/app_ui.png)

---

### Real OpenAI Response

![Real OpenAI Response](docs/screenshots/real-gpt-response.png)

---

### Document Upload and Q&A Workflow

![Document Q&A Workflow](docs/screenshots/document-qa-workflow.png)

---
## Live Demo

Frontend (Streamlit):
https://enterprise-ai-agent-platform-8hyseap2azqwdqtkqwcyt.streamlit.app

Backend API (Railway):
https://web-production-c1b1e.up.railway.app

API Docs:
https://web-production-c1b1e.up.railway.app/docs
---

## Architecture

```mermaid
flowchart TD

    A[User] --> B[Streamlit Frontend]

    B --> C[FastAPI Backend]

    C --> D[Document Upload Pipeline]

    D --> E[PDF/TXT Parsing]

    E --> F[Document Chunking]

    F --> G[Sentence Transformer Embeddings]

    G --> H[(ChromaDB Vector Store)]

    I[User Question] --> J[Semantic Retrieval]

    H --> J

    J --> K[Relevant Chunks]

    K --> L[OpenAI GPT-4o-mini]

    L --> M[Citation-aware Response]

    M --> B

    subgraph Cloud Deployment
        B
        C
        H
    end
```
---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Streamlit
- LangChain / LangGraph-style orchestration
- RAG pipelines
- Docker
- GitHub

---

## Current Capabilities

- Upload TXT/PDF documents
- Ask contextual questions
- Run AI workflow pipelines
- Validate response groundedness
- Generate evaluation metrics

---

## Features

- OpenAI-powered question answering
- PDF and TXT document upload
- Text extraction from uploaded documents
- Document chunking
- Embedding generation with Sentence Transformers
- ChromaDB vector storage
- Semantic retrieval over document chunks
- Citation-aware RAG pipeline with source metadata
- FastAPI backend
- Streamlit frontend

---

## Run Locally

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate