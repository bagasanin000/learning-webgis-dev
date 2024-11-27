# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the code
COPY . .

# Run the app
CMD ["python", "app.py"]
