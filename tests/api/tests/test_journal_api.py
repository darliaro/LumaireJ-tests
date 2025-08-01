"""Simple API tests using Faker for test data."""

import pytest

from tests.api.clients.api_client import APIClient
from tests.api.schemas.journal_schema import JournalEntryResponse
from tests.shared.test_data import JournalEntryData


@pytest.mark.api
@pytest.mark.journal
@pytest.mark.smoke
def test_create_journal_entry_with_content(
    api_base_url: str, journal_entry_data: JournalEntryData) -> None:
    """Test creation of a journal entry with content."""
    client = APIClient(api_base_url)
    result = client.create_journal_entry(journal_entry_data.content)
    entry = JournalEntryResponse.model_validate(result)

    assert entry.content == journal_entry_data.content


@pytest.mark.api
@pytest.mark.journal
@pytest.mark.smoke
def test_create_journal_entry_with_mood(api_base_url: str, journal_entry_data: JournalEntryData) -> None:
    """Test creation of a journal entry with mood."""
    client = APIClient(api_base_url)
    result = client.create_journal_entry(journal_entry_data.content, journal_entry_data.mood)
    entry = JournalEntryResponse.model_validate(result)

    assert entry.content == journal_entry_data.content


@pytest.mark.api
@pytest.mark.journal
@pytest.mark.regression
def test_create_journal_entry_without_mood(api_base_url: str, journal_entry_without_mood: JournalEntryData) -> None:
    """Test creation of a journal entry without mood."""
    client = APIClient(api_base_url)
    result = client.create_journal_entry(journal_entry_without_mood.content)
    entry = JournalEntryResponse.model_validate(result)

    assert entry.content == journal_entry_without_mood.content
