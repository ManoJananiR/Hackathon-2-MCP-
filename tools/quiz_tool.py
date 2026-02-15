from archestra import Tool

def generate_quiz(topic: str, llm=None):
    prompt = f"Create 5 multiple choice questions for {topic}"
    return llm(prompt)

quiz_tool = Tool(
    name="generate_quiz",
    description="Generate quiz questions for a topic",
    func=generate_quiz
)
