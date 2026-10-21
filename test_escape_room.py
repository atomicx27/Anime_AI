import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        browser.close()

def test_escape_room_simulation(browser_context):
    page = browser_context.new_page()

    # The frontend and backend are both served by main.py on port 8010
    page.goto("http://localhost:8010/")

    # Verify title
    assert "Anime Escape Room AI" in page.title()

    # Verify header is visible
    assert page.locator("h1:has-text('Anime Escape Room AI')").is_visible()

    # Enter a theme
    theme_input = page.locator("#themeInput")
    theme_input.fill("A trapped high-tech submarine at the bottom of the ocean.")

    # Click start button
    start_btn = page.locator("#startBtn")
    start_btn.click()

    # Wait for the results to become visible (roles and terminal)
    # The terminal auto-scroll happens after 2500ms, and animations take time
    # Waiting for the roles container to have children is a good indicator
    page.wait_for_selector("#rolesContainer > div", state="visible", timeout=15000)

    # Verify Roles panel
    roles_panel = page.locator("#rolesPanel")
    assert roles_panel.is_visible()

    roles_cards = page.locator("#rolesContainer > div")
    assert roles_cards.count() == 4

    # Verify Terminal panel
    terminal_panel = page.locator("#terminalPanel")
    assert terminal_panel.is_visible()

    terminal_logs = page.locator("#terminal-content p")
    assert terminal_logs.count() > 0

    # Check for specific success/fail text in logs
    log_text = terminal_panel.inner_text()
    assert "successfully escaped" in log_text or "failed to escape" in log_text
