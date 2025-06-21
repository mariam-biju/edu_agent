import streamlit as st
from datetime import datetime

# In-memory mood log
mood_log = {}

def mood_tracker():
    st.subheader("🧠 Mood Tracker")

    moods = {
        "🙂 Happy": "That's awesome! Keep up the good vibes!",
        "😐 Neutral": "A calm mind is a focused mind. Keep going!",
        "😔 Tired": "It's okay to feel tired. Take a break and recharge."
    }

    mood = st.radio("How are you feeling today?", list(moods.keys()), index=None)

    if mood and st.button("Submit Mood"):
        today = datetime.today().strftime('%Y-%m-%d')
        mood_log[today] = mood
        st.success(f"{moods[mood]}")
        st.info(f"🗓️ Logged for: {today}")

    if mood_log:
        with st.expander("📅 Mood History"):
            for date, mood in sorted(mood_log.items(), reverse=True):
                st.write(f"{date}: {mood}")

def remember_mood():
    if mood_log:
        latest_day = sorted(mood_log.keys())[-1]
        return mood_log[latest_day]
    return "Neutral"
