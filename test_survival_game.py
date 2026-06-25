import time
from playwright.sync_api import sync_playwright

def test_survival_game():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        print("Navigating to http://localhost:8009/")
        page.goto("http://localhost:8009/")

        print("Filling scenario input...")
        page.fill("#scenarioInput", "A massive earthquake traps everyone in an underground facility.")

        print("Clicking simulate button...")
        page.click("#simulateBtn")

        print("Waiting for roles to populate...")
        page.wait_for_selector("#rolesContainer > div", state="visible", timeout=15000)

        # Wait for log animations to finish
        time.sleep(5)

        print("Taking screenshot...")
        page.screenshot(path="survival_game.png")

        browser.close()
        print("Test complete. Screenshot saved to survival_game.png")

if __name__ == "__main__":
    test_survival_game()
