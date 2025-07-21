from typing import Any

import requests


class APIClient:
    """Simple client for API endpoints."""

    def __init__(self, base_url: str) -> None:
        """Initialize the API client."""
        self.base_url = base_url.rstrip("/")

    def create_journal_entry(self, content: str) -> dict[str, Any]:
        """Create a new journal entry."""
        payload: dict[str, str] = {"content": content}
        url: str = f"{self.base_url}/api/v1/journal"
        response = requests.post(url, json=payload)
        return response.json()
