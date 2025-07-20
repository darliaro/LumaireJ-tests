import os

import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def base_url() -> str:
    """Returns the resolved base URL from pytest CLI options"""
    return os.getenv("BASE_URL")
