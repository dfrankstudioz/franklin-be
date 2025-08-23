FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir openai requests pytest
