/**
 * app.js
 * Main entry point for the application. Initializes components and event listeners.
 */

import { $, $$, storage } from './utils.js';
import { API } from './api.js';
import { ChatUI } from './chat.js';

class App {
    constructor() {
        this.api = new API();
        this.ui = new ChatUI();

        this.init();
    }

    init() {
        this._setupEventListeners();
        this._setupTheme();
        this._setupMobileSidebar();

        // Auto-focus input
        if (window.innerWidth > 768) {
            $('#message-input').focus();
        }

        this.loadHistory();
    }

    async loadHistory() {
        // Show small loader or just wait
        const data = await this.api.getHistory();
        if (data.history && data.history.length > 0) {
            // Clear empty state if history exists
            this.ui.emptyState.classList.add('hidden');

            data.history.forEach(msg => {
                // Msg: {sender, text, timestamp}
                this.ui.addMessage(msg.text, msg.sender, false); // false = no animate
            });
            this.ui.scrollToBottom();
        }
    }

    _setupEventListeners() {
        // Input Handling
        const input = $('#message-input');
        const sendBtn = $('#send-btn');
        const newChatBtn = $('#new-chat-btn');

        // Auto-resize textarea
        input.addEventListener('input', () => {
            input.style.height = 'auto'; // Reset
            input.style.height = input.scrollHeight + 'px';

            // Enable/Disable send button
            if (input.value.trim().length > 0) {
                sendBtn.removeAttribute('disabled');
            } else {
                sendBtn.setAttribute('disabled', 'true');
            }
        });

        // Enter to send, Shift+Enter for new line
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.handleSendMessage();
            }
        });

        sendBtn.addEventListener('click', () => this.handleSendMessage());

        // Quick Prompts
        $$('.prompt-chip').forEach(chip => {
            chip.addEventListener('click', () => {
                const prompt = chip.dataset.prompt;
                this.ui.input.value = prompt;
                this.ui.input.dispatchEvent(new Event('input')); // Trigger resize/enable
                this.handleSendMessage(); // Auto send? Yes
            });
        });

        // Copy Button Delegation
        $('#messages-container').addEventListener('click', (e) => {
            const btn = e.target.closest('.copy-btn');
            if (btn) {
                const text = btn.dataset.text;
                navigator.clipboard.writeText(text).then(() => {
                    const originalHTML = btn.innerHTML;
                    btn.innerHTML = '<span>Copied!</span>';
                    setTimeout(() => btn.innerHTML = originalHTML, 2000);
                });
            }

            // Regenerate logic (placeholder for now)
            const regenBtn = e.target.closest('.regen-btn');
            if (regenBtn) {
                // To implement, we needs last user message.
                // For now, simpler to just re-send last inputs or similar.
                alert('Regenerate feature coming soon!');
            }
        });

        // New Chat
        if (newChatBtn) {
            newChatBtn.addEventListener('click', async () => {
                if (confirm('Start a new chat? This will clear current view.')) {
                    // Generate new session
                    this.api.sessionId = 'user-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
                    localStorage.setItem('chat_session_id', this.api.sessionId);

                    // Clear UI
                    $('#messages-container').innerHTML = '';
                    this.ui.emptyState.classList.remove('hidden');
                    $('#messages-container').appendChild(this.ui.emptyState);
                }
            });
        }
    }

    async handleSendMessage() {
        const input = $('#message-input');
        const message = input.value.trim();

        if (!message) return;

        // Reset input
        input.value = '';
        input.style.height = 'auto';
        $('#send-btn').setAttribute('disabled', 'true');

        // Add User Message
        this.ui.addMessage(message, 'user');

        // Show Loading
        this.ui.showTyping();

        try {
            // API Call
            const data = await this.api.sendMessage(message);

            // Remove Loading
            this.ui.hideTyping();

            // Add Bot Message
            if (data.response) {
                this.ui.addMessage(data.response, 'bot');
            } else {
                this.ui.addMessage("I'm sorry, I received an empty response.", 'bot');
            }
        } catch (error) {
            this.ui.hideTyping();
            this.ui.addMessage(`⚠️ **Error:** ${error.message}. Please check if the backend is running.`, 'bot');
        }
    }

    _setupTheme() {
        const toggleBtn = $('#theme-toggle');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

        // Load saved or default
        const savedTheme = storage.get('theme', prefersDark ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme', savedTheme);

        toggleBtn.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');
            const newTheme = current === 'dark' ? 'light' : 'dark';

            document.documentElement.setAttribute('data-theme', newTheme);
            storage.set('theme', newTheme);
        });
    }

    _setupMobileSidebar() {
        const sidebar = $('#sidebar');
        const menuBtn = $('#mobile-menu-btn');
        const closeBtn = $('#close-sidebar');

        // Create Overlay
        const overlay = document.createElement('div');
        overlay.className = 'overlay';
        sidebar.after(overlay);

        const open = () => {
            sidebar.classList.add('open');
            // Overlay logic can be css only if adjacent, effectively handled in responsive.css
            // But we need to handle clicks
            overlay.style.pointerEvents = 'auto';
        };

        const close = () => {
            sidebar.classList.remove('open');
            overlay.style.pointerEvents = 'none';
        };

        menuBtn.addEventListener('click', open);
        closeBtn.addEventListener('click', close);
        overlay.addEventListener('click', close);
    }
}

// Start App
document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});
