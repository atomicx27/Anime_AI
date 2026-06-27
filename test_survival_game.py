import time
import pytest
from playwright.sync_api import Page, expect

def test_survival_game(page: Page):
    # Navigate to the local server
    page.goto("http://localhost:8010/")

    # Check the title
    expect(page).to_have_title("Anime Survival Game AI")

    # Take initial screenshot
    page.screenshot(path="screenshots/survival_game_initial.png")

    # Fill in the scenario input
    page.fill("#scenarioInput", "Trapped in a room with a hungry zombie")

    # Click the simulate button
    page.click("#simulateBtn")

    # Wait for the results to populate
    # The results are injected dynamically, so we wait for cards to appear
    page.wait_for_selector("#resultsContainer > div", state="visible", timeout=15000)

    # Optional: wait a bit more for animations to finish
    time.sleep(1)

    # Assert that cards are rendered
    cards = page.locator("#resultsContainer > div")
    expect(cards).to_have_count(14)  # Ensure 14 characters were loaded and processed

    # Take final screenshot
    page.screenshot(path="screenshots/survival_game_results.png", full_page=True)
