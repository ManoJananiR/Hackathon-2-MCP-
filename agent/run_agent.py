from agent import agent_router

print("🎓 Adaptive MCP Learning Agent (Archestra Style)")
print("Type 'exit' to stop\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = agent_router(user)
    print("Agent:", response)
