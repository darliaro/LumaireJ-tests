"""Main test configuration with shared fixtures."""

import sys
from pathlib import Path

# Ensure current directory is in sys.path to avoid conflicts with system 'tests' package
_project_root = Path(__file__).parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

# Import shared fixtures
from tests.shared.fixtures import api_base_url, base_url, is_ci, ui_base_url  # noqa: E402
from tests.shared.test_data import journal_entry_data, journal_entry_without_mood  # noqa: E402

# Re-export shared fixtures for global access
__all__ = [
    'base_url',
    'api_base_url',
    'ui_base_url',
    'is_ci',
    'journal_entry_data',
    'journal_entry_without_mood'
]
