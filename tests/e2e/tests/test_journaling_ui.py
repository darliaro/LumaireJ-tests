# tests/e2e/tests/test_journaling_ui.py
import pytest
from playwright.sync_api import Page

from tests.e2e.pages.journal_page import JournalPage


@pytest.mark.e2e
@pytest.mark.journal
def test_journal_submission(page: Page, base_url: str) -> None:
    """
    Verify that submitting the journal form with valid data shows a success message."""
    journal = JournalPage(page, base_url)
    journal.open()
    journal.fill(content="Feeling hopeful today", mood="hopeful")
    journal.submit()
    journal.expect_success()
