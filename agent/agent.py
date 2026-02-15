from llm import ask_llm
from mcp_client import get_roadmap, generate_quiz, track_progress, get_progress

USER_ID = "jan"

def agent_router(user_input: str):
    user_input = user_input.lower()

    if "roadmap" in user_input or "learn" in user_input:
        topic = user_input.replace("roadmap", "").replace("learn", "").strip()
        data = get_roadmap(topic)
        return f"📚 Roadmap for {topic}:\n{data}"

    elif "quiz" in user_input:
        topic = user_input.replace("quiz", "").strip()
        quiz = generate_quiz(topic)
        return quiz

    elif "progress" in user_input:
        return get_progress(USER_ID)

    else:
        return ask_llm(user_input)
