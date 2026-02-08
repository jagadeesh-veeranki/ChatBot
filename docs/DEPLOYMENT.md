# Deployment Guide

## 🐳 Docker Deployment (Recommended)

### Prerequisites

- Docker installed
- Docker Compose installed

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/ai-chatbot.git
    cd ai-chatbot
    ```

2. **Configure Environment**:
    Copy the example env file:

    ```bash
    cp .env.example .env
    # Edit .env with your secrets if needed
    ```

3. **Build and Run**:

    ```bash
    docker-compose up --build -d
    ```

4. **Verify**:
    Check if the API is running at `http://localhost:5000/api/health`.

---

## ☁️ Cloud Deployment (Heroku/Render)

### Using Docker on Render

1. Connect your GitHub repository to Render.
2. Select "Web Service".
3. Choose "Docker" as the Environment.
4. Render will automatically detect the `Dockerfile` and build it.
5. Add environment variables in the Render dashboard.

### Using Python Runtime on Heroku

1. Create a `Procfile` (already configured via Gunicorn command, but explicit file helps):

    ```
    web: gunicorn --config gunicorn_config.py api.app:create_app()
    ```

2. Push to Heroku:

    ```bash
    heroku create
    git push heroku main
    ```

---

## 🔄 CI/CD Pipeline

The project includes a GitHub Actions workflow `.github/workflows/ci.yml` that automatically:

- Lints code with `flake8`.
- Runs unit and integration tests with `pytest`.

To enable CD (Continuous Deployment), you can add a step to the workflow to push the Docker image to Docker Hub or trigger a deployment hook on Render/Heroku.
