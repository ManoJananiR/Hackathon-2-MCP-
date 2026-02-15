from archestra import Tool

def generate_roadmap(topic: str, llm=None):
    prompt = f"Create a beginner to advanced learning roadmap for {topic}"
    return llm(prompt)

roadmap_tool = Tool(
    name="generate_roadmap",
    description="Generate learning roadmap using LLM",
    func=generate_roadmap
)
