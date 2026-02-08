import time

class ContextManager:
    """
    Manages session state and conversation context for users.
    Stores data in-memory for now (Phase 4).
    """
    def __init__(self):
        # Dictionary structure:
        # {
        #   "user_id": {
        #       "context_state": "awaiting_city", 
        #       "data": {"city": "London"}, 
        #       "history": [],
        #       "last_active": timestamp
        #   }
        # }
        self.sessions = {}

    def get_session(self, user_id):
        if user_id not in self.sessions:
            self.sessions[user_id] = {
                "context_state": None,
                "data": {},
                "history": [],
                "last_active": time.time()
            }
        self.sessions[user_id]["last_active"] = time.time()
        return self.sessions[user_id]

    def set_context(self, user_id, context_state):
        session = self.get_session(user_id)
        session["context_state"] = context_state

    def get_context(self, user_id):
        session = self.get_session(user_id)
        return session.get("context_state")

    def clear_context(self, user_id):
        session = self.get_session(user_id)
        session["context_state"] = None

    def update_data(self, user_id, key, value):
        session = self.get_session(user_id)
        session["data"][key] = value

    def get_data(self, user_id, key):
        session = self.get_session(user_id)
        return session["data"].get(key)
        
    def add_to_history(self, user_id, user_text, bot_response):
        session = self.get_session(user_id)
        session["history"].append({"user": user_text, "bot": bot_response})
