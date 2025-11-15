# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for faster caching)
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all API files
COPY app .

# Expose API port
EXPOSE 8000

# Run FastAPI using uvicorn
