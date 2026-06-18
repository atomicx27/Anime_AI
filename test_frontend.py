from playwright.sync_api import sync_playwright
import os

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Access via FastAPI static file serving (which runs on port 8006 based on earlier step)
        page.goto("http://localhost:8006/")

        # Wait for options to load
        page.wait_for_function('document.querySelectorAll("#char1-select option").length > 1', timeout=10000)

        # Interact with UI
        page.select_option('#char1-select', index=1)
        page.select_option('#char2-select', index=2)
        page.fill('#context-input', 'Final Valley')
        page.click('#simulate-btn')

        # Wait for results to be visible
        page.wait_for_selector('#results-card:not(.hidden)', timeout=15000)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/power_scaler.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_frontend()
