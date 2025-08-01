from datetime import datetime

from pydantic import BaseModel


class JournalEntryResponse(BaseModel):
    """Journal entry schema returned by the POST /journal API"""

    id: int
    content: str
    created_at: datetime
    mood: str | None
