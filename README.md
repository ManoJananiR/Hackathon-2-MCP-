Ther is a error in my demo video , while screen recording the terminal window , the chrome interface is not visible but its open when I click the link ,let me provide another video there the chrome will be visible but not the terminal.


MCP Agent for learning from edtech platform
1. Project Overview

An interactive learning assistant for developers and students.

Fetches tutorials, roadmaps, and interview quizzes dynamically from GeeksforGeeks.

Uses Ollama LLM for natural language queries and explanations.

Simple CLI interface, optional Docker deployment.

2. Key Features

Dynamic Retrieval: Fetches content directly from GFG (tutorials, roadmap, interview questions).

LLM Integration: Handles queries not directly linked to GFG using Ollama.

Portable: Runs locally or in Docker.

Lightweight & Extensible: Easily add new topics/tools.

3. Architecture
[User CLI]  <----->  [MCP Server: FastAPI]  <----->  [GFG Tools / Ollama LLM]
       |                     |                       |
       |                     |----> Fetch GFG links  |
       |                     |----> Call Ollama LLM  |
       |                     |                       |
       v                     v                       v
    User Input           JSON Response           LLM-generated answer


Flow:

User types a query (e.g., "Javascript tutorial") in CLI.

MCP Server checks GFG tools → returns link if found.

If topic is not found → sends query to Ollama LLM for explanation.

CLI displays results:

{
  "topic": "java",
  "links": {"tutorial": "<link>", "interview": "<link>", "roadmap": "<link>"},
  "summary": "LLM-generated answer"
}

4. How Archestra + Ollama Are Used

Inspired by Archestra.ai architecture:

Separation of tool retrieval and LLM reasoning.

Modular design: easy to extend and maintain.

Ollama: Local LLM for privacy, fast responses, natural language handling.

5. Technologies

Python 3.14 – Core logic.

FastAPI – MCP server for queries.

Requests + BeautifulSoup – Dynamic GFG scraping.

Ollama LLM – Advanced query handling.

Docker – Optional containerized deployment.

6. How to Run

Start Ollama:

ollama serve


Run MCP server:

python mcp_server.py


Run CLI agent:

python main.py

Ask queries:

You: javascript tutorial
You: python roadmap
You: dsa interview
You: exit

7. Benefits

Instant access to real GFG content dynamically.

Can answer custom queries using Ollama LLM.

Lightweight and extendable → add new topics/tools anytime.

Professional-grade setup: modular, CLI + server + optional Docker.
