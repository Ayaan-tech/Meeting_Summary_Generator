# Use a lightweight Python base image
FROM python:3.12-slim

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libasound2-dev \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    libevdev-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables to prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy only the requirements file first to leverage Docker's caching
COPY requirements.txt /app/requirements.txt

# Set the working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the app's default port
EXPOSE 8000

# Define the command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
