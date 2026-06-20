from playwright.sync_api import sync_playwright
import os

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the local server hosting the frontend
        page.goto("http://localhost:8010/")

        # Interact with UI
        page.fill('#pitch-input', 'A revolutionary teleportation network using advanced chakra relay stations, completely eliminating global shipping costs and reducing carbon emissions to zero.')
        page.click('#pitch-btn')

        # Wait for results to be visible
        page.wait_for_selector('#results-container:not(.hidden)', timeout=15000)

        # Wait a moment for animations to finish
        page.wait_for_timeout(2000)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/startup_pitch.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_frontend()
