# main.py

import requests

# Ensure this matches the port your MCP server is running on
BASE_URL = "http://127.0.0.1:8080"

print("MCP Agent (For retrieving tutorial link) — type 'exit' to quit")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        break
    if not user_input:
        continue

    try:
        # Send the user input to the MCP server
        response = requests.post(f"{BASE_URL}/mcp_query", json={"topic": user_input}, timeout=15)
        response.raise_for_status()  # Raise exception for HTTP errors
        try:
            data = response.json()
            print("Agent:", data)
        except requests.exceptions.JSONDecodeError:
            print("Agent: Received invalid JSON from MCP server.")
    except requests.exceptions.ConnectionError:
        print(f"Agent: Cannot connect to MCP server at {BASE_URL}. Make sure it is running.")
    except requests.exceptions.Timeout:
        print("Agent: Request timed out. The MCP server might be busy or slow.")
    except requests.exceptions.HTTPError as e:
        print(f"Agent: MCP server returned HTTP error: {e}")
    except Exception as e:
        print(f"Agent: Unexpected error: {e}")