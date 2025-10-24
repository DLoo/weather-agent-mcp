# Use an official, slim Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the Python dependencies
# --no-cache-dir makes the image smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy your main application file into the container at /app
COPY main.py .

# Expose port 8000 to allow communication with the app from outside the container
EXPOSE 8000

# Define the command to run your application when the container starts.
# We use --host 0.0.0.0 to make the server accessible from outside the container.
# This will be the command that uvicorn runs.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]