
import pytest
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def test_webui_rag_prompt():
    prompt = "List files in /memory"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:5173")

        # Type the prompt and submit
        page.fill("textarea", prompt)
        page.keyboard.press("Enter")

        try:
            # Wait for response to appear
            page.wait_for_selector('div:has-text("AI:")', timeout=15000)
            response = page.inner_text('div:has-text("AI:")')
            print("\n--- AI Response ---\n", response)

            assert "Unable to summarize" not in response
            assert "Fallback" not in response
            assert "TinyLlama" not in response

        except PlaywrightTimeoutError:
            print("\n[❌] AI response did not appear in time.")
            print("Page content for debugging:\n")
            print(page.content())
            raise AssertionError("AI response did not appear on the page.")

        finally:
            browser.close()
