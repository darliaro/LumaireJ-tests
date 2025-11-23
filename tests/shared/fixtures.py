"""Shared fixtures for API and E2E tests."""

import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def base_url() -> str:
    """Return the base URL for API and UI."""
    url = os.getenv("BASE_URL", "").rstrip("/")
    if not url:
        pytest.skip("BASE_URL environment variable is not set")
    return url


@pytest.fixture(scope="session")
def api_base_url(base_url: str) -> str:
    """Return the API base URL."""
    return f"{base_url}/api/v1"


@pytest.fixture(scope="session")
def ui_base_url(base_url: str) -> str:
    """Return the UI base URL."""
    return base_url


@pytest.fixture(scope="session")
def is_ci() -> bool:
    """Check if running in a CI environment."""
    return os.getenv("CI", "false").lower() in ("1", "true")
