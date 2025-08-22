# 🚀 Installing Franklin Builder’s Edition

## Prerequisites

- Docker + Docker Compose
- Python 3.11+ (for tests)
- Node.js (for rebuilding UI, optional)
- OpenAI API key (for hybrid mode)

---

## 1. Clone the Repository

```bash
git clone https://github.com/dfrankstudioz/franklin-be.git
cd franklin-be
```

---

## 2. Set Environment Variables

Edit `.env` inside `docker-compose/`:

```
OPENAI_API_KEY=your-key-here
```

---

## 3. Build and Launch

```bash
cd docker-compose
docker compose up -d --build
```

---

## 4. Access Franklin

- Web UI: [http://localhost:9006/ui](http://localhost:9006/ui)
- API: `POST /chat` with `{ "prompt": "your query" }`

---

## 5. Run Tests

```bash
cd ..
./run_tests_menu.sh
```

Use option 7 to run full validation and push to GitHub.
