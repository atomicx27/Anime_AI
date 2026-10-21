from playwright.sync_api import sync_playwright
import time

def test_courtroom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8007/")

        page.fill("#crimeInput", "Eating the last slice of pizza")
        page.click("#submitBtn")

        # Wait for the transcript to appear
        page.wait_for_selector("#transcript div.message-card", timeout=10000)

        # Give it a few seconds for all animations to finish
        time.sleep(5)

        page.screenshot(path="screenshots/courtroom_test.png", full_page=True)
        browser.close()

if __name__ == "__main__":
    test_courtroom()
