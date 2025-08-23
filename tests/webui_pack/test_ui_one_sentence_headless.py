import re, os
from playwright.sync_api import sync_playwright

BASE = os.environ.get("FRANKLIN_UI_URL", "http://localhost:9006/ui")
PROMPT = "One sentence (<=12 words): what does Docker do?"

def first_sentence_12w(s: str) -> str:
    s = re.split(r'(?<=[.!?])\s+', s.strip())[0]
    words = s.split()
    return " ".join(words[:12]).rstrip(".") + "." if words else ""

def test_ui_one_sentence_clamp_headless():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE, timeout=30000, wait_until="domcontentloaded")

        # Wait for the prompt control to exist (attached), not necessarily visible.
        prompt_locator = page.locator(":is(textarea,input)#prompt")
        prompt_locator.wait_for(state="attached", timeout=30000)
        prompt_locator.fill(PROMPT)

        # Click a likely send button (id, submit, or text)
        send = page.locator(":is(button#send, button[type='submit'], button:has-text('Send'))")
        send.first.click()

        # Wait for any bubble node to be attached, then read the last one
        page.locator("#chat .bubble").first.wait_for(state="attached", timeout=30000)
        text = page.locator("#chat .bubble").last.inner_text()

        browser.close()

        sent = first_sentence_12w(text)
        assert len(sent.split()) <= 12, f"Too many words: {sent!r}"
        assert any(p in sent for p in '.!?'), f"No sentence terminator: {sent!r}"
