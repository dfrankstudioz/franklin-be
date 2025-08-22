# Franklin Builder’s Edition

Franklin is your local-first AI assistant — fully offline-capable, fast, and customizable.

This is the **Builder’s Edition**, designed for developers, tinkerers, and homelabbers.

---

## ✨ Features

- FastAPI backend with `/chat` endpoint
- Hybrid AI routing: OpenAI + local TinyLlama fallback
- Natural prompt → tool routing (RAG)
- React Web UI (no external calls)
- Configurable local memory folder
- Works 100% offline after setup

---

## 🧠 System Overview

```
[User] → [Web UI / API]
              ↓
         [Franklin Core]
              ↓
      [GPT-4o] + [TinyLlama]
              ↓
  [Filesystem Tools: read, list, summarize]
```

---

## 📦 Project Structure

```
franklin-be/
├── ai-middleware/      # FastAPI + RAG logic
├── docker-compose/     # Compose file and env
├── web-ui/             # React frontend (source)
├── snapshots/          # Tagged ZIP exports
└── tests/              # Test suite (API, UI, RAG)
```

---

## ✅ Tests

Use the test suite menu to run:

- API checks
- Web UI validation
- Snapshot verification
- GitHub push automation

---

## ⚠️ This version excludes secret sauce:
- Encrypted logic has been validated
- `secret_logic.py` is excluded
- All core functionality still works

---

Released: `v2025.08.22`
