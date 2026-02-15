def track_progress(data):
    user = data.get("user_id")
    progress = data.get("progress")
    return {
        "message": f"Progress updated for {user}",
        "progress": progress
    }

def sync_content(data):
    course = data.get("course_id")
    return {
        "message": f"Content synced for course {course}"
    }

def recommend(data):
    user = data.get("user_id")
    return {
        "recommendations": [
            "AI Basics",
            "Prompt Engineering",
            "FastAPI for LLM apps"
        ],
        "user": user
    }

def submit_assessment(data):
    user = data.get("user_id")
    score = data.get("score")
    return {
        "message": f"Assessment submitted for {user}",
        "score": score
    }

def generate_feedback(data):
    score = data.get("score")
    if score > 80:
        feedback = "Excellent work!"
    elif score > 50:
        feedback = "Good job, keep improving."
    else:
        feedback = "Needs more practice."

    return {
        "feedback": feedback,
        "score": score
    }
