import streamlit as st
from chat import answer_query
from quiz import generate_quiz, check_answers, get_user_difficulty
from gamification import show_celebration, get_level
from flashcards import show_flashcards
from mood import mood_tracker
from db_utils import init_db, store_score, get_progress_data, get_average_score
from quote_api import get_motivational_quote
from calendar_utils import get_holidays
import matplotlib.pyplot as plt

st.set_page_config(page_title="Ai-thena", layout="wide", page_icon="🧠")
init_db()

st.sidebar.title("🧠 Ai-thena")
st.sidebar.markdown(get_motivational_quote())

menu = st.sidebar.radio("Navigate", ["AI Chat", "Quiz", "Flashcards", "Progress", "Mood Tracker", "Study Calendar"])

# AI Chat
if menu == "AI Chat":
    st.subheader("💬 Ask Ai-thena")
    user_input = st.text_input("Ask an academic question:")
    if user_input:
        st.success(answer_query(user_input))

# Quiz
elif menu == "Quiz":
    st.subheader("📝 Quiz Generator")

    if "quiz_started" not in st.session_state:
        st.session_state["quiz_started"] = False
    if "quiz_submitted" not in st.session_state:
        st.session_state["quiz_submitted"] = False

    topic = st.text_input("Enter a topic:")

    if st.button("Generate Quiz") and topic:
        avg_score = get_average_score(topic)
        difficulty = get_user_difficulty(avg_score)
        st.info(f"Generating a {difficulty} level quiz on: {topic}")
        st.session_state["questions"] = generate_quiz(topic, difficulty)
        st.session_state["quiz_started"] = True
        st.session_state["quiz_submitted"] = False

    if st.session_state["quiz_started"]:
        for q in st.session_state["questions"]:
            st.radio(q["question"], q["options"], key=q["question"], index=None)

        if st.button("Submit Quiz") and not st.session_state["quiz_submitted"]:
            if any(st.session_state.get(q["question"]) is None for q in st.session_state["questions"]):
                st.warning("⚠️ Please answer all questions before submitting.")
            else:
                score = check_answers(st.session_state["questions"])
                store_score(topic, score, len(st.session_state["questions"]))
                show_celebration(score, len(st.session_state["questions"]))
                st.success(f"🎯 You scored {score}/{len(st.session_state['questions'])}")
                st.info(f"🏅 Level: {get_level(score)}")
                st.session_state["quiz_submitted"] = True

# Flashcards
elif menu == "Flashcards":
    show_flashcards()

# Progress
elif menu == "Progress":
    st.subheader("📊 Your Progress")
    data = get_progress_data()
    if data:
        topics, scores = zip(*data)
        fig, ax = plt.subplots()
        ax.bar(topics, scores)
        st.pyplot(fig)
    else:
        st.info("No quiz history yet.")

# Mood Tracker
elif menu == "Mood Tracker":
    mood_tracker()

# Study Calendar
elif menu == "Study Calendar":
    st.title("📅 Upcoming Holidays")
    holidays = get_holidays()
    for h in holidays:
        st.write("🗓️", h)
