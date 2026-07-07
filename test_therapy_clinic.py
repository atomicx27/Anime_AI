import pytest
from playwright.sync_api import sync_playwright
import time
import requests

def wait_for_server(url, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.ConnectionError:
            pass
        time.sleep(1)
    return False

def test_therapy_clinic_frontend():
    # Assume frontend is on 8012 and backend on 8011

    # Check if frontend is accessible (at least the port)
    if not wait_for_server("http://localhost:8012", timeout=5):
        print("Warning: Frontend server might not be ready, but proceeding with test.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto("http://localhost:8012/index.html")

            # Verify the title
            assert "Anime Therapy Clinic" in page.title()

            # Fill out the form
            page.fill("#problemInput", "I am feeling overwhelmed by all my responsibilities at work and I don't know how to balance everything.")

            # Click submit
            page.click("#submitBtn")

            # Wait for results container to become visible, not the loading state
            page.wait_for_selector("#resultsContainer", state="visible", timeout=15000)

            # Allow some time for animations
            page.wait_for_timeout(2000)

            # Verify that advice cards were generated
            cards_count = page.locator("#adviceCards > div").count()
            assert cards_count > 0, "No advice cards were generated"

            # Take screenshot
            page.screenshot(path="therapy_clinic.png", full_page=True)
            print(f"Successfully generated {cards_count} advice cards. Screenshot saved to therapy_clinic.png")

        except Exception as e:
            page.screenshot(path="therapy_clinic_error.png")
            print(f"Test failed: {e}. Screenshot saved to therapy_clinic_error.png")
            raise
        finally:
            browser.close()

if __name__ == "__main__":
    test_therapy_clinic_frontend()