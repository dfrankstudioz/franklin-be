# Installation Instructions

## Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for optional testing)
- OpenAI API Key (optional, for hybrid mode)

---

## Quick Start

```bash
git clone https://github.com/dfrankstudioz/franklin-be.git
cd franklin-be/docker-compose
docker compose up -d --build
```

Access the Web UI: [http://localhost:9006/ui](http://localhost:9006/ui)

---

## Environment Variables
Create a `.env` file in `docker-compose/` or copy from the template:

```bash
cp docker-compose/.env.example docker-compose/.env
```

Example values:

```env
# OpenAI API key (optional if you only want local TinyLlama)
OPENAI_API_KEY=sk-xxxx
```

---

## Verify Install
```bash
curl -s -X POST http://localhost:9006/chat   -H "Content-Type: application/json"   -d '{"prompt":"list_dir(\"/memory\")"}'
```

---

## Common Issues
- **Port already in use** → Stop other services using 9006 or change in `docker-compose.yml`.
- **API key missing** → Franklin works in local-only mode without OpenAI, but hybrid features require a key.
- **Docker errors** → Ensure Docker Desktop/Engine is running and up-to-date.
