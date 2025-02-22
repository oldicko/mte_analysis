# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5001

# Set the command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]