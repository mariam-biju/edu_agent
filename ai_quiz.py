from ai_quiz import generate_ai_quiz

def generate_quiz(topic, difficulty="easy"):
    # Difficulty is unused for static quizzes but preserved for compatibility
    return generate_ai_quiz(topic)

def check_answers(questions):
    score = 0
    for q in questions:
        if q["answer"] == q["options"][q["options"].index(q["answer"])]:
            if q["question"] in q and q["answer"] == q["options"][q["options"].index(q["answer"])]:
                score += 1 if q["answer"] == q["options"][q["options"].index(q["answer"])] else 0
            elif q["question"] in q:
                selected = q["options"].index(q["answer"])
                if selected == q["options"].index(q["answer"]):
                    score += 1
        elif q["question"] in q:
            selected = q["options"].index(q["answer"])
            if selected == q["options"].index(q["answer"]):
                score += 1
    return score

def get_user_difficulty(avg_score):
    # You can customize this logic if needed later
    if avg_score < 2:
        return "easy"
    elif avg_score < 4:
        return "medium"
    return "hard"
