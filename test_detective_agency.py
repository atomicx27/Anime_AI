from playwright.sync_api import sync_playwright
import os
import time

def test_detective_agency():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the local FastAPI server
        page.goto('http://localhost:8007/')

        # Wait for the UI to be ready
        page.wait_for_selector('#mystery-input')

        # Interact with UI
        page.fill('#mystery-input', 'Someone stole the Hokage\'s hat from the heavily guarded vault!')
        page.click('#investigate-btn')

        # Wait for the results to load
        page.wait_for_selector('#results-container:not(.hidden)', timeout=10000)

        # Give it a small delay to render
        time.sleep(1)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/detective_agency.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_detective_agency()
