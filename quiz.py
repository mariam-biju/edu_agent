import streamlit as st

def generate_quiz(topic, difficulty="easy"):
    topic = topic.lower()
    
    if topic == "ai" or topic == "artificial intelligence":
        return [
            {
                "question": "What is Artificial Intelligence (AI)?",
                "options": [
                    "A branch of biology",
                    "A computer system's ability to mimic human intelligence",
                    "A type of smartphone",
                    "An ancient language"
                ],
                "answer": "A computer system's ability to mimic human intelligence"
            },
            {
                "question": "Which of these is a real-world use of AI?",
                "options": [
                    "Growing plants faster",
                    "Digital assistants like Siri and Alexa",
                    "Producing electricity",
                    "Catching fish"
                ],
                "answer": "Digital assistants like Siri and Alexa"
            },
            {
                "question": "Which programming language is popular for AI development?",
                "options": [
                    "Python",
                    "HTML",
                    "CSS",
                    "Sketch"
                ],
                "answer": "Python"
            }
        ]
    
    elif topic == "photosynthesis":
        return [
            {
                "question": "What is the main product of photosynthesis?",
                "options": [
                    "Carbon dioxide",
                    "Water",
                    "Oxygen",
                    "Nitrogen"
                ],
                "answer": "Oxygen"
            },
            {
                "question": "Which part of the plant carries out photosynthesis?",
                "options": [
                    "Roots",
                    "Stem",
                    "Leaves",
                    "Flowers"
                ],
                "answer": "Leaves"
            },
            {
                "question": "Which gas is needed for photosynthesis?",
                "options": [
                    "Oxygen",
                    "Hydrogen",
                    "Carbon Dioxide",
                    "Nitrogen"
                ],
                "answer": "Carbon Dioxide"
            }
        ]
    
    else:
        return [
            {
                "question": f"Sorry, no quiz available for '{topic}'.",
                "options": ["A", "B", "C", "D"],
                "answer": "A"
            }
        ]

def check_answers(questions):
    score = 0
    for q in questions:
        if st.session_state.get(q["question"]) == q["answer"]:
            score += 1
    return score

def get_user_difficulty(avg_score):
    if avg_score < 2:
        return "easy"
    elif avg_score < 4:
        return "medium"
    return "hard"
