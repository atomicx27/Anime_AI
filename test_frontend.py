from playwright.sync_api import sync_playwright
import os

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # The instructions say: When testing frontend user journeys with Playwright, navigate the browser to the local HTTP server
        # (e.g., http://localhost:<port>) instead of using local file:// paths to prevent CORS and relative API route resolution errors.
        page.goto('http://localhost:8006/')

        # Interact with UI for anime_power_scaler
        # Assuming the button is simulate-btn and there is an input like opponent-input or context-input
        page.fill('#context-input', 'Tournament of Power')
        page.click('#simulate-btn')

        # Wait for results to be visible
        # It's better to wait for the terminal or log entries
        page.wait_for_selector('.log-entry', timeout=15000)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/power_scaler.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_frontend()
