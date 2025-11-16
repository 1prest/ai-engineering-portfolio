FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all API files from app/ into /app
COPY app/ .

# Expose API port
EXPOSE 8000

# Run API
CMD ["python", "api.py"]
