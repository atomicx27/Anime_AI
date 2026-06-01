from playwright.sync_api import sync_playwright
import os

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Construct path to local HTML file
        filepath = f"file://{os.path.abspath('anime_power_scaler/frontend/index.html')}"
        page.goto(filepath)

        # Interact with UI
        page.fill('#ability-input', 'Laser vision that cuts through anything')
        page.click('#scale-btn')

        # Wait for results to be visible
        page.wait_for_selector('#results-container:not(.hidden)', timeout=10000)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/power_scaler.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_frontend()
