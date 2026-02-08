import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chatbot.chatbot_v1 import RuleBasedChatbot
from src.chatbot.chatbot_v2 import NLPChatbot

test_cases = [
    ("Hello there", True, True),
    ("I am running", False, True),
    ("Weather forecast", True, True),
    ("Tell me about yourself", True, True),
    ("Give me assistance", True, True),
    ("Helping me", False, True),
]

def run_comparison():
    bot_v1 = RuleBasedChatbot()
    bot_v2 = NLPChatbot()
    
    print(f"{'Input':<25} | {'v1 (Basic)':<15} | {'v2 (NLP)':<15}")
    print("-" * 60)
    
    for text, expected_v1, expected_v2 in test_cases:
        resp_v1 = bot_v1.get_response(text)
        resp_v2 = bot_v2.get_response(text)
        

        success_v1 = "I didn't understand" not in resp_v1
        success_v2 = "I didn't understand" not in resp_v2
        
        v1_mark = "✅" if success_v1 else "❌"
        v2_mark = "✅" if success_v2 else "❌"
        
        print(f"{text:<25} | {v1_mark:<15} | {v2_mark:<15}")

if __name__ == "__main__":
    run_comparison()
