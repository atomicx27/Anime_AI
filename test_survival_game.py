import pytest
from playwright.sync_api import Page, expect

def test_anime_survival_game(page: Page):
    # Navigate to the local backend serving the frontend
    page.goto("http://localhost:8009/")

    # Check the title
    expect(page).to_have_title("Anime Survival Game AI")

    # Check that the main heading is visible
    heading = page.locator("h1", has_text="Anime Survival Game AI")
    expect(heading).to_be_visible()

    # Wait for the input field to be visible and type a scenario
    scenario_input = page.locator("#scenarioInput")
    expect(scenario_input).to_be_visible()
    scenario_input.fill("A catastrophic blizzard hitting the hidden village.")

    # Click the simulate button
    simulate_btn = page.locator("#surviveBtn")
    simulate_btn.click()

    # Wait for the squad container to be visible (it loses the hidden class)
    # The simulation might take a short moment, and animations follow.
    squad_container = page.locator("#squadContainer")

    # We wait for the first log entry to confirm simulation is running
    log_container = page.locator("#logContainer")
    # Wait for at least one log entry (div inside logContainer that's not the loader)
    # The first actual log will have the role badge or time tag.
    page.wait_for_selector("#squadList .glass-card", timeout=10000)

    # Wait for the "End of Day" log or just wait a bit for animations
    page.wait_for_function('document.querySelectorAll("#logContainer > div.animate-fade-in").length > 0', timeout=10000)

    # Take a screenshot
    page.screenshot(path="survival_game.png", full_page=True)

    # Basic assertions
    squad_cards = page.locator("#squadList .glass-card")
    expect(squad_cards).to_have_count(4) # We assign 4 roles: Leader, Scavenger, Defender, Medic

    logs = page.locator("#logContainer > div.animate-fade-in")
    # There should be at least a few logs depending on who was assigned
    count = logs.count()
    assert count > 0, "Expected survival logs to be generated"
