import pytest
from playwright.sync_api import sync_playwright

def test_ui_load_and_elements():
    """Check UI loads and core elements are present"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:9006/ui", timeout=15000)
        
        # Dump HTML for debugging
        print("\n[DEBUG] Page content:\n", page.content())
        
        # Check main input exists
        assert page.query_selector("#prompt") is not None
        assert page.query_selector("button") is not None
        
        browser.close()
