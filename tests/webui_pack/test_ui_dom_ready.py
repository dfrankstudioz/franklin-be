import pytest
from playwright.sync_api import sync_playwright

def test_ui_dom_ready():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:9006/ui", timeout=10000)
        page.wait_for_selector("div.bubble", timeout=30000)
        html = page.content()
        assert "AI:" in html or "Chat" in html
        browser.close()