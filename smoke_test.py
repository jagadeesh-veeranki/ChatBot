
import sys
import os

# Add backend to path specifically
sys.path.append(os.path.join(os.getcwd(), 'backend'))

try:
    print("Attempting to import app...")
    from backend.app import create_app
    app = create_app()
    print("App created successfully.")
    
    print("Attempting to import bot logic...")
    from backend.src.chatbot.chatbot_v7 import LLMChatbot
    bot = LLMChatbot()
    print("Bot initialized successfully.")
    
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)
