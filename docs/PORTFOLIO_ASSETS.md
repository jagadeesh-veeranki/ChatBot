# 💼 Portfolio Assets

## 🎥 Demo Video Script (60 Seconds)

**Scene 1: Intro (0:00-0:10)**

* *Visual*: Split screen showing code (VS Code) and the clean Web UI.
* *Audio*: "Hi, I'm Jagadeesh. This is my AI Chatbot, a context-aware AI chatbot I built from scratch using Python, Flask, and Scikit-learn."

**Scene 2: NLP & ML (0:10-0:25)**

* *Visual*: Typing "Hello" and "I need help with python". Show terminal logs revealing intent classification probabilities.
* *Audio*: "Unlike basic script bots, this bot uses a Naive Bayes classifier trained on custom datasets to understand intent, backed by NLTK for robust text processing."

**Scene 3: Context & Advanced Features (0:25-0:45)**

* *Visual*: Typing "Check weather" -> Bot asks "Which city?" -> Typing "Tokyo" -> Bot shows real weather data.
* *Audio*: "It maintains conversation state across turns using a custom context manager and integrates with external APIs to fetch real-time data like weather."

**Scene 4: Engineering (0:45-1:00)**

* *Visual*: Showing Dockerfile, GitHub Actions workflow, and API Docs.
* *Audio*: "The entire system is Dockerized, includes a CI/CD pipeline, and features a scalable REST API. Check out the code on my GitHub."

---

## 📝 Blog Post Outline

**Title**: How I Built a Production-Grade Chatbot from Scratch (No GPT APIs)

**Introduction**

* The challenge: Building an ML chatbot without relying on OpenAI wrapper-libraries.
* Goal: Understanding the core mechanics of NLP and system design.

**The Tech Stack**

* Python & Flask for the backend.
* Scikit-learn & NLTK for the "Brain".
* Vanilla JS for a lightweight frontend.

**Key Challenges Solved**

1. **Context Management**: Handling multi-turn conversations (Simulating memory).
2. **Intent Classification**: Training a model on limited data.
3. **State Persistence**: Implementing SQLite to save sessions.

**Conclusion**

* Lessons learned about system architecture.
* Link to GitHub repository.
