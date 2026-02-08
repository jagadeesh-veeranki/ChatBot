from flask import request, jsonify
import time

# Very simple in-memory rate limiter
# { ip_address: [timestamp1, timestamp2, ...] }
request_history = {}
RATE_LIMIT = 5  # requests per second
WINDOW = 1.0    # seconds

def rate_limit_check():
    """
    Check if IP has exceeded request limit within the window.
    This can be used as a decorator or checking logic.
    For simplicity in Phase 5, we are not integrating a robust middleware,
    but user asked for middleware file. 
    """
    ip = request.remote_addr
    now = time.time()
    
    if ip not in request_history:
        request_history[ip] = []
        
    # Filter out old requests
    request_history[ip] = [ts for ts in request_history[ip] if now - ts < WINDOW]
    
    if len(request_history[ip]) >= RATE_LIMIT:
        return True # Limited
        
    request_history[ip].append(now)
    return False

# In a real app, we'd wrap this as a decorator or register before_request in app.py
# For now, just providing the logic as requested.
