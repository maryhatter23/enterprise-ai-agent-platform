from fastapi import FastAPI

app = FastAPI(title="Enterprise AI Agent Platform")

@app.get("/")
def root():
    return {"message": "Enterprise AI Agent Platform is running."}
