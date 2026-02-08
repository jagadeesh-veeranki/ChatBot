from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import time
import os
import nltk

# Configure NLTK data path
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
if os.path.exists(nltk_data_path):
    nltk.data.path.append(nltk_data_path)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    CORS(app)


    from routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    def index():
        return jsonify({"message": "AI Chatbot API is running. use /api/chat"})


    @app.errorhandler(Exception)
    def handle_exception(e):
        logger.error(f"Unhandled Exception: {str(e)}", exc_info=True)
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

    @app.errorhandler(404)
    def handle_not_found(e):
        return jsonify({"error": "Resource not found"}), 404
        
    @app.errorhandler(400)
    def handle_bad_request(e):
        return jsonify({"error": "Bad Request"}), 400

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
