import unittest
import sys
import os



from src.chatbot.chatbot_v1 import RuleBasedChatbot
from src.chatbot.intents import INTENTS

class TestRuleBasedChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = RuleBasedChatbot()

    def test_greeting(self):

        response = self.bot.get_response("Hello there")

        greeting_responses = next(i['responses'] for i in INTENTS if i['tag'] == 'greeting')
        self.assertIn(response, greeting_responses)

    def test_farewell(self):

        response = self.bot.get_response("bye now")
        farewell_responses = next(i['responses'] for i in INTENTS if i['tag'] == 'farewell')
        self.assertIn(response, farewell_responses)
        
    def test_help(self):

        response = self.bot.get_response("I need help")
        help_responses = next(i['responses'] for i in INTENTS if i['tag'] == 'help')
        self.assertIn(response, help_responses)

    def test_unknown(self):

        response = self.bot.get_response("Supercalifragilisticexpialidocious")
        self.assertEqual(response, "I'm sorry, I didn't understand that. Could you rephrase?")

    def test_case_insensitivity(self):

        response_lower = self.bot.get_response("hello")
        response_upper = self.bot.get_response("HELLO")
        
        greeting_responses = next(i['responses'] for i in INTENTS if i['tag'] == 'greeting')
        self.assertIn(response_lower, greeting_responses)
        self.assertIn(response_upper, greeting_responses)

if __name__ == '__main__':
    unittest.main()
