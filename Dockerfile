# Use an official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
