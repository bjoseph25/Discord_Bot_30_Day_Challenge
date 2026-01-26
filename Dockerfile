# 1. Choose a base image with Python installed
FROM python:3.11-slim

# 2. Set a working directory inside the container
WORKDIR /app

# Copy main app files
COPY main.py /app/
COPY handlers/ /app/handlers/
COPY infrastructure/ /app/infrastructure/

# Copy commands folder
COPY commands/ /app/commands/

# 3. Copy dependency list first (for caching)
COPY requirements.txt .

# 4. Install Python dependencies inside the image
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Start the Discord bot
CMD ["python", "main.py"]
