from playwright.sync_api import sync_playwright
import os
import time

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Connect to local frontend server
        page.goto('http://localhost:8080')

        # Interact with UI
        page.fill('#mystery-input', 'Someone stole the forbidden scrolls from the Hokage\'s office, leaving behind only a trace of black ash...')
        page.click('#investigate-btn')

        # Wait for results to be visible
        page.wait_for_selector('#results-container:not(.hidden)', timeout=15000)

        # Allow some time for animations to settle
        time.sleep(1)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/detective_agency.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_frontend()
