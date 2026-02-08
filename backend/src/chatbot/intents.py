

INTENTS = [
    {
        "tag": "greeting",
        "patterns": ["hi", "hello", "hey", "good morning", "what's up", "howdy"],
        "responses": ["Hello there!", "Hi! How can I help you today?", "Hey! Nice to see you.", "Greetings!"]
    },
    {
        "tag": "farewell",
        "patterns": ["bye", "goodbye", "see you", "later", "cya", "exit", "quit"],
        "responses": ["Goodbye!", "See you later!", "Have a great day!", "Until next time!"]
    },
    {
        "tag": "help",
        "patterns": ["help", "support", "what can you do", "assistance", "guide"],
        "responses": ["I can help you with basic questions. Try saying 'hello' or ask about me."]
    },
    {
        "tag": "about",
        "patterns": ["who are you", "what are you", "your name", "bot"],
        "responses": ["I am the AI Chatbot v1, a rule-based AI built for learning purposes."]
    },
    {
        "tag": "weather",
        "patterns": ["weather", "rain", "sunny", "forecast"],
        "responses": ["I can't check real-time weather yet, but I hope it's nice outside!"]
    }
]
