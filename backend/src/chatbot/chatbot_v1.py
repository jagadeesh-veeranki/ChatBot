import random
from src.chatbot.intents import INTENTS

class RuleBasedChatbot:

    def __init__(self):
        self.intents = INTENTS

    def get_response(self, user_input: str) -> str:

        if not user_input:
            return "Please say something."

        user_input = user_input.lower()


        for intent in self.intents:
            for pattern in intent['patterns']:

                if pattern in user_input:
                    return random.choice(intent['responses'])
        

        return "I'm sorry, I didn't understand that. Could you rephrase?"

if __name__ == "__main__":
    bot = RuleBasedChatbot()
    print("🤖 AI Chatbot v1 (Rule-Based)")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
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
