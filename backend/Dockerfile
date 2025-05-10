FROM python:3.10-slim

WORKDIR /app

# Install system packages needed for git and any other build tools
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app
COPY alembic.ini .
COPY alembic ./alembic

# Expose port
EXPOSE 8000

# Start server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
