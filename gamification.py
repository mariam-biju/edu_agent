import streamlit as st

def show_celebration(score, total):
    percentage = score / total

    if score == total:
        st.balloons()
        st.success("🏆 Perfect Score! You're a genius!")
    elif percentage >= 0.8:
        st.success("🎉 Great job! Keep it up!")
    elif percentage >= 0.5:
        st.info("🙂 Good attempt! Review and try again.")
    else:
        st.warning("😅 Keep practicing! You’ll improve with time.")

def get_level(score, total=5):
    percentage = score / total
    if percentage == 1.0:
        return "Expert"
    elif percentage >= 0.8:
        return "Advanced"
    elif percentage >= 0.5:
        return "Intermediate"
    else:
        return "Beginner"
