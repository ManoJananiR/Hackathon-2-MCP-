import sqlite3

conn = sqlite3.connect("progress.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS progress (
    user_id TEXT,
    topic TEXT,
    score INTEGER
)
""")
conn.commit()

def save_progress(user_id, topic, score):
    cursor.execute(
        "INSERT INTO progress VALUES (?, ?, ?)",
        (user_id, topic, score)
    )
    conn.commit()
    return {"status": "saved"}

def get_progress(user_id):
    cursor.execute(
        "SELECT topic, score FROM progress WHERE user_id=?",
        (user_id,)
    )
    rows = cursor.fetchall()
    return [{"topic": r[0], "score": r[1]} for r in rows]
