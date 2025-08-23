import pytest
from playwright.sync_api import sync_playwright

def test_ui_fetch_success():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:9006/ui", timeout=10000)
        page.evaluate("""() => {
            return fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt: 'hello' })
            }).then(res => res.json());
        }""")
        browser.close()