import pytest

# Configure Playwright to record video for all tests
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_dir": "./videos",  # Directory where videos will be saved
        "record_video_size": {"width": 1280, "height": 720}  # Video resolution
    }