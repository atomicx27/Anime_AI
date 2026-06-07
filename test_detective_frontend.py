from playwright.sync_api import sync_playwright
import os

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Connect to local HTTP server
        page.goto('http://localhost:8007')

        # Interact with UI
        page.fill('#case-input', 'The mysterious disappearance of the legendary ramen recipe from Ichiraku Ramen.')
        page.click('#investigate-btn')

        # Wait for results to be visible
        page.wait_for_selector('#results-section:not(.hidden)', timeout=15000)
        page.wait_for_selector('#task-force-grid > div', timeout=15000)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/detective_agency.png'
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_frontend()
