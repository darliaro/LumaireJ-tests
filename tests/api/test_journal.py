import pytest

from clients.api_client import APIClient
from schemas.journal import JournalEntryResponse


@pytest.mark.api
@pytest.mark.journal
def test_create_journal_entry(base_url: str) -> None:
    """Test creation of a journal entry."""
    client = APIClient(base_url)
    result = client.create_journal_entry("Test content")
    entry = JournalEntryResponse.model_validate(result)
    assert entry.content == "Test content"
