# Use a base image with Python 3.12
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (including Xvfb)

RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    gcc \
    g++ \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Set the DISPLAY environment variable for Xvfb
ENV DISPLAY=:0

# Expose the port your app runs on (default is 8000 for uvicorn)
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "Xvfb :0 & uvicorn app:app --host 0.0.0.0 --port 8000"]
