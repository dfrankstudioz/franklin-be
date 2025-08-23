import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

import os, requests, re

BASE = os.environ.get("FRANKLIN_BASE_URL", "http://localhost:9006")

def test_rag_smoke_list_dir():
    # Natural language that should route to list_dir in your middleware (if implemented)
    r = requests.post(f"{BASE}/chat", json={"prompt": "List files in /"}, timeout=20)
    assert r.status_code == 200
    data = r.json()
    assert "response" in data
    # Don't enforce contents; just ensure we didn't fall back to marketing soup
    assert len(data["response"]) > 0

def test_rag_smoke_read_and_summarize_graceful():
    # If your RAG impl supports it, this should try to read; otherwise it should error nicely.
    r = requests.post(f"{BASE}/chat", json={"prompt": "Read file /etc/hostname"}, timeout=20)
    assert r.status_code == 200
    data = r.json()
    assert "response" in data
    # Summarize flow (may be a stub in your current code); just ensure JSON shape is OK
    r2 = requests.post(f"{BASE}/chat", json={"prompt": "Summarize file /etc/hostname"}, timeout=20)
    assert r2.status_code == 200
    data2 = r2.json()
    assert "response" in data2
