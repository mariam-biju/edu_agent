def detect_intent(text):
    text = text.lower()

    quiz_keywords = ["quiz", "test", "mcq"]
    question_keywords = ["how", "what", "why", "define", "explain"]
    flashcard_keywords = ["flashcard", "revise", "review"]
    progress_keywords = ["progress", "score", "track", "report"]
    mood_keywords = ["mood", "feel", "emotion", "mental", "state"]

    if any(word in text for word in quiz_keywords):
        return "generate_quiz"
    elif any(word in text for word in question_keywords):
        return "ask_question"
    elif any(word in text for word in flashcard_keywords):
        return "show_flashcards"
    elif any(word in text for word in progress_keywords):
        return "track_progress"
    elif any(word in text for word in mood_keywords):
        return "track_mood"
    else:
        return "unknown"
