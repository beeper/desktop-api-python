# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .reaction import Reaction
from ..._models import BaseModel
from .attachment import Attachment

__all__ = ["Message", "Link", "LinkImgSize", "SendStatus"]


class LinkImgSize(BaseModel):
    """Preview image dimensions."""

    height: Optional[float] = None

    width: Optional[float] = None


class Link(BaseModel):
    """Link preview included with a message."""

    title: str
    """Link preview title."""

    url: str
    """Resolved link URL."""

    favicon: Optional[str] = None
    """Favicon URL if available.

    May be temporary or local-only to this device; download promptly if durable
    access is needed.
    """

    img: Optional[str] = None
    """Preview image URL if available.

    May be temporary or local-only to this device; download promptly if durable
    access is needed.
    """

    img_size: Optional[LinkImgSize] = FieldInfo(alias="imgSize", default=None)
    """Preview image dimensions."""

    original_url: Optional[str] = FieldInfo(alias="originalURL", default=None)
    """Original URL when the displayed URL is shortened or redirected."""

    summary: Optional[str] = None
    """Link preview summary."""


class SendStatus(BaseModel):
    """Message send status for this message, when reported by the bridge."""

    status: Literal["SUCCESS", "PENDING", "FAIL_RETRIABLE", "FAIL_PERMANENT"]
    """Current status of the message send attempt."""

    timestamp: datetime
    """Timestamp for the send status event."""

    delivered_to_users: Optional[List[str]] = FieldInfo(alias="deliveredToUsers", default=None)
    """User IDs the message was delivered to, when reported by the network."""

    internal_error: Optional[str] = FieldInfo(alias="internalError", default=None)
    """Internal bridge error detail. Intended for diagnostics, not end-user display."""

    message: Optional[str] = None
    """Human-readable send status or failure message."""

    reason: Optional[str] = None
    """Machine-readable failure reason. Present when the send status is a failure."""


class Message(BaseModel):
    id: str
    """Message ID."""

    account_id: str = FieldInfo(alias="accountID")
    """Beeper account ID the message belongs to."""

    chat_id: str = FieldInfo(alias="chatID")
    """Chat ID.

    Input routes also accept the local chat ID from this Beeper Desktop installation
    when available.
    """

    sender_id: str = FieldInfo(alias="senderID")
    """
    Matrix-style fully-qualified sender user ID, usually including a bridge prefix
    and homeserver.
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

    links: Optional[List[Link]] = None
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
    """
    Resolved sender display name (impersonator/full name/username/participant name).
    """

    send_status: Optional[SendStatus] = FieldInfo(alias="sendStatus", default=None)
    """Message send status for this message, when reported by the bridge."""

    text: Optional[str] = None
    """Matrix HTML body if present."""

    type: Optional[
        Literal["TEXT", "NOTICE", "IMAGE", "VIDEO", "VOICE", "AUDIO", "FILE", "STICKER", "LOCATION", "REACTION"]
    ] = None
    """Message content type.

    Useful for distinguishing reactions, media messages, and state events from
    regular text messages.
    """
