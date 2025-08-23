import time
from playwright.sync_api import sync_playwright

def test_web_ui_prompt_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:9006/ui")
        
        page.fill("input", "list files in /memory")
        page.click("text=Send")
        
        page.wait_for_timeout(3000)
        response_text = page.text_content("body")
        
        assert "AI:" in response_text or "Franklin" in response_text
        browser.close()
