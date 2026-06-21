from playwright.sync_api import sync_playwright
import os

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the local server
        page.goto("http://localhost:8007/")

        # Interact with UI
        page.fill('#mysteryInput', 'The Mayor\'s prized diamond necklace was stolen from a locked vault overnight. Only a single black feather was left behind.')
        page.click('#investigateBtn')

        # Wait for results to be visible
        page.wait_for_selector('#resultsSection', state='visible', timeout=30000)

        # Wait a moment for animations to finish
        page.wait_for_timeout(2000)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/detective_agency.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_frontend()
