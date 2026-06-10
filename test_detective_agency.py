import time
import subprocess
import os
from playwright.sync_api import sync_playwright

def test_anime_detective_agency():
    print("Starting Anime Detective Agency Test...")

    # 1. Start the backend server
    print("Starting backend server...")
    backend_process = subprocess.Popen(
        ["python3", "main.py"],
        cwd="anime_detective_agency/backend",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # 2. Start frontend http server
    print("Starting frontend server...")
    frontend_process = subprocess.Popen(
        ["python3", "-m", "http.server", "8087"],
        cwd="anime_detective_agency/frontend",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Give servers time to start
    time.sleep(3)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Navigate to frontend
            print("Navigating to UI...")
            page.goto("http://localhost:8087/index.html")
            page.wait_for_selector("text=ANIME DETECTIVE AGENCY")

            # Fill the input
            print("Submitting a case...")
            page.fill("#caseInput", "A wealthy noble was found poisoned in a locked room. There are no signs of forced entry, but a strange magical aura lingers near the tea cup.")

            # Click the investigate button
            page.click("#investigateBtn")

            # Wait for results to load (checking for a role badge to appear)
            print("Waiting for agent to process...")
            page.wait_for_selector(".role-badge", timeout=15000)

            # Verify results populated
            cards = page.locator(".glass-panel .role-badge")
            count = cards.count()
            print(f"Test complete. Found {count} assigned roles.")
            assert count > 0, "No assigned roles were displayed."

            # Take screenshot for verification
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            page.screenshot(path="screenshots/detective_agency_test.png", full_page=True)
            print("Screenshot saved to screenshots/detective_agency_test.png")

            browser.close()
            print("Test passed successfully!")

    finally:
        # Cleanup processes
        print("Cleaning up processes...")
        backend_process.terminate()
        frontend_process.terminate()
        backend_process.wait()
        frontend_process.wait()

if __name__ == "__main__":
    test_anime_detective_agency()
