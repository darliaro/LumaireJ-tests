import os

import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url() -> str:
    """Return the API base URL from the environment."""
    url = os.getenv("BASE_URL")
    return url
