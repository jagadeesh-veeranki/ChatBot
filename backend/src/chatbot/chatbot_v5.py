import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.chatbot.chatbot_v4 import ContextChatbot
from src.utils.prompt_loader import PromptLoader

class SystemPromptChatbot(ContextChatbot):
    def __init__(self):
        super().__init__()
        self.prompt_loader = PromptLoader()
        try:
            self.system_prompt = self.prompt_loader.load_prompt()
            print("System Prompt loaded.")
        except Exception as e:
            print(f"Warning: Could not load system prompt: {e}")
            self.system_prompt = "You are a helpful assistant."

    def get_system_persona(self):
        """Returns the core identity from the system prompt."""
        return self.prompt_loader.get_layer("IDENTITY")

    # In a real LLM integration, we would prepend this to the message history.
    # For now, we expose it for debugging or future API usage.

if __name__ == "__main__":
    bot = SystemPromptChatbot()
    print("\n--- Active Persona ---")
    print(bot.get_system_persona())
    print("\n--- Bot Ready ---")
    
    # Simple loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            break
        print(f"Bot: {bot.get_response(user_input)}")
