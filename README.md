# Adaptive Learning MCP Server

Adaptive learning MCP-style server for EdTech/corporate learning use cases (GeeksforGeeks-style platforms, LMS, internal training).

## Features
- Track learner progress across multiple systems.
- Integrate content from CMS/LMS systems.
- Personalize recommendations with ML ranking + Groq LLM plan generation.
- Coordinate quiz/assessment submissions and auto-generate feedback.
- Orchestration layer using `Archestra` in Python.

## Stack
- Python + FastAPI
- Archestra orchestration (`archestra/`)
- Groq LLM API
- SQLite persistence (for MVP)
- Docker + Docker Compose

## API Endpoints
- `GET /health`
- `POST /progress/upsert`
- `POST /content/upsert`
- `POST /recommendations/generate`
- `POST /assessments/submit`
- `POST /feedback/generate`

## Local Run
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn mcp.server:app --reload --host 0.0.0.0 --port 8000
```

## Docker Run
```bash
docker compose up --build
```

## Environment
Add in `.env`:
```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant
```

## Example Request
```bash
curl -X POST http://localhost:8000/progress/upsert \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "u-101",
    "system": "geeksforgeeks",
    "course_id": "dsa",
    "module_id": "graphs",
    "progress_percent": 70,
    "score": 66,
    "time_spent_minutes": 40
  }'
```
