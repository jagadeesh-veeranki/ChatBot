# ChatBot AI (Production Ready)

A professional, full-stack AI chatbot aimed at providing accurate, helpful, and human-like assistance.  
**Live Demo:** [https://jagadeesh-veeranki.github.io/ChatBot](https://jagadeesh-veeranki.github.io/ChatBot)

---

## 🚀 Features

- **Modern UI**: Dark mode suppport, responsive design, markdown rendering, and syntax highlighting for code blocks.
- **AI Powered**: Integrates with OpenAI's GPT models (GPT-3.5/4) via a secure backend proxy to provide intelligent responses.
- **Smart Fallback**: Automatically switches to a local, rule-based NLTK model if the API key is missing or the service is down, ensuring 100% uptime.
- **Context Awareness**: Maintains conversation history (persisted via SQLite) to provide context-aware answers.
- **Secure**: API keys are stored only on the backend server, never exposed to the client.

## 🛠 Tech Stack

- **Frontend**:
  - HTML5, CSS3 (Custom responsive design)
  - Vanilla JavaScript (ES6+)
  - `marked.js` (Markdown parsing)
  - `highlight.js` (Code syntax highlighting)
- **Backend**:
  - Python 3.x
  - Flask (REST API)
  - OpenAI API (LLM Integration)
  - NLTK & Scikit-learn (Natural Language Processing & Intent Classification)
  - SQLite (Session storage)
- **Deployment**:
  - Frontend: GitHub Pages
  - Backend: Render / Railway / Fly.io

## 📂 Project Structure

```bash
/
├── index.html        # Frontend Entry Point (Hosted on GitHub Pages)
├── css/              # Stylesheets (Chat, Responsive, Theme)
├── js/               # Application Logic (API, UI, State)
├── assets/           # Images and Icons
├── backend/          # Server-side Application
│   ├── app.py        # Flask Application Entry
│   ├── routes.py     # API Endpoints
│   ├── requirements.txt # Python Dependencies
│   └── src/          # Chatbot Logic (LLM + Rule-based)
└── README.md         # Documentation
```

## 🏃‍♂️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/jagadeesh-veeranki/ChatBot.git
cd ChatBot
```

### 2. Setup Backend

Navigate to the backend directory and install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

**Optional: Set your OpenAI API Key**
(If skipped, the bot will run in "Offline Rule-Based" mode)

**Windows (PowerShell):**

```powershell
$env:OPENAI_API_KEY="sk-your-openai-key-here"
```

**Linux/Mac:**

```bash
export OPENAI_API_KEY="sk-your-openai-key-here"
```

**Start the Server:**

```bash
python app.py
```

*Server starts at `http://127.0.0.1:5000`*

### 3. Run Frontend

Since the frontend is static HTML/JS:

1. Simply open `index.html` in your browser.
2. OR serve it locally:

   ```bash
   # From project root
   python -m http.server 8000
   ```

   Access at `http://localhost:8000`.

## 🔒 Security Note

- **API Keys**: Stored ONLY in backend environment variables. Never exposed in frontend code.
- **CORS**: Configured to allow requests from the frontend origin.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---
Built with ❤️ by Jagadeesh
