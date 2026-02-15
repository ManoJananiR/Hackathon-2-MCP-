import requests

BASE_URL = "http://127.0.0.1:8080"

print("🎓 Dynamic MCP Agent (GFG + Ollama) — type 'exit' to quit")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break
    response = requests.post(f"{BASE_URL}/mcp_query", json={"topic": user_input}).json()
    print("Agent:", response)
