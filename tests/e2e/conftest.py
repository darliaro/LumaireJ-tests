"""Simple E2E test configuration."""

from collections.abc import Generator

import pytest
from playwright.sync_api import Browser, Page, Playwright, sync_playwright


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright]:
    """Provide a Playwright instance for the test session."""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright_instance: Playwright, is_ci: bool) -> Generator[Browser]:
    """Provide a browser instance."""
    headless = is_ci
    browser = playwright_instance.chromium.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser) -> Generator[Page]:
    """Provide a new page for each test."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
