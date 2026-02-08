import os
import sys
import requests
import json
from src.chatbot.chatbot_v6 import AdvancedChatbot

class LLMChatbot(AdvancedChatbot):
    def __init__(self):
        super().__init__()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.system_prompt = """You are an advanced large language model–based assistant similar to ChatGPT.

Purpose:
- Provide accurate, helpful, and human-like responses.
- Assist users with technical and non-technical questions.
- Maintain conversational context across turns.

Security & API Usage Rules:
- You do not reveal, repeat, or expose any API keys, secrets, tokens, or credentials.
- If asked about API keys, explain their purpose conceptually without showing values.
- Assume authentication is handled securely via environment variables.
- Never suggest hardcoding secrets in source code.

Behavior Rules:
- Always respond clearly, politely, and professionally.
- Adapt explanation depth based on user expertise.
- If asked for code, provide clean, correct, and best-practice implementations.
- If ambiguous, ask a brief clarifying question.
- Never hallucinate facts or APIs.

Style Guidelines:
- Friendly, calm, and confident tone.
- Concise by default, detailed when requested.
- No robotic or repetitive replies.
"""

    def get_response(self, user_input, user_id='default_user'):
        # 1. Log User Message & Sentiment (handled by v6/DB)
        # We call the DB logic manually here to ensure logging happens before LLM call
        # But v6.get_response does logic + response. We want to override logic.
        
        # Re-use v6 sentiment analysis for database logging
        # (Copying logic is cleaner than super().get_response() which would trigger v4 logic)
        from src.utils.sentiment import analyze_sentiment
        polarity, sentiment_label = analyze_sentiment(user_input)
        self.db.log_message(user_id, 'user', user_input, sentiment_label)

        # 2. Check for API Key (Fallback to v6 if missing)
        if not self.api_key:
            print("[WARNING] No OPENAI_API_KEY found. Falling back to Rule-Based Bot.")
            return super().get_response(user_input, user_id)

        # 3. Call OpenAI API
        try:
            # Get Context History (Last 10 messages)
            history_rows = self.db.get_history(user_id, limit=10)
            messages = [{"role": "system", "content": self.system_prompt}]
            
            # History is [(sender, text, timestamp), ...] chronologically
            # Sender is 'user' or 'bot'. OpenAI expects 'user' or 'assistant'.
            for sender, text, _ in history_rows:
                role = "user" if sender == "user" else "assistant"
                messages.append({"role": role, "content": text})

            # Append current message (It was logged but get_history might miss it if DB is slow or we just logged it)
            # Actually get_history reads from DB. We just wrote to DB. So it should be there?
            # get_history limit=10 returns last 10.
            # To be safe and ensure it is included, we can trust DB or append explicitly.
            # Since we just logged it, it is in DB.
            
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": messages,
                "temperature": 0.7
            }
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }

            resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            resp.raise_for_status()
            
            llm_response = resp.json()['choices'][0]['message']['content']
            
            # 4. Log Bot Response
            self.db.log_message(user_id, 'bot', llm_response, 'NEUTRAL')
            
            return llm_response

        except Exception as e:
            fallback = f"I'm encountering an issue connecting to my brain ({str(e)}). Switching to offline mode."
            print(f"LLM Error: {e}")
            self.db.log_message(user_id, 'bot', fallback, 'NEGATIVE')
            return super().get_response(user_input, user_id)

if __name__ == "__main__":
    bot = LLMChatbot()
    print("🤖 Advanced AI Assistant (LLM-Powered)")
    print("Type 'quit' to exit.")
    while True:
        u = input("You: ")
        if u.lower() == 'quit': break
        print(f"Bot: {bot.get_response(u)}")
