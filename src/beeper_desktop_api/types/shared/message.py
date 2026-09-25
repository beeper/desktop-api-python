# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .reaction import Reaction
from ..._models import BaseModel
from .attachment import Attachment
from .send_status import SendStatus
from .link_preview import LinkPreview

__all__ = ["Message"]


class Message(BaseModel):
    id: str
    """Message ID."""

    account_id: str = FieldInfo(alias="accountID")
    """Beeper account ID the message belongs to."""

    chat_id: str = FieldInfo(alias="chatID")
    """Chat ID.

    Input routes also accept the local chat ID from this installation when
    available.
    """

    sender_id: str = FieldInfo(alias="senderID")
    """Fully qualified sender user ID.

    Network-backed IDs usually include the network prefix and homeserver.
    """

    sort_key: str = FieldInfo(alias="sortKey")
    """A unique, sortable key used to sort messages."""

    timestamp: datetime
    """Message timestamp."""

    attachments: Optional[List[Attachment]] = None
    """Attachments included with this message, if any."""

    edited_timestamp: Optional[datetime] = FieldInfo(alias="editedTimestamp", default=None)
    """Timestamp when the message was edited, if known."""

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)
    """True if the message has been deleted."""

    is_hidden: Optional[bool] = FieldInfo(alias="isHidden", default=None)
    """True if the message is hidden from normal display."""

    is_sender: Optional[bool] = FieldInfo(alias="isSender", default=None)
    """True if the authenticated user sent the message."""

    is_unread: Optional[bool] = FieldInfo(alias="isUnread", default=None)
    """True if the message is unread for the authenticated user. May be omitted."""

    linked_message_id: Optional[str] = FieldInfo(alias="linkedMessageID", default=None)
    """ID of the message this is a reply to, if any."""

    links: Optional[List[LinkPreview]] = None
    """Link previews included with this message, if any."""

    mentions: Optional[List[str]] = None
    """
    Mentioned user IDs, @room, or null for legacy messages that require text
    scanning.
    """

    reactions: Optional[List[Reaction]] = None
    """Reactions to the message, if any."""

    seen: Union[bool, datetime, Dict[str, Union[bool, datetime]], None] = None
    """Read receipt state for this message, when available."""

    sender_name: Optional[str] = FieldInfo(alias="senderName", default=None)
    """Resolved sender display name."""

    send_status: Optional[SendStatus] = FieldInfo(alias="sendStatus", default=None)
    """Message send status for this message, when reported by the bridge."""

    text: Optional[str] = None
    """Rich-text message body if present."""

    type: Optional[
        Literal["TEXT", "NOTICE", "IMAGE", "VIDEO", "VOICE", "AUDIO", "FILE", "STICKER", "LOCATION", "REACTION"]
    ] = None
    """Message content type.

    Useful for distinguishing reactions, media messages, and state events from
    regular text messages.
    """
