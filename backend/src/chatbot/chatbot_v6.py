import sys
import os
import random

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.chatbot.chatbot_v4 import ContextChatbot
from src.utils.database import DatabaseManager
from src.utils.sentiment import analyze_sentiment
from src.utils.external_apis import ExternalAPIs

class AdvancedChatbot(ContextChatbot):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()

    def get_response(self, user_input, user_id='default_user'):
        polarity, sentiment_label = analyze_sentiment(user_input)
        
        self.db.log_message(user_id, 'user', user_input, sentiment_label)
        
        session_data = self.db.get_session(user_id)
        if session_data:
            if user_id not in self.context_manager.sessions:
                 self.context_manager.get_session(user_id)
            
            self.context_manager.sessions[user_id]['context_state'] = session_data['context_state']
            self.context_manager.sessions[user_id]['data'] = session_data['data']

        prefix = ""
        if sentiment_label == "NEGATIVE" and polarity < -0.5:
            prefix = "[Noticed you're upset...] "
        
        response = super().get_response(user_input, user_id)
        
        if "(Simulated)" in response:
            try:
                city = self.context_manager.sessions[user_id]['data'].get('city')
                if city:
                    real_weather = ExternalAPIs.get_weather(city)
                    response = real_weather
            except Exception as e:
                response += f" (Real API failed: {e})"
                
        current_session = self.context_manager.get_session(user_id)
        self.db.update_session(user_id, current_session['context_state'], current_session['data'])
        
        final_response = prefix + response
        self.db.log_message(user_id, 'bot', final_response, 'NEUTRAL')
        
        return final_response

if __name__ == "__main__":
    bot = AdvancedChatbot()
    print("🤖 AI Chatbot v6 (Advanced: DB + Sentiment + API)")
    
    uid = "advanced_user"
    while True:
        try:
            uargs = input("You: ")
            if uargs.lower() in ['quit', 'exit']:
                break
            resp = bot.get_response(uargs, uid)
            print(f"Bot: {resp}")
        except KeyboardInterrupt:
            break
