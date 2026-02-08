/**
 * chat.js
 * Manages the UI logic for the chat interface.
 */

import { $, escapeHTML, formatTime } from './utils.js';

export class ChatUI {
    constructor() {
        this.container = $('#messages-container');
        this.input = $('#message-input');
        this.sendBtn = $('#send-btn');
        this.emptyState = $('#empty-state');
        this.scrollBtn = $('#scroll-bottom-btn');

        this.isTyping = false;
        this.isScrolledToBottom = true;

        this._setupScrollListener();
    }

    /**
     * Add a message to the UI
     * @param {string} text - Message content
     * @param {string} sender - 'user' or 'bot'
     * @param {boolean} animate - Whether to animate entry (default true)
     */
    addMessage(text, sender, animate = true) {
        // Hide empty state if first message
        if (this.emptyState && !this.emptyState.classList.contains('hidden')) {
            this.emptyState.classList.add('hidden');
        }

        const wrapper = document.createElement('div');
        wrapper.className = `message-wrapper ${sender}`;
        if (!animate) wrapper.style.animation = 'none';
        wrapper.style.opacity = '1'; // Ensure visible if no animation

        const timestamp = formatTime();

        // Avatar logic (simplified)
        const avatarHTML = sender === 'bot'
            ? `<div class="avatar"><img src="assets/logo.svg" alt="AI"></div>`
            : ``; // User avatar hidden in this design

        // Process text (Markdown for bot, plain for user)
        let processedText = text;
        if (sender === 'bot' && window.marked) {
            try {
                processedText = window.marked.parse(text);
            } catch (e) {
                console.error('Markdown parse error:', e);
                processedText = escapeHTML(text);
            }
        } else if (sender === 'user') {
            processedText = escapeHTML(text).replace(/\n/g, '<br>');
        }

        wrapper.innerHTML = `
            ${avatarHTML}
            <div class="message-content">
                <div class="bubble prose">${processedText}</div>
                ${sender === 'bot' ? this._getActionsHTML(text) : ''}
                <div class="timestamp hidden">${timestamp}</div> 
            </div>
        `;

        this.container.appendChild(wrapper);

        // Highlight code
        if (sender === 'bot' && window.hljs) {
            wrapper.querySelectorAll('pre code').forEach((block) => {
                window.hljs.highlightElement(block);
            });
        }

        this.scrollToBottom();
    }

    /**
     * Show typing indicator
     */
    showTyping() {
        if (this.isTyping) return;
        this.isTyping = true;

        const typingEl = document.createElement('div');
        typingEl.id = 'typing-indicator';
        typingEl.className = 'message-wrapper bot';
        typingEl.innerHTML = `
            <div class="avatar"><img src="assets/logo.svg" alt="AI"></div>
            <div class="typing">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
        `;
        this.container.appendChild(typingEl);
        this.scrollToBottom();
    }

    /**
     * Hide typing indicator
     */
    hideTyping() {
        const typingEl = $('#typing-indicator');
        if (typingEl) {
            typingEl.remove();
        }
        this.isTyping = false;
    }

    /**
     * Scroll chat to bottom
     */
    scrollToBottom() {
        this.container.scrollTop = this.container.scrollHeight;
        this.isScrolledToBottom = true;
        this.scrollBtn.classList.add('hidden');
    }

    _setupScrollListener() {
        this.container.addEventListener('scroll', () => {
            const { scrollTop, scrollHeight, clientHeight } = this.container;
            const isBottom = scrollHeight - scrollTop - clientHeight < 100;

            this.isScrolledToBottom = isBottom;

            if (isBottom) {
                this.scrollBtn.classList.add('hidden');
            } else {
                this.scrollBtn.classList.remove('hidden');
            }
        });

        this.scrollBtn.addEventListener('click', () => this.scrollToBottom());
    }

    _getActionsHTML(rawText) {
        // Escape content for attribute
        const safeText = escapeHTML(rawText);
        return `
            <div class="message-actions">
                <button class="action-btn copy-btn" data-text="${safeText}" title="Copy">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                    Copy
                </button>
                <button class="action-btn regen-btn" title="Regenerate">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path><path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"></path><path d="M16 21h5v-5"></path></svg>
                </button>
            </div>
        `;
    }
}
