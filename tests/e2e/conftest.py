import os
from collections.abc import Generator

import pytest
from playwright.sync_api import Browser, Page, Playwright, sync_playwright


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright]:
    """Provide a Playwright instance for the test session."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright_instance: Playwright) -> Generator[Browser]:
    """Provide a Chromium browser instance in headed mode for debugging."""
    headless = os.getenv("CI", "false").lower() in ("1", "true")
    browser = playwright_instance.chromium.launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser) -> Generator[Page]:
    """Provide a new page (tab) for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
