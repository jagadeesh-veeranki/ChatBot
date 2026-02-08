import pickle
import json
import random
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.utils.nlp_utils import preprocess

def clean_text(text):

    tokens = preprocess(text)
    return " ".join(tokens)

class MLChatbot:
    def __init__(self):

        model_path = os.path.join(os.path.dirname(__file__), '../../models/chatbot_model.pkl')
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
            

        data_file = os.path.join(os.path.dirname(__file__), '../../data/intents.json')
        with open(data_file, 'r') as f:
            self.intents = json.load(f)

    def get_response(self, user_input):
        if not user_input:
            return "Please say something."


        clean_input = clean_text(user_input)
        

        predicted_tag = self.model.predict([clean_input])[0]
        

        probs = self.model.predict_proba([clean_input])[0]
        max_prob = max(probs)
        

        if max_prob < 0.4:
            return "I'm not sure I understand. Could you rephrase?"


        for intent in self.intents:
            if intent['tag'] == predicted_tag:
                return random.choice(intent['responses'])
                
        return "Error: Intent recognized but no response found."

if __name__ == "__main__":
    bot = MLChatbot()
    print("🤖 AI Chatbot v3 (Machine Learning)")
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
