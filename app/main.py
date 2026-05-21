from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Enterprise AI Agent Platform is running."}