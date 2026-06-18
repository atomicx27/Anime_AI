from playwright.sync_api import sync_playwright
import os
import subprocess
import time
import requests

def test_frontend():
    # Start the backend server for anime_power_scaler
    backend_dir = os.path.abspath('anime_power_scaler/backend')
    backend_process = subprocess.Popen(
        ['python3', 'main.py'],
        cwd=backend_dir,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Wait for backend to start
    for _ in range(10):
        try:
            r = requests.get('http://127.0.0.1:8006/api/characters')
            if r.status_code == 200:
                break
        except requests.ConnectionError:
            time.sleep(1)
    else:
        print("Backend failed to start")
        backend_process.terminate()
        return

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Navigate to the backend server which also serves the frontend
            page.goto("http://127.0.0.1:8006/")

            # Wait for characters to load. The previous timeout error said it found 14 options but wait_for_selector might be strict about visibility for options.
            # Let's wait for the fetch to complete
            time.sleep(2)

            # Select characters
            page.select_option('#char1-select', index=1)
            page.select_option('#char2-select', index=2)
            page.fill('#context-input', 'Test Arena')

            page.click('#simulate-btn')

            # Wait for results
            page.wait_for_selector('#results-card:not(.hidden)', timeout=15000)

            # Take screenshot
            os.makedirs('screenshots', exist_ok=True)
            screenshot_path = 'screenshots/power_scaler.png'
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

            browser.close()
    finally:
        backend_process.terminate()

if __name__ == "__main__":
    test_frontend()
