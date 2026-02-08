# 🔌 API Documentation

Base URL: `http://localhost:5000/api`

## Endpoints

### 1. Chat Completion

Send a message to the bot and receive a response.

* **URL**: `/chat`
* **Method**: `POST`
* **Content-Type**: `application/json`

**Request Body:**

```json
{
  "message": "What is the weather in London?",
  "session_id": "user_12345"
}
```

**Response (200 OK):**

```json
{
  "response": "Currently in London: 15°C with wind speeds of 12 km/h.",
  "session_id": "user_12345",
  "context_state": null
}
```

**Error Response (400 Bad Request):**

```json
{
  "error": "Missing 'message' field"
}
```

---

### 2. Health Check

Verify API status and model availability.

* **URL**: `/health`
* **Method**: `GET`

**Response (200 OK):**

```json
{
  "status": "ok",
  "model_loaded": true,
  "version": "v1.0.0"
}
```

---

### 3. Reset Session

Clear conversation history and context for a user.

* **URL**: `/reset`
* **Method**: `POST`

**Request Body:**

```json
{
  "session_id": "user_12345"
}
```

**Response (200 OK):**

```json
{
  "message": "Session user_12345 cleared."
}
```

---

### 4. List Intents

Get a list of all trained intents (Debug utility).

* **URL**: `/intents`
* **Method**: `GET`
