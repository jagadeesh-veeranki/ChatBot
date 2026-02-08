import pickle
import json
import random
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.utils.nlp_utils import preprocess
from src.utils.context_manager import ContextManager


def clean_text(text):
    tokens = preprocess(text)
    return " ".join(tokens)

class ContextChatbot:
    def __init__(self):

        # Updated paths for new folder structure (backend/src/chatbot/ -> backend/../..)
        # Current file is in backend/src/chatbot/
        # Root is backend/
        # Data is in backend/data/ (if moved) OR root/data?
        # Let's check where data folder is.
        # list_dir showed 'data' is in root c:\Chatbot\data
        # So path from backend/src/chatbot is ../../../data
        
        base_dir = os.path.dirname(__file__)
        # Go up 3 levels: src/chatbot -> src -> backend -> root
        root_dir = os.path.abspath(os.path.join(base_dir, '../../../'))
        
        model_path = os.path.join(root_dir, 'models', 'chatbot_model.pkl')
        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
        except FileNotFoundError:
            print(f"Model not found at {model_path}. Please run training.")
            self.model = None

        data_file = os.path.join(root_dir, 'data', 'intents.json')
        try:
            with open(data_file, 'r') as f:
                self.intents = json.load(f)
        except FileNotFoundError:
             print(f"Intents not found at {data_file}.")
             self.intents = []

        self.context_manager = ContextManager()

    def get_response(self, user_input, user_id='default_user'):
        if not user_input:
            return "Please say something."


        current_context = self.context_manager.get_context(user_id)
        

        
        clean_input = clean_text(user_input)
        if self.model:
            predicted_tag = self.model.predict([clean_input])[0]
            probs = self.model.predict_proba([clean_input])[0]
            max_prob = max(probs)
        else:
            predicted_tag = "error"
            max_prob = 0


        

        if current_context == 'awaiting_city':

            if predicted_tag == 'farewell' or 'cancel' in user_input.lower():
                self.context_manager.clear_context(user_id)
                return "Cancelled request."
                

            city_name = user_input
            self.context_manager.update_data(user_id, 'city', city_name)
            self.context_manager.clear_context(user_id)
            return f"Weather in {city_name} is sunny! (Simulated)"


        if max_prob < 0.2:
            return "I'm not sure. Can you rephrase?"


        matched_intent = next((i for i in self.intents if i['tag'] == predicted_tag), None)
        
        if matched_intent:
            if 'context_set' in matched_intent:
                self.context_manager.set_context(user_id, matched_intent['context_set'])
            

            
            return random.choice(matched_intent['responses'])
            
        return "I'm lost."

if __name__ == "__main__":
    bot = ContextChatbot()
    print("🤖 AI Chatbot v4 (Context-Aware)")
    
    user_id = "test_user"
    
    while True:
        try:
            user_text = input("You: ")
            if user_text.strip().lower() in ['quit', 'exit']:
                break
                
            response = bot.get_response(user_text, user_id)
            print(f"Bot: {response}")
            
        except KeyboardInterrupt:
            break
