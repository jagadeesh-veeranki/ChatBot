# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=api/app.py
ENV PORT=5000

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy project source code
COPY . .

# Run NLTK download (forpunkt/stopwords if necessary)
# Or rely on code doing it, but pre-downloading in image is safer.
RUN python -m nltk.downloader punkt stopwords

# Expose port from container
EXPOSE 5000

# Use Gunicorn as production server
CMD ["gunicorn", "--config", "gunicorn_config.py", "api.app:create_app()"]
