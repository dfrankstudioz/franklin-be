# Franklin Builder’s Edition

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Release](https://img.shields.io/github/v/release/dfrankstudioz/franklin-be)](https://github.com/dfrankstudioz/franklin-be/releases)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](#installation)

Franklin is a **self-hosted, hybrid AI assistant** designed for privacy-first workflows.  
The **Builder’s Edition (BE)** is a slimmed-down public snapshot for developers, homelabbers, and open-source contributors.  

---

## ✨ Features

- ✅ API and Web UI fully functional  
- ✅ Natural prompt routing  
- ✅ Local tools: `list_dir`, `read_file`, `summarize_file`  
- ✅ Fallback LLM via TinyLlama (Ollama)  
- ✅ GPT-4o prompt interpretation (OpenAI optional)  
- ✅ 60+ passing tests (API, RAG, Web UI, fallback, system)  

---

## 🚀 Quick Start

```bash
git clone https://github.com/dfrankstudioz/franklin-be.git
cd franklin-be/docker-compose
docker compose up -d --build
```

Visit the Web UI: [http://localhost:9006/ui](http://localhost:9006/ui)

---

## 🛠 Usage Examples

Prompt in Web UI or via API:

```bash
curl -s -X POST http://localhost:9006/chat   -H "Content-Type: application/json"   -d '{"prompt":"list_dir(\"/memory\")"}'
```

Or natural language:

```bash
"Summarize the contents of memory.txt"
```

---

## 📦 Installation & Configuration
See [INSTALL.md](INSTALL.md) for full details.  
Check [RELEASE_NOTES.md](RELEASE_NOTES.md) for changes.

---

## 📜 Roadmap
See [ROADMAP.md](ROADMAP.md) (coming soon).

---

## 🤝 Contributing
We welcome contributions from tinkerers, testers, and builders.  
See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License
Released under the [MIT License](LICENSE.md).  
Certain proprietary logic is shipped in encrypted form.
