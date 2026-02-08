import random
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.chatbot.intents import INTENTS
from src.utils.nlp_utils import preprocess, stem

class NLPChatbot:
    def __init__(self):
        self.intents = INTENTS
        self.processed_intents = []
        for intent in self.intents:
            processed_patterns = []
            for pattern in intent['patterns']:
                processed_patterns.append(preprocess(pattern))
            
            self.processed_intents.append({
                "tag": intent['tag'],
                "patterns": processed_patterns,
                "responses": intent['responses']
            })

    def get_response(self, user_input: str) -> str:
        if not user_input:
            return "Please say something."

        user_tokens = preprocess(user_input)
        
        if not user_tokens:
            return "I couldn't understand that. Please use more words."

        best_match = None
        highest_score = 0

        for intent in self.processed_intents:
            for pattern_tokens in intent['patterns']:
                if not pattern_tokens: continue
                
                common_tokens = set(user_tokens) & set(pattern_tokens)
                score = len(common_tokens)
                
                if score > highest_score:
                    highest_score = score
                    best_match = intent

        if best_match and highest_score > 0:
            return random.choice(best_match['responses'])
        
        return "I'm sorry, I didn't understand that. Could you rephrase?"

if __name__ == "__main__":
    bot = NLPChatbot()
    print("🤖 AI Chatbot v2")
    print("Type 'quit' to exit.\n")
    
    while True:
        try:
            user_text = input("You: ")
            if user_text.strip().lower() in ['quit', 'exit']:
                print("Bot: Goodbye!")
                break
                
            response = bot.get_response(user_text)
            print(f"Bot: {response}")
            
        except KeyboardInterrupt:
            print("\nBot: Exiting...")
            break
