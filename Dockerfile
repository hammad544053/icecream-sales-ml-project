# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirement files first (helps with Docker build caching)
COPY requirements.txt .

# Install dependencies without keeping cached wheels
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Hugging Face Spaces expects port 7860
EXPOSE 7860

# Run the app using production-ready Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]