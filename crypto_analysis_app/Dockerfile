# Stage 1: Build the Python application
FROM python:3.8-slim as builder

# Set up the working directory
WORKDIR /app

# Copy the Python dependencies file
COPY requirements.txt /app/requirements.txt

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        libffi-dev \
        libssl-dev \
        && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY script.py /app/script.py

# Run the Python script to generate the index.html file
RUN python /app/script.py

# Stage 2: Set up Nginx to serve the content
FROM nginx:latest

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the generated index.html from the builder stage
COPY --from=builder /app/index.html /usr/share/nginx/html/index.html

# Set up cron job in the Nginx container to run the Python script every 15 minutes
# Note: dcron is not available in the nginx:alpine image, so we use crontabs
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*
RUN echo "*/15 * * * * python /usr/share/nginx/html/script.py >> /var/log/cron.log 2>&1" > /etc/cron.d/script-cron
RUN chmod 0644 /etc/cron.d/script-cron
RUN crontab /etc/cron.d/script-cron

# Copy the Python script into the Nginx container for the cron job
COPY --from=builder /app/script.py /usr/share/nginx/html/script.py

# Expose port 80 for Nginx
EXPOSE 8081

# Start cron and Nginx
CMD cron && nginx -g 'daemon off;'

