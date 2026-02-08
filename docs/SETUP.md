# 🛠️ Setup Guide

## System Requirements

- Python 3.9+
- Git
- Docker (optional, for containerization)

## Manual Installation (Local)

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/ai-chatbot.git
    cd ai-chatbot
    ```

2. **Create Virtual Environment**

    ```bash
    python -m venv venv
    
    # Windows
    venv\Scripts\activate
    
    # Mac/Linux
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLP Data**

    ```bash
    python -m nltk.downloader punkt stopwords wordnet
    ```

5. **Train the Model**

    ```bash
    python src/chatbot/train_model.py
    ```

6. **Run the Server**

    ```bash
    python api/app.py
    ```

    Server will start at `http://localhost:5000`.

## Docker Installation

1. **Build Image**

    ```bash
    docker build -t ai-chatbot .
    ```

2. **Run Container**

    ```bash
    docker run -p 5000:5000 ai-chatbot
    ```

## Post-Setup

Once running, open `frontend/index.html` in your web browser to start chatting.
