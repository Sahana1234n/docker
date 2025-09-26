# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the current directory contents into container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

#Define environment variable
ENV FLASK_APP = app.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]


