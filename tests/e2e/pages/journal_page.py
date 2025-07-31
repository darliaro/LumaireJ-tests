# tests/e2e/pages/journal_page.py
from playwright.sync_api import Page, expect


class JournalPage:
    """Page Object Model for the journaling HTML page."""
    BASE_PATH = "/static/journal.html"

    CONTENT = "#content"
    MOOD    = "#mood"
    SUBMIT  = "button[type=submit]"
    RESPONSE = "#response"

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.url = f"{base_url.rstrip('/')}{self.BASE_PATH}"

    def open(self) -> None:
        """Navigate to the journaling page and wait for it to fully load."""
        self.page.goto(self.url, wait_until="load")

    def fill(self, content: str, mood: str = "") -> None:
        """Fill out the journaling form."""
        self.page.locator(self.CONTENT).fill(content)
        if mood:
            self.page.locator(self.MOOD).fill(mood)

    def submit(self) -> None:
        """Submit the journaling form."""
        self.page.locator(self.SUBMIT).click()

    def expect_success(self) -> None:
        """Assert that a success message appears with an ID number."""
        locator = self.page.locator(self.RESPONSE)
        expect(locator).to_contain_text("Entry created! ID:", timeout=5000)
