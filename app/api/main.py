import os
import fitz

from app.rag.vector_store import add_document_to_vector_db, retrieve_relevant_chunks
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Enterprise AI Agent Platform")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DOCUMENT_CONTEXT = ""


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "Enterprise AI Agent Platform is running."}


@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    global DOCUMENT_CONTEXT

    content = await file.read()

    if file.filename.lower().endswith(".pdf"):
        with open("temp_uploaded.pdf", "wb") as f:
            f.write(content)

        doc = fitz.open("temp_uploaded.pdf")
        text = ""

        for page in doc:
            text += page.get_text()

        DOCUMENT_CONTEXT = text

    else:
        DOCUMENT_CONTEXT = content.decode("utf-8", errors="ignore")

    chunks_added = add_document_to_vector_db(
        DOCUMENT_CONTEXT,
        file.filename
    )

    return {
        "filename": file.filename,
        "characters_extracted": len(DOCUMENT_CONTEXT),
        "chunks_added_to_vector_db": chunks_added,
        "message": "Document uploaded and processed successfully."
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    relevant_chunks = retrieve_relevant_chunks(request.question)

    retrieved_context = "\n\n".join(
        [chunk["text"] for chunk in relevant_chunks]
    )

    prompt = f"""
You are an enterprise document intelligence assistant.

Use the retrieved document context below to answer the user's question.
If the answer is not available in the retrieved context, say that the document does not provide enough information.

Retrieved Document Context:
{retrieved_context}

User Question:
{request.question}
"""

    completion = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {
                "role": "system",
                "content": "You answer questions based on retrieved enterprise document chunks."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return {
        "question": request.question,
        "answer": completion.choices[0].message.content,
        "context_length": len(retrieved_context),
        "retrieved_chunks": relevant_chunks
    }