import sqlite3
import json
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), '../../data/chatbot.db')

class DatabaseManager:
    def __init__(self):
        # Ensure data directory exists
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        
        # Sessions Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                user_id TEXT PRIMARY KEY,
                context_state TEXT,
                data TEXT,  -- JSON string
                last_active TIMESTAMP
            )
        ''')
        
        # Messages Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                sender TEXT,  -- 'user' or 'bot'
                text TEXT,
                sentiment TEXT, -- 'positive', 'neutral', 'negative'
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES sessions(user_id)
            )
        ''')
        
        self.conn.commit()

    def update_session(self, user_id, context_state=None, data=None):
        cursor = self.conn.cursor()
        
        # Check if exists
        cursor.execute("SELECT data FROM sessions WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        
        current_data = {}
        if row:
            if row[0]:
                try:
                    current_data = json.loads(row[0])
                except:
                    current_data = {}
        
        # Merge new data
        if data:
            current_data.update(data)
            
        json_data = json.dumps(current_data)
        now = datetime.now()
        
        cursor.execute('''
            INSERT OR REPLACE INTO sessions (user_id, context_state, data, last_active)
            VALUES (?, ?, ?, ?)
        ''', (user_id, context_state, json_data, now.isoformat()))
        
        self.conn.commit()

    def get_session(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT context_state, data FROM sessions WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        
        if row:
            data = {}
            if row[1]:
                try:
                    data = json.loads(row[1])
                except:
                    pass
            return {"context_state": row[0], "data": data}
        return None

    def log_message(self, user_id, sender, text, sentiment=None):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO messages (user_id, sender, text, sentiment)
            VALUES (?, ?, ?, ?)
        ''', (user_id, sender, text, sentiment))
        self.conn.commit()

    def get_history(self, user_id, limit=10):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT sender, text, timestamp FROM messages
            WHERE user_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (user_id, limit))
        return cursor.fetchall()[::-1] # Reverse to chronological order

if __name__ == "__main__":
    db = DatabaseManager()
    print("Database initialized.")
