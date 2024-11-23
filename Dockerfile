# Use an official Python image as a base
FROM python:3.10-slim

# Set environment variables to prevent Python from buffering output
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1


# Copy only the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .


WORKDIR /app
# Command to run the FastAPI application
CMD ["python3", "main.py"]