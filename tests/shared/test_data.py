"""Simple test data management using Faker."""

from dataclasses import dataclass
from typing import Self

import pytest
from faker import Faker

# Initialize Faker
fake = Faker(["en_US", "ru_RU"])


@dataclass(slots=True)
class JournalEntryData:
    """Test data for journal entries."""

    content: str
    mood: str = ""

    @classmethod
    def create_random(cls) -> Self:
        """Create random test data using Faker."""
        return cls(
            content=fake.text(max_nb_chars=100),
            mood=fake.random_element(
                elements=("happy", "excited", "calm", "motivated", "grateful")
            ),
        )

    @classmethod
    def create_without_mood(cls) -> Self:
        """Create data without a mood."""
        return cls(content=fake.text(max_nb_chars=100))


@pytest.fixture
def journal_entry_data() -> JournalEntryData:
    """Fixture for random journal data."""
    return JournalEntryData.create_random()


@pytest.fixture
def journal_entry_without_mood() -> JournalEntryData:
    """Fixture for data without a mood."""
    return JournalEntryData.create_without_mood()
