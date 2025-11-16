FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Copy only requirements first (for cache)
COPY app/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the app
COPY app /app

# Expose API port
EXPOSE 8000

# Run API
CMD ["python", "api.py"]
