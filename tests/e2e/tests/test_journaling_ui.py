"""Simple E2E tests using Faker for test data."""

import pytest
from playwright.sync_api import Page

from tests.e2e.pages.journal_page import JournalPage
from tests.shared.test_data import JournalEntryData


@pytest.mark.e2e
@pytest.mark.journal
@pytest.mark.smoke
@pytest.mark.parametrize("with_mood", [True, False])
def test_journal_submission(
    with_mood: bool,
    page: Page,
    ui_base_url: str,
    journal_entry_data: JournalEntryData,
    journal_entry_without_mood: JournalEntryData
) -> None:
    """Test journal submission with and without mood."""
    journal = JournalPage(page, ui_base_url)
    journal.open()

    if with_mood:
        journal.fill(content=journal_entry_data.content, mood=journal_entry_data.mood)
    else:
        journal.fill(content=journal_entry_without_mood.content)

    journal.submit()
    journal.expect_success()


@pytest.mark.e2e
@pytest.mark.journal
@pytest.mark.regression
def test_journal_submission_success_message(
    page: Page, ui_base_url: str, journal_entry_data: JournalEntryData
) -> None:
    """Test that a success message appears after submission."""
    journal = JournalPage(page, ui_base_url)
    journal.open()
    journal.fill(content=journal_entry_data.content, mood=journal_entry_data.mood)
    journal.submit()

    response_text = journal.get_response_text()
    assert "Saved" in response_text
    assert "id:" in response_text


@pytest.mark.e2e
@pytest.mark.journal
@pytest.mark.regression
def test_journal_form_validation(page: Page, ui_base_url: str) -> None:
    """Test form validation with empty content."""
    journal = JournalPage(page, ui_base_url)
    journal.open()

    # Try to submit an empty form
    journal.submit()

    assert not journal.is_response_visible(), (
        "Response element should not be visible for empty form"
    )
