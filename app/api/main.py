from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Enterprise AI Agent Platform")


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "Enterprise AI Agent Platform is running."}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    return {
        "question": request.question,
        "answer": f"Mock AI response for: {request.question}"
    }
