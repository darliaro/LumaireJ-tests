"""Simple API client for endpoints."""

from typing import Any

import requests

from tests.shared.constants import API_REQUEST_TIMEOUT_SEC


class APIClient:
    """Simple client for API endpoints."""

    def __init__(self, base_url: str) -> None:
        """Initialize the API client."""
        self.base_url = base_url.rstrip("/")

    def create_journal_entry(self, content: str, mood: str = "") -> dict[str, Any]:
        """Create a new journal entry."""
        payload: dict[str, str] = {"content": content}
        if mood:
            payload["mood"] = mood

        url: str = f"{self.base_url}/journal"
        response = requests.post(url, json=payload, timeout=API_REQUEST_TIMEOUT_SEC)
        response.raise_for_status()
        return response.json()
