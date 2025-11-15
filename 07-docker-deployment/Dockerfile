# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements first
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all API files
COPY app/ .

# Expose API port
EXPOSE 8000

# Run the API
CMD ["python", "api.py"]
