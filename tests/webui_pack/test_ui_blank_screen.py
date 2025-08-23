import pytest
from playwright.sync_api import sync_playwright

def test_ui_blank_screen():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:9006/ui", timeout=10000)
        body_content = page.inner_html("body")
        assert body_content.strip() != "", "Blank screen detected — body is empty"
        browser.close()