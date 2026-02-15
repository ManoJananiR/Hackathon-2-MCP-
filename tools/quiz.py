def generate_quiz(topic: str):
    return {
        "topic": topic,
        "questions": [
            {
                "question": f"What is {topic}?",
                "options": ["Concept", "Language", "OS", "Compiler"],
                "answer": "Concept"
            },
            {
                "question": f"Why is {topic} important?",
                "options": ["Optimization", "Decoration", "UI", "Color"],
                "answer": "Optimization"
            }
        ]
    }
