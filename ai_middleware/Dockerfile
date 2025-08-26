FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set working directory
WORKDIR /app

# Copy app code
COPY . /app

# Install dependencies (runtime + dev/test tools)
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir openai requests pytest
ENV PYTHONPATH=/app
ENV PYTHONPATH=/app
