
let sessionId = localStorage.getItem('chat_session_id');
if (!sessionId) {
    sessionId = 'user_' + Math.random().toString(36).substr(2, 9);
    localStorage.setItem('chat_session_id', sessionId);
}

const API_URL = 'http://localhost:5000/api';

const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const resetBtn = document.getElementById('reset-btn');
const typingIndicator = document.getElementById('typing-indicator');


sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
resetBtn.addEventListener('click', resetSession);

async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;


    addMessage(message, 'user');
    userInput.value = '';
    userInput.focus();


    showTyping(true);

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            })
        });

        const data = await response.json();


        showTyping(false);

        if (response.ok) {
            addMessage(data.response, 'bot');

        } else {
            addMessage('Error: ' + (data.error || 'Server error'), 'bot');
        }

    } catch (error) {
        showTyping(false);
        addMessage('Network error. Is the server running?', 'bot');
        console.error('Error:', error);
    }
}

async function resetSession() {
    try {
        await fetch(`${API_URL}/reset`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ session_id: sessionId })
        });


        chatMessages.innerHTML = `
            <div class="message bot-message">
                <div class="avatar">AI</div>
                <div class="bubble">Conversation reset. Anything else?</div>
            </div>
        `;
    } catch (error) {
        console.error('Reset error:', error);
    }
}

function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');

    const avatar = sender === 'user' ? 'You' : 'AI';

    messageDiv.innerHTML = `
        <div class="avatar">${avatar}</div>
        <div class="bubble">${escapeHtml(text)}</div>
    `;

    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function showTyping(show) {
    if (show) {
        chatMessages.appendChild(typingIndicator);
        typingIndicator.style.display = 'flex';
    } else {
        typingIndicator.style.display = 'none';

    }
    scrollToBottom();
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
