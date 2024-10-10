# Use the official Python image (Debian-based) as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Update the package list and install Node.js and Flask
RUN apt-get update && apt-get install -y nodejs && pip install Flask

# Command to run the Flask app
CMD ["python", "app.py"]
