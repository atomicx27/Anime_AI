import pytest
from playwright.sync_api import Page, expect

def test_anime_escape_room(page: Page):
    # Navigate to the frontend
    page.goto("http://localhost:8010/")

    # Check title and header
    expect(page).to_have_title("Anime Escape Room AI")
    expect(page.locator("h1")).to_contain_text("Anime Escape Room AI")

    # Fill in the scenario
    scenario_input = page.locator("#scenarioInput")
    scenario_input.fill("A room filled with ancient glowing runes and a countdown timer.")

    # Click the simulate button
    simulate_btn = page.locator("#simulateBtn")
    simulate_btn.click()

    # The terminal should become visible
    terminal_container = page.locator("#terminalContainer")
    expect(terminal_container).to_be_visible()

    # Wait for the results to appear (rolesGrid should be populated)
    # The terminal log types out, which takes time, so we wait for the results container
    results_container = page.locator("#resultsContainer")
    expect(results_container).to_be_visible(timeout=15000)

    # Check that role cards are rendered
    role_cards = page.locator(".role-card")
    expect(role_cards).to_have_count(4)

    # Take a screenshot
    page.screenshot(path="screenshots/escape_room.png", full_page=True)
