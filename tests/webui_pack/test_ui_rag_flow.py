
import pytest
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def test_webui_rag_prompt():
    prompt = "List files in /memory"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:5174")
        print("\n[🧪] Page loaded, dumping HTML...")
        print(page.content())

        # Type the prompt and submit
        page.fill("#prompt", prompt)
        page.click("button:has-text(\"Send\")")
        page.keyboard.press("Enter")

        try:
            # Wait for response to appear
            page.wait_for_selector('div.bubble', timeout=15000)
            response = page.inner_text('div.bubble')
            print("\n--- AI Response ---\n", response)

            assert "Unable to summarize" not in response
            assert "Fallback" not in response

        except PlaywrightTimeoutError:
            print("\n[❌] AI response did not appear in time.")
            print("Page content for debugging:\n")
            print(page.content())
            raise AssertionError("AI response did not appear on the page.")

        finally:
            browser.close()
