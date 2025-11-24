# Franklin BE — Builder’s Edition  
Local-first AI middleware built for developers, homelabbers, makers, and builders.

<p align="center">
  <img src="https://img.shields.io/github/v/release/dfrankstudioz/franklin-be?label=Release&color=brightgreen">
  <img src="https://img.shields.io/badge/License-Proprietary-orange">
  <img src="https://img.shields.io/github/last-commit/dfrankstudioz/franklin-be?color=yellow">
  <img src="https://img.shields.io/github/issues/dfrankstudioz/franklin-be">
  <img src="https://img.shields.io/github/stars/dfrankstudioz/franklin-be?style=social">
</p>

---

## 📌 Overview

**Franklin BE (Builder’s Edition)** is a **local-first AI middleware system** that runs entirely on your machine.  
No cloud. No uploads. No tracking.

Franklin combines:

- A **FastAPI backend**
- A lightweight **Web UI**
- Smart **tool routing** (list/read/summarize files)
- Optional **LLM fallback** (TinyLlama locally, GPT-4o if enabled)
- A **plugin-ready architecture** for future expansion

Franklin is built for people who want **full control**, **local execution**, and **a file-centric AI assistant** that works *with* their system — not against it.

---

## 🚀 Key Features

### 🔒 100% Local-First  
Your files stay on your machine. Franklin never uploads anything unless you explicitly enable GPT fallback.

### ⚙️ Smart Tool Routing  
Natural language → local tools:

- `list_dir()`
- `read_file()`
- `summarize_file()`

Franklin understands what you want and picks the right tool.

### 🧠 TinyLLama Local Model  
Runs via **Ollama**, used for:
- Local-only queries  
- On-device analysis  
- Privacy-sensitive prompts  

### 🔁 GPT-4o Optional Fallback  
If enabled, GPT-4o helps interpret complex queries and generate high-quality summaries.

### 🖥 Modern Web UI  
A fast, simple React-based UI accessible from any browser.

### 🔌 Plugin-Ready  
Extend Franklin with future plugins:
- System monitoring  
- Git helpers  
- Automation tools  
- LifeOS/Notebook extensions  

### 🐳 Docker-Powered  
Install and run with a single command.

---

## ⚡ Quick Start (TL;DR)

```bash
git clone https://github.com/dfrankstudioz/franklin-be.git
cd franklin-be
docker compose up -d
```

Then open:

```
http://localhost:8000
```

That’s it — Franklin is running locally.

---

## 📘 Documentation

Full documentation and legal pages are hosted on GitHub Pages:

👉 **https://dfrankstudioz.github.io/franklin-be/**

Includes:

- Getting Started  
- Tools & Commands  
- Local-Only Mode  
- Settings & Fallback  
- Updating & Maintenance  
- EULA / Terms / Privacy / Refund Policy  

---

## 🧱 Architecture Overview (Text Only)

Franklin BE is built using a clean modular architecture:

```
┌──────────────────────────────┐
│         Web UI (React)       │
└──────────────┬───────────────┘
               │ HTTP (Chat API)
┌──────────────▼───────────────┐
│     FastAPI Backend (BE)     │
│  - Tool Router               │
│  - TinyLlama Fallback        │
│  - GPT-4o Fallback (opt)     │
└──────────────┬───────────────┘
               │ Local Tools
       ┌───────┴────────┬────────┐
       │                │         │
 list_dir()      read_file()   summarize_file()
```

---

## ❓ Why Franklin BE?

Because most AI tools are:
- Cloud-locked  
- Privacy-invasive  
- Overly complex  
- Unable to interact with your actual system  

Franklin is the opposite:

- 🏠 **Runs locally**
- 🔒 **Zero data leaves your machine**
- 📂 **Understands your files**
- 🧩 **Extendable via plugins**
- 🧱 **Simple Docker deployment**
- ⚡ **Fast and lightweight**

---

## 🗺 Roadmap

Franklin BE is actively evolving. Planned features include:

- Plugin marketplace  
- On-device planning agents  
- Model switching UI  
- System Monitoring plugin  
- LifeOS module  
- NOC Dashboard  
- Unified settings  
- More local tools  

---

## 🔑 Licensing

Franklin BE — Builder’s Edition is **proprietary software**.

Full EULA:  
👉 https://dfrankstudioz.github.io/franklin-be/#/licence

---

## 💬 Support  

Email: **support@dfrankstudioz.com**  
Issues: https://github.com/dfrankstudioz/franklin-be/issues  

---

## ⭐ Enjoying Franklin?

Give the project a **star** — it helps visibility and growth!
