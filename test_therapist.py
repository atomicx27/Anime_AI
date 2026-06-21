import os
from playwright.sync_api import sync_playwright

def test_anime_therapy():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Assuming the FastAPI server is running on localhost:8009 and serving the frontend
        page.goto("http://localhost:8009")

        # Verify page title
        assert "Anime Therapy AI" in page.title()

        # Fill in the struggle input
        page.fill("#struggleInput", "I'm feeling unmotivated and lost.")

        # Click the seek guidance button
        page.click("#seekTherapyBtn")

        # Wait for the results section to become visible
        # We use a relatively long timeout since the backend simulates "typing" via sleep
        page.wait_for_selector("#resultsSection", state="visible", timeout=15000)

        # Wait for the advice cards to be rendered
        page.wait_for_function('document.querySelectorAll("#adviceContainer .glass-panel").length >= 3', timeout=5000)

        # Ensure directory for screenshots exists
        os.makedirs("test-results", exist_ok=True)
        screenshot_path = "test-results/therapist_result.png"

        # Take a screenshot
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Test passed! Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_anime_therapy()
