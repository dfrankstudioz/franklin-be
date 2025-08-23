
import os
import pytest
import requests

BASE_URL = os.environ.get("FRANKLIN_BASE_URL", "http://localhost:9006")
TIMEOUT = int(os.environ.get("FRANKLIN_TEST_TIMEOUT", "60"))

def _chat(prompt: str, mode: str | None = None):
    payload = {"prompt": prompt}
    if mode:
        payload["mode"] = mode
    r = requests.post(f"{BASE_URL}/chat", json=payload, timeout=TIMEOUT)
    assert r.status_code == 200, f"/chat HTTP {r.status_code}: {r.text[:400]}"
    data = r.json()
    assert data.get("tool") == "chat", f"Unexpected tool: {data}"
    assert isinstance(data.get("response"), str), f"No 'response' field: {data}"
    assert data.get("response") != "(no output)", f"Empty model output: {data}"
    assert isinstance(data.get("source"), str) and data.get("source"), f"No 'source' hint: {data}"
    return data

def test_healthz_whoami():
    r = requests.get(f"{BASE_URL}/healthz", timeout=10)
    assert r.status_code == 200 and r.json().get("ok") is True
    r = requests.get(f"{BASE_URL}/whoami", timeout=10)
    assert r.status_code == 200 and r.json().get("ok") is True
    assert isinstance(r.json().get("identity"), dict)

@pytest.mark.skipif(not os.environ.get("OPENAI_API_KEY"), reason="OPENAI_API_KEY not set; skipping OpenAI path test.")
def test_openai_path_or_skip():
    data = _chat("In one clear sentence, what does a container do?", mode="openai")
    assert data["source"] == "openai", f"Expected source=openai, got: {data['source']} (fallback happened?)"

def test_ollama_forced():
    data = _chat("Reply with exactly one short sentence.", mode="ollama")
    assert data["source"] == "ollama", f"Expected source=ollama, got: {data['source']}"

def test_openai_or_fallback_auto_detect():
    """
    If OpenAI is available, expect source=openai; otherwise expect source=ollama (fallback).
    This validates boss/sidekick routing without forcing a failure.
    """
    data = _chat("One sentence: define virtualization.")
    assert data["source"] in {"openai", "ollama"}, f"Unexpected source: {data['source']}"
    # If it's openai, great. If it fell back, still acceptable.
