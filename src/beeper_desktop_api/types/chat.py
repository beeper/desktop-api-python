# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user import User

__all__ = ["Chat", "Participants"]


class Participants(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """True if there are more participants than included in items."""

    items: List[User]
    """Participants returned for this chat (limited by the request; may be a subset)."""

    total: int
    """Total number of participants in the chat."""


class Chat(BaseModel):
    id: str
    """Unique identifier of the chat across Beeper."""

    account_id: str = FieldInfo(alias="accountID")
    """Account ID this chat belongs to."""

    network: str
    """Display-only human-readable network name (e.g., 'WhatsApp', 'Messenger')."""

    participants: Participants
    """Chat participants information."""

    type: Literal["single", "group"]
    """Chat type: 'single' for direct messages, 'group' for group chats."""

    unread_count: int = FieldInfo(alias="unreadCount")
    """Number of unread messages."""

    description: Optional[str] = None
    """Description of the chat."""

    is_archived: Optional[bool] = FieldInfo(alias="isArchived", default=None)
    """True if chat is archived."""

    is_muted: Optional[bool] = FieldInfo(alias="isMuted", default=None)
    """True if the chat is muted."""

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)
    """True if the chat is pinned."""

    last_activity: Optional[datetime] = FieldInfo(alias="lastActivity", default=None)
    """Timestamp of last activity."""

    last_read_message_sort_key: Optional[str] = FieldInfo(alias="lastReadMessageSortKey", default=None)
    """Last read message sortKey."""

    local_chat_id: Optional[str] = FieldInfo(alias="localChatID", default=None)
    """Local chat ID specific to this Beeper Desktop installation."""

    title: Optional[str] = None
    """Display title of the chat."""
