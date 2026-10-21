from playwright.sync_api import sync_playwright
import os

def test_group_chat_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Construct path to local HTML file
        filepath = f"file://{os.path.abspath('anime_group_chat/frontend/index.html')}"
        page.goto(filepath)

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/group_chat.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_group_chat_frontend()
