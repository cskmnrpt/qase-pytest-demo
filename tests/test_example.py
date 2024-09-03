import pytest

def test_example_com_title(page):
    # Navigate to the Example website and check the title
    page.goto("https://example.com")
    assert page.title() == "Example Domain"

def test_example_com_content(page):
    # Check that the h1 element contains the correct text
    page.goto("https://example.com")
    h1_text = page.locator("h1").text_content()
    assert h1_text == "Example Domain"

def test_example_com_link_navigation(page):
    # Check that the "More information" link navigates to the correct page
    page.goto("https://example.com")
    page.click("a")
    assert page.url == "https://www.iana.org/domains/reserved"

def test_google_search(page):
    # Perform a search on Google and verify the results page
    page.goto("https://www.google.com")
    page.fill("input[name='q']", "Playwright Python")
    page.press("input[name='q']", "Enter")
    page.wait_for_timeout(2000)  # Wait for results to load
    results_text = page.locator("#search").text_content()
    assert "playwright.dev" in results_text

def test_form_submission(page):
    # Simulate filling out and submitting a form
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    success_message = page.locator(".flash.success").text_content()
    assert "You logged into a secure area!" in success_message

@pytest.mark.parametrize("url, title", [
    ("https://example.com", "Example Domain"),
    ("https://playwright.dev", "Fast and reliable end-to-end testing for modern web apps | Playwright"),
    ("https://www.python.org", "Welcome to Python.org"),
])
def test_multiple_sites(page, url, title):
    # Parametrized test to check titles of different websites
    page.goto(url)
    assert page.title() == title