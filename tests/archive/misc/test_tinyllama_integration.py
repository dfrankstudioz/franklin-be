
import os
import json
import pytest
import requests

BASE_URL = os.environ.get("FRANKLIN_BASE_URL", "http://localhost:9006")

def _post_chat(prompt: str, mode: str = None):
    payload = {"prompt": prompt}
    if mode:
        payload["mode"] = mode
    r = requests.post(f"{BASE_URL}/chat", json=payload, timeout=60)
    assert r.status_code == 200, f"/chat HTTP {r.status_code}: {r.text[:500]}"
    data = r.json()
    assert isinstance(data, dict), "Response is not JSON object"
    assert data.get("tool") == "chat", f"Unexpected tool: {data}"
    assert isinstance(data.get("source"), str) and data.get("source"), "Missing source"
    assert isinstance(data.get("response"), str), "Missing response field"
    return data

def test_health_and_identity():
    r = requests.get(f"{BASE_URL}/healthz", timeout=10)
    assert r.status_code == 200
    assert r.json().get("ok") is True

    r = requests.get(f"{BASE_URL}/whoami", timeout=10)
    assert r.status_code == 200
    j = r.json()
    assert j.get("ok") is True
    assert isinstance(j.get("identity"), dict)

def test_tinyllama_chat_basic_follow():
    data = _post_chat("Tell me a very short joke. Keep it under 15 words.", mode="ollama")
    words = data["response"].split()
    assert len(words) <= 20, f"Response too long: {len(words)} words. Full: {data['response']!r}"
    assert any(ch in data["response"] for ch in ".!?"), f"Not sentence-like: {data['response']!r}"

@pytest.mark.parametrize("prompt", [
    "Reply with exactly one short sentence.",
    "Answer in one sentence only."
])
def test_tinyllama_consistency(prompt):
    data = _post_chat(prompt, mode="ollama")
    assert any(ch in data["response"] for ch in ".!?"), f"Not sentence-like: {data['response']!r}"
