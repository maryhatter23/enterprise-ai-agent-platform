import os

from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Enterprise AI Agent Platform")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "Enterprise AI Agent Platform is running."}


@app.post("/ask")
def ask_question(request: QuestionRequest):

    completion = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {
                "role": "system",
                "content": "You are an enterprise AI workflow assistant."
            },
            {
                "role": "user",
                "content": request.question
            }
        ]
    )

    answer = completion.choices[0].message.content

    return {
        "question": request.question,
        "answer": answer
    }