import sqlite3

def init_db():
    with sqlite3.connect("learnova.db") as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                topic TEXT,
                score INTEGER,
                total INTEGER
            )
        ''')
        conn.commit()

def store_score(topic, score, total):
    with sqlite3.connect("learnova.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO scores (topic, score, total) VALUES (?, ?, ?)", (topic, score, total))
        conn.commit()

def get_progress_data():
    with sqlite3.connect("learnova.db") as conn:
        c = conn.cursor()
        c.execute("SELECT topic, score, total FROM scores")
        data = c.fetchall()
        return [(topic, f"{score}/{total}") for topic, score, total in data]

def get_average_score(topic):
    with sqlite3.connect("learnova.db") as conn:
        c = conn.cursor()
        c.execute("SELECT AVG(score * 1.0 / total) FROM scores WHERE topic = ?", (topic,))
        result = c.fetchone()[0]
        return round(result * 5, 2) if result else 0  # Scale to 5 for consistency
