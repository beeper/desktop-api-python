# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.message import Message

__all__ = ["MessageListResponse"]


class MessageListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """True if additional results can be fetched."""

    items: List[Message]
    """Messages from the chat, sorted by timestamp.

    Use message.sortKey as cursor for pagination.
    """
