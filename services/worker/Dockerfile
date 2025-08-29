FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

CMD ["celery", "-A", "main.celery_app", "worker", "--loglevel=info"]