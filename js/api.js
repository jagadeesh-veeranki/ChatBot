/**
 * api.js
 * Handles all network requests to the backend API.
 */

// For local development: http://127.0.0.1:5000/api
// For production: Replace with your deployed backend URL (e.g., Render/Railway)
const API_BASE_URL = 'http://127.0.0.1:5000/api';

export class API {
    constructor() {
        this.sessionId = this._initSession();
    }

    _initSession() {
        let sid = localStorage.getItem('chat_session_id');
        if (!sid) {
            sid = 'user-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
            localStorage.setItem('chat_session_id', sid);
        }
        return sid;
    }

    /**
     * Send message to chatbot
     * @param {string} message 
     * @returns {Promise<Object>}
     */
    async sendMessage(message) {
        try {
            const response = await fetch(`${API_BASE_URL}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    session_id: this.sessionId
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `Server Error: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    /**
     * Get chat history
     * @returns {Promise<Object>}
     */
    async getHistory() {
        try {
            const response = await fetch(`${API_BASE_URL}/history?session_id=${this.sessionId}`);
            if (!response.ok) {
                // If 404 or other, just return empty
                return { history: [] };
            }
            return await response.json();
        } catch (error) {
            console.warn('Failed to fetch history:', error);
            return { history: [] };
        }
    }

    /**
     * Reset the conversation history on server
     */
    async resetConversation() {
        try {
            await fetch(`${API_BASE_URL}/reset`, { // Assuming reset endpoint exists or creating session logic
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ session_id: this.sessionId })
            });
            // Update session ID just in case
            this.sessionId = 'user-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
            localStorage.setItem('chat_session_id', this.sessionId);
        } catch (error) {
            console.warn('Reset failed:', error);
        }
    }
}
