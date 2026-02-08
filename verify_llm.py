import os
import sys
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def verify_llm_connection():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("[ERROR] GOOGLE_API_KEY not found in environment variables.")
        return

    print(f"[INFO] Found API Key: {api_key[:8]}...{api_key[-4:]}")

    # List models to see what's available
    # url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    
    # Use gemini-2.0-flash as confirmed by list_models
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}

    payload = {
        "contents": [{
            "parts": [{"text": "Explain quantum computing in 2 sentences."}]
        }],
        "generationConfig": {
            "maxOutputTokens": 200
        }
    }

    print("Checking Google Gemini API connectivity (gemini-2.0-flash)...")
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            try:
                content = data['candidates'][0]['content']['parts'][0]['text']
                print("[SUCCESS] API Connection Successful!")
                print(f"[BOT] Response: {content}")
            except (KeyError, IndexError):
                print("[ERROR] API Response Format Issue")
                print(data)
        else:
            print(f"[ERROR] API Request Failed: {response.status_code}")
            print(f"Details: {response.text}")

    except Exception as e:
        print(f"[ERROR] Connection Error: {e}")

if __name__ == "__main__":
    verify_llm_connection()
