import pytest
import requests

from schemas.journal import JournalEntryResponse


@pytest.mark.api
@pytest.mark.journal
def test_create_journal_entry(base_url: str) -> None:
    """Draft-Test for POST /journal"""
    payload = {"content": "Test content", "mood": "reflective"}

    response = requests.post(f"{base_url}/api/v1/journal", json=payload)
    assert response.status_code == 201

    parsed = JournalEntryResponse.model_validate(response.json())
    assert parsed.content == payload["content"]
