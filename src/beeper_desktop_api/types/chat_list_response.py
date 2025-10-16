# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .chat import Chat
from .shared.message import Message

__all__ = ["ChatListResponse"]


class ChatListResponse(Chat):
    preview: Optional[Message] = None
    """Last message preview for this chat, if available."""
