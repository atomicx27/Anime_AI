from playwright.sync_api import sync_playwright
import os
import subprocess
import time

def test_frontend():
    # Start backend so API loads characters!
    proc = subprocess.Popen(['python3', 'anime_power_scaler/backend/main.py'])
    time.sleep(3) # Wait for it to start

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # The issue: anime_power_scaler fetch calls `/api/characters`.
        # When opening via `file://`, `/api/characters` becomes `file:///api/characters`, which fails!
        # It needs to point to `http://localhost:8006/api/characters` or we just mock the fetch.

        # We can intercept network requests and fulfill them or we can run a simple HTTP server.
        # It's easier to mock the DOM directly as I did before.

        filepath = f"file://{os.path.abspath('anime_power_scaler/frontend/index.html')}"
        page.goto(filepath)

        page.wait_for_selector('#char1-select')

        # Manually populate options
        page.evaluate('''() => {
            const select1 = document.getElementById('char1-select');
            const select2 = document.getElementById('char2-select');

            // clear first
            select1.innerHTML = '<option value="">Select Character...</option>';
            select2.innerHTML = '<option value="">Select Character...</option>';

            const opt1 = document.createElement('option');
            opt1.value = 'Naruto Uzumaki';
            opt1.text = 'Naruto Uzumaki';
            select1.appendChild(opt1);

            const opt2 = document.createElement('option');
            opt2.value = 'Son Goku';
            opt2.text = 'Son Goku';
            select2.appendChild(opt2);
        }''')

        try:
            page.select_option('#char1-select', value='Naruto Uzumaki')
            page.select_option('#char2-select', value='Son Goku')

            # Since fetch('/api/battle') will ALSO fail via file://, we mock window.fetch!
            page.evaluate('''() => {
                window.fetch = async (url, options) => {
                    if (url.includes('/api/battle')) {
                        return {
                            ok: true,
                            json: async () => ({
                                char1: { name: 'Naruto Uzumaki', archetype: 'Protagonist' },
                                char2: { name: 'Son Goku', archetype: 'Protagonist' },
                                logs: ['Mock log 1', 'Mock log 2'],
                                winner: 'Son Goku',
                                summary: 'Goku wins in mock battle.'
                            })
                        };
                    }
                    return { ok: false };
                };
            }''')

            page.click('#simulate-btn')
            page.wait_for_selector('#results-card:not(.hidden)', timeout=10000)
        except Exception as e:
            print("Failed interaction:", e)

        os.makedirs('screenshots', exist_ok=True)
        screenshot_path = 'screenshots/power_scaler.png'
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

    proc.terminate()

if __name__ == "__main__":
    test_frontend()
