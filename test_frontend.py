from playwright.sync_api import sync_playwright
import os
import time

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Construct path to local HTML file or localhost
        # using localhost:8006 as specified in memory
        page.goto("http://localhost:8006/")

        # Wait for characters to load
        time.sleep(2)

        # Interact with UI
        page.select_option('#char1-select', index=1)
        page.select_option('#char2-select', index=2)
        page.fill('#context-input', 'Laser vision that cuts through anything')
        page.click('#simulate-btn')

        # Wait for results to be visible
        page.wait_for_selector('#results-card:not(.hidden)', timeout=15000)
        time.sleep(2)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/power_scaler.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_frontend()
