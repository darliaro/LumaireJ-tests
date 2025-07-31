import os

import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url() -> str:
    """Return the base root URL (host:port) for API and UI."""
    return os.getenv("BASE_URL", "").rstrip("/")
