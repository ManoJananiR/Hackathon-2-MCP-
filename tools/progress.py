user_state = {}

def save_progress(user_id: str, topic: str, score: int):
    if user_id not in user_state:
        user_state[user_id] = []

    user_state[user_id].append({
        "topic": topic,
        "score": score
    })

    return {"status": "saved", "data": user_state[user_id]}

def get_user_progress(user_id: str):
    return user_state.get(user_id, [])
