# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .reaction import Reaction
from ..._models import BaseModel
from .attachment import Attachment

__all__ = ["Message"]


class Message(BaseModel):
    id: str
    """Stable message ID for cursor pagination."""

    account_id: str = FieldInfo(alias="accountID")
    """Beeper account ID the message belongs to."""

    chat_id: str = FieldInfo(alias="chatID")
    """Beeper chat/thread/room ID."""

    message_id: str = FieldInfo(alias="messageID")
    """Stable message ID (same as id)."""

    sender_id: str = FieldInfo(alias="senderID")
    """Sender user ID."""

    sort_key: Union[str, float] = FieldInfo(alias="sortKey")
    """A unique key used to sort messages"""

    timestamp: datetime
    """Message timestamp."""

    attachments: Optional[List[Attachment]] = None
    """Attachments included with this message, if any."""

    is_sender: Optional[bool] = FieldInfo(alias="isSender", default=None)
    """True if the authenticated user sent the message."""

    is_unread: Optional[bool] = FieldInfo(alias="isUnread", default=None)
    """True if the message is unread for the authenticated user. May be omitted."""

    reactions: Optional[List[Reaction]] = None
    """Reactions to the message, if any."""

    sender_name: Optional[str] = FieldInfo(alias="senderName", default=None)
    """
    Resolved sender display name (impersonator/full name/username/participant name).
    """

    text: Optional[str] = None
    """Plain-text body if present.

    May include a JSON fallback with text entities for rich messages.
    """
