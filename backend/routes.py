from flask import Blueprint, request, jsonify
import sys
import os
import time

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chatbot.chatbot_v7 import LLMChatbot

api_bp = Blueprint('api', __name__)

# Initialize bot (lazy load or global singleton)
# To avoid reloading model on every request, we initialize once here.
bot = LLMChatbot()

@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok",
        "model_loaded": bot.model is not None,
        "version": "v1.1.0"
    }), 200

@api_bp.route('/chat', methods=['POST'])
def chat():
    start_time = time.time()
    data = request.get_json()
    
    if not data or 'message' not in data:
        return jsonify({"error": "Missing 'message' field"}), 400
        
    message = data.get('message')
    session_id = data.get('session_id', 'default_user')
    
    # Get response
    try:
        response_text = bot.get_response(message, session_id)
        
        # Get context status
        context = bot.context_manager.get_context(session_id)
        
        return jsonify({
            "response": response_text,
            "session_id": session_id,
            "context_state": context,
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_bp.route('/reset', methods=['POST'])
def reset_session():
    data = request.get_json() or {}
    session_id = data.get('session_id', 'default_user')
    
    bot.context_manager.clear_context(session_id)
    # Also clear stored data if implemented (we did implement update_data)
    if session_id in bot.context_manager.sessions:
        bot.context_manager.sessions[session_id]['data'] = {}
        
    return jsonify({"message": f"Session {session_id} cleared."}), 200

@api_bp.route('/intents', methods=['GET'])
def list_intents():
    # Return list of intent tags for frontend debug
    tags = [intent['tag'] for intent in bot.intents]
    return jsonify({"intents": tags}), 200

@api_bp.route('/history', methods=['GET'])
def get_history():
    """Fetch chat history for a given session ID."""
    session_id = request.args.get('session_id')
    if not session_id:
        return jsonify({"error": "Missing session_id parameter"}), 400
        
    try:
        # Fetch history (limit 50 for now)
        # Note: get_history returns [(sender, text, timestamp), ...] chronologically
        history = bot.db.get_history(session_id, limit=50)
        
        # Format for frontend
        formatted_history = []
        for sender, text, timestamp in history:
            formatted_history.append({
                "sender": sender,
                "text": text,
                "timestamp": timestamp
            })
            
        return jsonify({"history": formatted_history}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

