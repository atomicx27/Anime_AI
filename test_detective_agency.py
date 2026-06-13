from playwright.sync_api import sync_playwright
import os
import time

def test_detective_agency():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Connect to the local frontend HTTP server on port 8008
        page.goto("http://localhost:8008/")

        # Interact with UI
        page.fill('#mystery-input', 'Who stole the final slice of pizza from the agency fridge?')
        page.click('#solve-btn')

        # Wait for results to be visible
        page.wait_for_selector('#results-container:not(.hidden)', timeout=15000)

        # Allow animations to settle
        time.sleep(1)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/detective_agency.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_detective_agency()
