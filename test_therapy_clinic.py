import pytest
from playwright.sync_api import Page, expect

def test_therapy_clinic(page: Page):
    """
    E2E test for the Anime Therapy Clinic UI.
    Assumes the frontend is running on http://localhost:8012
    and backend on http://localhost:8011.
    """
    # Navigate to the local frontend server
    page.goto("http://localhost:8012")

    # Verify the title and header
    expect(page).to_have_title("Anime Therapy Clinic AI")
    expect(page.locator("h1")).to_contain_text("Anime Therapy Clinic AI")

    # Fill in a problem
    page.fill("#problemInput", "I'm feeling really stressed about my upcoming exams and I'm not sure how to handle the pressure.")

    # Submit the form
    page.click("#submitBtn")

    # Wait for the results container to become visible and populated
    # The container should have the flex class once results are loaded
    results_container = page.locator("#resultsContainer")

    # Use wait_for_function to ensure it becomes visible and has content
    page.wait_for_function('document.getElementById("resultsContainer").classList.contains("flex") && document.getElementById("resultsContainer").children.length > 0', timeout=10000)

    # Verify that at least one character response is shown
    expect(results_container.locator(".glass-panel").first).to_be_visible()

    # Take a screenshot for visual verification
    page.screenshot(path="therapy_clinic.png", full_page=True)
