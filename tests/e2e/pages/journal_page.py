"""Simple Page Object Model for the journaling page."""

from playwright.sync_api import Page, expect


class JournalPage:
    """Page Object Model for the journaling page."""

    BASE_PATH = "/static/journal.html"

    # Selectors
    CONTENT = "#content"
    MOOD = "#mood"
    SUBMIT = "button[type=submit]"
    RESPONSE = "#response"

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.url = f"{base_url.rstrip('/')}{self.BASE_PATH}"

    def open(self) -> None:
        """Navigate to the journaling page."""
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
        """Assert that a success message appears."""
        locator = self.page.locator(self.RESPONSE)
        # New UI shows a multi-line message like:
        # "Saved\nid: <num>\nat: <timestamp>"
        expect(locator).to_contain_text("Saved", timeout=5000)
        expect(locator).to_contain_text("id:")

    def get_response_text(self) -> str:
        """Get the text from the response element."""
        response_locator = self.page.locator(self.RESPONSE)

        # Wait for a response element to be visible
        response_locator.wait_for(state="visible", timeout=5000)

        # Get text content
        text = response_locator.text_content() or ""
        return text

    def get_response_text_if_visible(self) -> str:
        """Get the text from the response element without waiting."""
        response_locator = self.page.locator(self.RESPONSE)

        # Get text content without waiting
        text = response_locator.text_content() or ""
        return text
