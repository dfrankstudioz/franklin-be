import re, requests

def first_sentence_12w(s: str) -> str:
    s = re.split(r'(?<=[.!?])\s+', s.strip())[0]
    words = s.split()
    return " ".join(words[:12]).rstrip(".") + "." if words else ""

def test_one_sentence_clamp():
    r = requests.post("http://localhost:9006/chat", json={"prompt": "One sentence (<=12 words): what does Docker do?"}, timeout=20)
    r.raise_for_status()
    txt = first_sentence_12w(r.json().get("response",""))
    assert len(txt.split()) <= 12
    assert any(p in txt for p in ".!?")
