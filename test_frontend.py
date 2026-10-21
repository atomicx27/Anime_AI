from playwright.sync_api import sync_playwright
import os

def test_debate_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Construct path to local HTML file
        filepath = f"file://{os.path.abspath('anime_debate_arena/frontend/index.html')}"
        page.goto(filepath)

        # Interact with UI
        page.fill('#topicInput', 'Is true peace achievable without sacrifice?')

        # Take screenshot
        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/debate_arena.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_debate_frontend()
