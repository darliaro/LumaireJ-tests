"""Simple E2E tests using Faker for test data."""

import pytest
from playwright.sync_api import Page

from tests.e2e.pages.journal_page import JournalPage
from tests.shared.test_data import JournalEntryData


@pytest.mark.e2e
@pytest.mark.journal
@pytest.mark.smoke
def test_journal_submission_with_mood(
    page: Page, ui_base_url: str, journal_entry_data: JournalEntryData
) -> None:
    """Test journal submission with mood."""
    journal = JournalPage(page, ui_base_url)
    journal.open()
    journal.fill(content=journal_entry_data.content, mood=journal_entry_data.mood)
    journal.submit()
    journal.expect_success()


@pytest.mark.e2e
@pytest.mark.journal
@pytest.mark.smoke
def test_journal_submission_without_mood(
    page: Page, ui_base_url: str, journal_entry_without_mood: JournalEntryData
) -> None:
    """Test journal submission without mood."""
    journal = JournalPage(page, ui_base_url)
    journal.open()
    journal.fill(content=journal_entry_without_mood.content)
    journal.submit()
    journal.expect_success()


@pytest.mark.e2e
@pytest.mark.journal
@pytest.mark.regression
def test_journal_page_loads(page: Page, ui_base_url: str) -> None:
    """Test that the journal page loads correctly."""
    journal = JournalPage(page, ui_base_url)
    journal.open()

    content_locator = journal.page.locator(journal.CONTENT)
    mood_locator = journal.page.locator(journal.MOOD)
    submit_locator = journal.page.locator(journal.SUBMIT)

    assert content_locator.is_visible()
    assert mood_locator.is_visible()
    assert submit_locator.is_visible()


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

    # Verify success message appears
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

    # Check that a response element remains hidden (form should not submit)
    response_locator = journal.page.locator(journal.RESPONSE)
    assert not response_locator.is_visible(), (
        "Response element should not be visible for empty form"
    )

    # Also check that no text appears
    response_text = journal.get_response_text_if_visible()
    assert response_text == "", "Response should be empty for invalid form"
