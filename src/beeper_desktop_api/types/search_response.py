# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .chat import Chat
from .._models import BaseModel
from .shared.message import Message

__all__ = ["SearchResponse", "Results", "ResultsMessages"]


class ResultsMessages(BaseModel):
    chats: Dict[str, Chat]
    """Map of chatID -> chat details for chats referenced in items."""

    has_more: bool = FieldInfo(alias="hasMore")
    """True if additional results can be fetched using the provided cursors."""

    items: List[Message]
    """Messages matching the query and filters."""

    newest_cursor: Optional[str] = FieldInfo(alias="newestCursor", default=None)
    """Cursor for fetching newer results (use with direction='after').

    Opaque string; do not inspect.
    """

    oldest_cursor: Optional[str] = FieldInfo(alias="oldestCursor", default=None)
    """Cursor for fetching older results (use with direction='before').

    Opaque string; do not inspect.
    """


class Results(BaseModel):
    chats: List[Chat]
    """Top chat results."""

    in_groups: List[Chat]
    """Top group results by participant matches."""

    messages: ResultsMessages


class SearchResponse(BaseModel):
    results: Results
