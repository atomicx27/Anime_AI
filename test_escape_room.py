import pytest
import requests
import time
from playwright.sync_api import Page, expect

BACKEND_URL = "http://localhost:8010"

def wait_for_server(url, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(f"{url}/api/characters")
            if response.status_code == 200:
                return True
        except requests.ConnectionError:
            pass
        time.sleep(1)
    return False

@pytest.fixture(scope="session", autouse=True)
def ensure_server_running():
    if not wait_for_server(BACKEND_URL):
        pytest.fail(f"Backend server did not start in time at {BACKEND_URL}")

def test_api_characters():
    response = requests.get(f"{BACKEND_URL}/api/characters")
    assert response.status_code == 200
    data = response.json()
    assert "characters" in data
    assert len(data["characters"]) > 0
    assert "name" in data["characters"][0]

def test_api_simulate():
    response = requests.post(
        f"{BACKEND_URL}/api/simulate",
        json={"scenario": "Trapped in a sinking submarine."}
    )
    assert response.status_code == 200
    data = response.json()

    assert data["scenario"] == "Trapped in a sinking submarine."
    assert "team" in data
    assert len(data["team"]) > 0
    assert "role" in data["team"][0]

    assert "narrative" in data
    assert len(data["narrative"]) > 0

    assert "outcome" in data

def test_frontend_escape_room_simulation(page: Page):
    # Navigate to the frontend
    page.goto(f"{BACKEND_URL}/")

    # Check title
    expect(page.locator("h1")).to_contain_text("Anime Escape Room AI")

    # Fill out the scenario
    page.fill("#scenarioInput", "A high-tech laboratory rapidly filling with toxic gas.")

    # Click simulate
    page.click("#simulateBtn")

    # Wait for the results to appear. The loading state is transient, so we wait for the team container.
    page.wait_for_selector("#teamContainer", state="visible", timeout=10000)
    page.wait_for_selector("#terminalContainer", state="visible", timeout=10000)

    # Verify team cards exist
    team_cards = page.locator("#teamGrid > div")
    expect(team_cards).to_have_count(4) # Expected 4 characters as per agent.py

    # Take a screenshot for verification
    page.screenshot(path="screenshots/escape_room.png", full_page=True)
