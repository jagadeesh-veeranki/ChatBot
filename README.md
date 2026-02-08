# AI Assistant ChatBot (Production Ready)

A professional, full-stack AI chatbot aimed at providing accurate, helpful, and human-like assistance.  
**Live Demo:** [Link to your GitHub Page]

---

## 🚀 Features

- **Modern UI**: Dark mode, responsive design, markdown rendering, and code highlighting.
- **AI Powered**: Uses OpenAI's GPT models (via backend) with a custom "Senior Engineer" persona.
- **Smart Fallback**: Automatically switches to a local rule-based model if the API is unavailable.
- **Persistence**: Remembers your conversation history (session-based).

## 🛠 Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JS (No frameworks, high performance).
- **Backend**: Python (Flask), SQLite, OpenAI API.
- **Deployment**:
  - Frontend: GitHub Pages
  - Backend: Render / Railway / Localhost

## 📂 Project Structure

```
/
├── index.html        # Frontend Entry
├── css/              # Styles
├── js/               # Application Logic
├── backend/          # Server API
│   ├── app.py        # Flask App
│   ├── routes.py     # Endpoints
│   └── src/          # Chatbot Logic
└── README.md
```

## 🏃‍♂️ How to Run Locally

1. **Clone the Repo**

   ```bash
   git clone https://github.com/yourusername/chatbot.git
   cd chatbot
   ```

2. **Setup Backend**

   ```bash
   cd backend
   pip install -r requirements.txt
   
   # Set API Key (Optional, for LLM mode)
   # Windows (PowerShell)
   $env:OPENAI_API_KEY="sk-your-key"
   
   python app.py
   ```

   *Server starts at `http://127.0.0.1:5000`*

3. **Run Frontend**
   - Simply open `index.html` in your browser.
   - Or run a local server: `python -m http.server 8000`

## 🔒 Security Note

- **API Keys**: Stored ONLY in backend environment variables. Never exposed in frontend code.
- **CORS**: Configured to allow requests from the frontend.

---
*Built with ❤️ by Jagadeesh*
