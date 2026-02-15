from ollama_llm import ask_llama
from tools.gfg_tool import tutorial_link, roadmap_link, quiz_link

def agent_router(user_input: str):
    user_input_lower = user_input.lower()

    if "tutorial" in user_input_lower:
        topic = user_input_lower.replace("tutorial", "").strip()
        return tutorial_link(topic)

    if "roadmap" in user_input_lower:
        topic = user_input_lower.replace("roadmap", "").strip()
        return roadmap_link(topic)

    if "quiz" in user_input_lower or "interview questions" in user_input_lower:
        topic = user_input_lower.replace("quiz", "").strip()
        return quiz_link(topic)

    # If no tool matched → ask LLM (Ollama)
    return ask_llama(user_input)
