from agent.agent import agent

print("🎓 Adaptive MCP Learning Agent (Archestra + Ollama)")
print("Type 'exit' to stop\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break

    response = agent.run(user)
    print("Agent:", response)

