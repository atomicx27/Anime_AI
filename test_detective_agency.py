import time
from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8007/")

        # Verify page loaded
        page.wait_for_selector("text=Anime Detective Agency AI")

        # Fill in a mystery
        page.fill("#mysteryInput", "The case of the missing ramen recipe. It vanished from a locked room with no signs of forced entry. Only logic can solve this.")

        # Click submit
        page.click("#submitBtn")

        # Wait for the result section to be visible
        page.wait_for_selector("#resultsSection", state="visible", timeout=15000)

        # Wait for typing effects to finish to get a nice screenshot
        time.sleep(3)

        # Capture screenshot
        page.screenshot(path="screenshots/detective_agency_result.png", full_page=True)

        browser.close()
        print("Playwright test completed successfully.")

if __name__ == "__main__":
    run_test()
