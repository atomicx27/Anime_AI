import time
from playwright.sync_api import sync_playwright

def test_detective_agency():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the frontend served on port 8008
        page.goto("http://localhost:8008")

        # Verify the title
        assert "Anime Detective Agency AI" in page.title()

        # Fill in the mystery input
        mystery_text = "The legendary Sword of Totsuka has been stolen from the spiritual realm. There was no sign of a forced entry, only a lingering smell of ozone and a few scattered black feathers."
        page.fill("#mystery-input", mystery_text)

        # Click the solve button
        page.click("#solve-btn")

        # Wait for the results to load (wait for the investigations grid to have children)
        # We wait for the cards to appear
        page.wait_for_selector("#investigations-grid > div", state="attached", timeout=10000)

        # Give a small buffer for typing animations to finish
        time.sleep(3)

        # Take a screenshot
        screenshot_path = "detective_agency_result.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_detective_agency()
