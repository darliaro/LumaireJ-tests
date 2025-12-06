"""Simple API tests using Faker for test data."""

from datetime import datetime

import pytest

from tests.api.clients.api_client import APIClient
from tests.api.schemas.journal_schema import JournalEntryResponse
from tests.shared.test_data import JournalEntryData


@pytest.mark.api
@pytest.mark.journal
@pytest.mark.smoke
def test_create_journal_entry_with_content(
    api_client: APIClient, journal_entry_data: JournalEntryData) -> None:
    """Test creation of a journal entry with content."""
    result = api_client.create_journal_entry(journal_entry_data.content)
    entry = JournalEntryResponse.model_validate(result)

    # Comprehensive field validation
    assert entry.content == journal_entry_data.content
    assert isinstance(entry.id, int)
    assert entry.id > 0
    assert isinstance(entry.created_at, datetime)
    assert entry.mood is None


@pytest.mark.api
@pytest.mark.journal
@pytest.mark.smoke
def test_create_journal_entry_with_mood(api_client: APIClient, journal_entry_data: JournalEntryData) -> None:
    """Test creation of a journal entry with mood."""
    result = api_client.create_journal_entry(journal_entry_data.content, journal_entry_data.mood)
    entry = JournalEntryResponse.model_validate(result)

    # Comprehensive field validation
    assert entry.content == journal_entry_data.content
    assert entry.mood == journal_entry_data.mood
    assert isinstance(entry.id, int)
    assert entry.id > 0
    assert isinstance(entry.created_at, datetime)


@pytest.mark.api
@pytest.mark.journal
@pytest.mark.regression
def test_create_journal_entry_without_mood(api_client: APIClient, journal_entry_without_mood: JournalEntryData) -> None:
    """Test creation of a journal entry without mood."""
    result = api_client.create_journal_entry(journal_entry_without_mood.content)
    entry = JournalEntryResponse.model_validate(result)

    # Comprehensive field validation
    assert entry.content == journal_entry_without_mood.content
    assert entry.mood is None
    assert isinstance(entry.id, int)
    assert entry.id > 0
    assert isinstance(entry.created_at, datetime)
