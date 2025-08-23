import os, requests

BASE = os.environ.get("FRANKLIN_BASE", "http://localhost:9006")

def test_whoami():
    r = requests.get(f"{BASE}/whoami", timeout=10)
    assert r.status_code == 200
    j = r.json()
    assert j.get("ok") is True
    ident = j.get("identity", {})
    assert ident.get("name") == "Franklin"
    assert "privacy-first" in (ident.get("description","") + ident.get("role","")).lower()

def test_identity_in_chat():
    payload = {"prompt": "Who are you?"}
    r = requests.post(f"{BASE}/chat", json=payload, timeout=15)
    assert r.status_code == 200
    j = r.json()
    assert "Franklin" in j.get("response","")
