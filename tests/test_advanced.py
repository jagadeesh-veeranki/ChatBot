import unittest
import sys
import os



from src.chatbot.chatbot_v6 import AdvancedChatbot
from src.utils.sentiment import analyze_sentiment
from src.utils.database import DatabaseManager
from src.utils.external_apis import ExternalAPIs

class TestAdvancedFeatures(unittest.TestCase):
    def setUp(self):
        self.bot = AdvancedChatbot()
        self.user_id = "test_adv_user"
        self.bot.db.update_session(self.user_id, context_state=None, data={})

    def test_sentiment_analysis(self):

        pol, label = analyze_sentiment("I am very angry and sad.")
        self.assertEqual(label, "NEGATIVE")
        

        pol, label = analyze_sentiment("I love this chatbot, it's amazing!")
        self.assertEqual(label, "POSITIVE")

    def test_database_persistence(self):

        msg = "Hello DB"
        self.bot.get_response(msg, self.user_id)
        

        history = self.bot.db.get_history(self.user_id, limit=5)

        
        found_msg = False
        for h in history:
            if h[1] == "Hello DB":
                found_msg = True
                break
        self.assertTrue(found_msg)

    def test_api_integration(self):

        weather = ExternalAPIs.get_weather("London")
        self.assertIn("wind speeds", weather) 

        fake = ExternalAPIs.get_weather("AtlantisUnderwaterCity")
        self.assertIn("couldn't find", fake)

if __name__ == '__main__':
    unittest.main()
