import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def context(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/"  # Directory where videos will be saved
    )
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

def test_record_video(page):
    page.goto("https://example.com")
    
    # Intentionally failing assertion
    assert page.locator("text=Non-Existent Element").is_visible()