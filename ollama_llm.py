import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("ARCHESTRA_OLLAMA_BASE_URL", "http://localhost:1143/v1")
API_KEY = os.getenv("ARCHESTRA_CHAT_OLLAMA_API_KEY")

def ask_llama(prompt: str):
    payload = {
        "model": "llama3",
        "messages": [{"role": "user", "content": prompt}]
    }
    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"

    response = requests.post(
    f"{BASE_URL}/completions",
    json=payload,
    headers=headers,
    timeout=60  # increase from 10 -> 60
)
    r = requests.post(f"{BASE_URL}/chat/completions", json=payload, headers=headers)
    if r.status_code == 200:
        return r.json()
    return {"error": r.text}
