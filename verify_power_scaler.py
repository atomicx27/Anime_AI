from playwright.sync_api import sync_playwright
import os
import sys

def run_cuj(page):
    # Use python's http.server to serve the files
    page.goto("http://localhost:8000/anime_power_scaler/frontend/index.html")
    page.wait_for_timeout(500)

    # Note: Backend isn't fully mocked, but we can verify visual states

    # Just checking hover states and basic layout
    page.hover('#char1-select')
    page.wait_for_timeout(500)

    page.hover('#simulate-btn')
    page.wait_for_timeout(500)

    # Take screenshot at the key moment
    page.screenshot(path="/home/jules/verification/screenshots/verification_power_scaler.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            context.close()
            browser.close()
