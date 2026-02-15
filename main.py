from fastapi import FastAPI
from pydantic import BaseModel
from tools.roadmap import generate_roadmap
from tools.quiz import generate_quiz
from tools.progress import save_progress, get_user_progress

app = FastAPI(title="Adaptive MCP Server")

# -----------------------------
# Models
# -----------------------------
class ProgressRequest(BaseModel):
    user_id: str
    topic: str
    score: int

# -----------------------------
# Routes
# -----------------------------
@app.get("/")
def root():
    return {"message": "MCP Server Running"}

@app.get("/roadmap")
def roadmap(topic: str):
    return generate_roadmap(topic)

@app.get("/quiz")
def quiz(topic: str):
    return generate_quiz(topic)

@app.post("/progress")
def progress(data: ProgressRequest):
    return save_progress(data.user_id, data.topic, data.score)

@app.get("/progress/{user_id}")
def progress_get(user_id: str):
    return get_user_progress(user_id)
