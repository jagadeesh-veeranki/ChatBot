# 📖 Usage Guide

## Web Interface

The easiest way to use the bot is via the included Web UI.

1. Open `frontend/index.html` in Chrome/Firefox/Edge.
2. Type a message in the input box and press Enter.

### Supported Commands

* **Greetings**: "Hello", "Hi", "Hey"
* **Help**: "Help me", "What can you do?"
* **Weather**: "Check weather", "Weather in London"
  * *Note*: The bot will ask for a city if you just say "Weather".
* **Emotional Support**: "I am sad today", "This is great!"

## API Usage

You can integrate the bot into other applications using HTTP requests.

### Example: Curl

```bash
curl -X POST http://localhost:5000/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello", "session_id": "cli_user"}'
```

### Example: Python Requests

```python
import requests

response = requests.post(
    "http://localhost:5000/api/chat",
    json={"message": "Hello", "session_id": "python_script"}
)
print(response.json()['response'])
```
