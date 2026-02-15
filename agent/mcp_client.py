import requests

MCP_URL = "http://localhost:8080"

def get_roadmap(topic: str):
    return requests.get(f"{MCP_URL}/roadmap", params={"topic": topic}).json()

def generate_quiz(topic: str):
    return requests.get(f"{MCP_URL}/quiz", params={"topic": topic}).json()

def track_progress(user_id: str, topic: str, score: int):
    return requests.post(
        f"{MCP_URL}/progress",
        json={"user_id": user_id, "topic": topic, "score": score},
    ).json()

def get_progress(user_id: str):
    return requests.get(f"{MCP_URL}/progress/{user_id}").json()
