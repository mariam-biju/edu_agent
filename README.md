# 🧠 Ai-thena – AI Learning Companion

**Ai-thena** is a gamified AI-powered learning assistant built with Streamlit.  
It integrates quizzes, flashcards, academic Q&A, mood tracking, and performance tracking — all in a modular, interactive web app.

---

## 🚀 Features

- 💬 AI-Powered Q&A using Wikipedia  
- 📝 Quiz Generator (hardcoded questions with difficulty adjustment)  
- 📚 Flashcards for active recall  
- 🎉 Gamification: confetti celebration, level-up logic  
- 📊 Progress visualization using bar charts  
- 😊 Mood tracker with emoji feedback  
- 📅 Study calendar with upcoming academic holidays  
- 🔐 (Optional) Authentication-ready structure  
- 🎨 Custom branding with logo support  

---

## 🧱 Folder Structure

Ai-thena/  
├── main.py                  # Streamlit frontend  
├── chat.py                  # Wikipedia-powered Q&A  
├── quiz.py                  # Quiz logic & scoring  
├── gamification.py          # Leveling, streaks, celebrations  
├── flashcards.py            # Interactive flashcards  
├── mood.py                  # Mood tracker  
├── db_utils.py              # Quiz history via SQLite  
├── calendar_utils.py        # Academic holiday list  
├── static/                  # Assets like logos  
│   └── athena_logo.png  

---

## 🧠 How It Works

- **Q&A Chat**: Uses Wikipedia to answer user questions  
- **Quiz Generator**: Questions change difficulty based on user’s score history  
- **Confetti Celebration**: Triggered when user scores highly  
- **Progress Graph**: Plots topics vs quiz scores using matplotlib  
- **Flashcards**: Simple left/right gestures using Streamlit widgets  
- **Mood Tracker**: Select mood → gets stored in memory  
- **Study Calendar**: Hardcoded list of upcoming holidays  

---

## 🖼️ Sample User Flow

1. Select **"AI Chat"** from sidebar → ask an academic question  
2. Choose **"Quiz"** → enter topic and take quiz  
3. See your score → unlock celebration and level  
4. Check progress → view bar chart of quiz history  
5. Use flashcards or track your daily mood  

---

## 📦 Requirements

pip install streamlit wikipedia matplotlib

---

## ▶️ How to Run

```bash
streamlit run main.py
```

Then go to:

```
http://localhost:8501/
```

---

## ⚙️ Future Enhancements (Ideas)

- 🔐 Add Google/GitHub OAuth  
- 🧠 Replace Wikipedia with GPT or Gemini API  
- 🎙️ Voice-based question input  
- ☁️ Deploy on Streamlit Cloud / Hugging Face Spaces  

---
