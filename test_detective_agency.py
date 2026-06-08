from playwright.sync_api import sync_playwright
import os

def test_detective_agency():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Connect to the local HTTP server for the anime detective agency
        # The backend runs on 8007 and serves the frontend at the root
        page.goto("http://localhost:8007")

        # Interact with UI
        page.fill('#case-input', 'Someone stole my limited edition Naruto action figure from a locked room!')
        page.click('#solve-btn')

        # Wait for results to be visible
        page.wait_for_selector('#results-container:not(.hidden)', timeout=15000)

        # Verify that an investigator was assigned
        # The script dynamically adds team members to the #team-grid. We check for a child element.
        assert page.locator('#team-grid > div').count() > 0

        print("Test passed successfully!")
        browser.close()

if __name__ == "__main__":
    test_detective_agency()
