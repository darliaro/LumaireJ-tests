"""Main test configuration with shared fixtures."""

# Import shared fixtures
from tests.shared.fixtures import api_base_url, api_client, base_url, is_ci, ui_base_url
from tests.shared.test_data import journal_entry_data, journal_entry_without_mood

# Re-export shared fixtures for global access
__all__ = [
    'base_url',
    'api_base_url',
    'api_client',
    'ui_base_url',
    'is_ci',
    'journal_entry_data',
    'journal_entry_without_mood'
]
