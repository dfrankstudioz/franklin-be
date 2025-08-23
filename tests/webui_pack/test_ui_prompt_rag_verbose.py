
import os
from playwright.sync_api import sync_playwright

def test_ui_prompt_rag_verbose():
    base = os.environ.get("FRANKLIN_UI_URL", "http://localhost:9006/ui")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=50)
        page = browser.new_page()
        page.goto(base, timeout=30000, wait_until="domcontentloaded")

        page.locator(":is(textarea,input)#prompt, [data-testid='prompt']").fill("Read file example.txt")
        page.locator(":is(button#send, button[type='submit'], button:has-text('Send'), [data-testid='send-btn'])").first.click()

        page.locator("#chat .bubble").first.wait_for(state="attached", timeout=30000)
        text = page.locator("#chat .bubble").last.inner_text()
        assert text and isinstance(text, str)
        browser.close()
