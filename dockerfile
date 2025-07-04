# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your code to the container
COPY . .

# Expose the port uvicorn will run on
EXPOSE 8080

# Start the FastAPI app when the container starts
CMD ["uvicorn", "fastapi_gptneo:app", "--host", "0.0.0.0", "--port", "8080"]
