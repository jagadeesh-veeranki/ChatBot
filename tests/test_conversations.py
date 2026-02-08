import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chatbot.chatbot_v4 import ContextChatbot

def test_multiturn():
    bot = ContextChatbot()
    user_id = "test_user_123"
    
    conversation = [
        "Hello",                  # Expect: Greeting
        "What is the weather?",   # Expect: Ask for city (set context)
        "Hyderabad",              # Expect: Weather report (context consumed)
        "Thanks",                 # Expect: Gratitude
    ]
    
    print(f"--- Testing Multi-Turn Conservation (User: {user_id}) ---")
    
    for text in conversation:
        print(f"You: {text}")
        response = bot.get_response(text, user_id)
        print(f"Bot: {response}")
        
    print("\n--- Context Verification ---")
    # Context should be clear now
    context = bot.context_manager.get_context(user_id)
    print(f"Current Context: {context} (Expected: None)")
    
    if context is None:
        print("✅ Context cleared successfully.")
    else:
        print("❌ Context stuck.")

if __name__ == "__main__":
    test_multiturn()
