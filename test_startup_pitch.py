import os
import subprocess
import time
import pytest
from playwright.sync_api import sync_playwright

FRONTEND_URL = "http://localhost:8010"
BACKEND_URL = "http://localhost:8009"

def check_server_running(url):
    import urllib.request
    import urllib.error
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.error.URLError:
        return False

def test_startup_pitch():
    # Wait for servers to be up
    for _ in range(10):
        if check_server_running(f"{FRONTEND_URL}/index.html"):
            break
        time.sleep(1)
    else:
        pytest.fail("Frontend server did not start in time")

    for _ in range(10):
        # We can't easily check backend root as it relies on static files, check if port is open
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', 8009))
        sock.close()
        if result == 0:
            break
        time.sleep(1)
    else:
        pytest.fail("Backend server did not start in time")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the frontend
        page.goto(f"{FRONTEND_URL}/index.html")

        # Wait for the main elements to load
        page.wait_for_selector('h1:has-text("Anime Startup Pitch AI")')
        page.wait_for_selector('#pitchInput')
        page.wait_for_selector('#submitBtn')

        # Fill in a pitch
        test_pitch = "An AI-powered shield that uses magic to protect peace and end combat."
        page.fill('#pitchInput', test_pitch)

        # Submit the pitch
        page.click('#submitBtn')

        # Wait for the results to appear (loading state hides, results container shows)
        page.wait_for_selector('#resultsContainer', state='visible', timeout=10000)

        # Verify that overall decision is rendered
        overall_decision = page.inner_text('#overallDecision')
        assert overall_decision in ['Funded!', 'Rejected']

        # Verify that investor cards are rendered
        cards = page.query_selector_all('#investorCards > div')
        assert len(cards) > 0

        # Take a screenshot
        os.makedirs("test-results", exist_ok=True)
        page.screenshot(path="test-results/startup_pitch_results.png")

        browser.close()
