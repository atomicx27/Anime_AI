import re
from playwright.sync_api import Page, expect

def test_escape_room_ui(page: Page):
    # Navigate to the local server
    page.goto("http://localhost:8009/")

    # Check that the main title is present
    expect(page.locator("h1")).to_contain_text("Anime Escape Room AI")

    # Fill out the theme input
    page.fill("#themeInput", "A cyberpunk facility guarded by robotic sentinels and laser grids.")

    # Click the submit button
    page.click("#submitBtn")

    # Wait for the results container to be visible (the loading state will hide and this will show)
    # The timeout is slightly longer to account for backend processing
    page.wait_for_selector("#resultsContainer", state="visible", timeout=15000)

    # Check that roles are rendered. We expect at least one role card.
    role_cards = page.locator(".role-card")
    expect(role_cards.first).to_be_visible()

    # There should be exactly 4 roles assigned
    expect(role_cards).to_have_count(4)

    # Take a screenshot for verification
    page.screenshot(path="escape_room.png")

    # Wait for the first log line to appear (the typing effect is staggered)
    page.wait_for_selector("#escapeLog p", state="visible", timeout=10000)

    # Wait a bit for more log lines to appear
    page.wait_for_timeout(3000)

    # Take another screenshot of the log rendering
    page.screenshot(path="escape_room_log.png")

    # Verify there are log lines present
    log_lines = page.locator("#escapeLog p")
    assert log_lines.count() > 0
