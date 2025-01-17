# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy the entire app directory
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Use main:app since main.py is directly under /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
