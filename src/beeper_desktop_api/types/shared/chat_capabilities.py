# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .attachment_capabilities import AttachmentCapabilities
from .chat_state_capabilities import ChatStateCapabilities

__all__ = ["ChatCapabilities", "DisappearingTimer", "MessageRequest", "ParticipantActions"]


class DisappearingTimer(BaseModel):
    """Disappearing-message timer capabilities."""

    omit_empty_timer: Optional[bool] = FieldInfo(alias="omitEmptyTimer", default=None)
    """True if empty timer objects should be omitted from message content."""

    timers: Optional[List[int]] = None
    """Allowed disappearing timer values in milliseconds.

    Omitted means any timer is allowed.
    """

    types: Optional[List[Literal["afterRead", "afterReadByRecipient", "afterSend"]]] = None
    """Supported disappearing timer types."""


class MessageRequest(BaseModel):
    """Message request capabilities."""

    accept_with_button: Optional[Literal[-2, -1, 0, 1, 2]] = FieldInfo(alias="acceptWithButton", default=None)
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    accept_with_message: Optional[Literal[-2, -1, 0, 1, 2]] = FieldInfo(alias="acceptWithMessage", default=None)
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class ParticipantActions(BaseModel):
    """Participant management capabilities."""

    ban: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    invite: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    kick: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    leave: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    revoke_invite: Optional[Literal[-2, -1, 0, 1, 2]] = FieldInfo(alias="revokeInvite", default=None)
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class ChatCapabilities(BaseModel):
    """Chat capabilities reported by the platform."""

    allowed_reactions: Optional[List[str]] = FieldInfo(alias="allowedReactions", default=None)
    """Allowed Unicode reactions. Omitted means all emoji reactions are allowed."""

    archive: Optional[bool] = None
    """True if archive/unarchive is supported."""

    attachments: Optional[Dict[str, AttachmentCapabilities]] = None
    """
    Supported attachment message types and their per-type constraints, keyed by
    Matrix msgtype or pseudo-msgtype (for example m.image, m.video,
    org.matrix.msc3245.voice). Missing message types should be treated as rejected.
    """

    custom_emoji_reactions: Optional[bool] = FieldInfo(alias="customEmojiReactions", default=None)
    """True if custom emoji reactions are supported."""

    delete: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    delete_chat: Optional[bool] = FieldInfo(alias="deleteChat", default=None)
    """True if deleting chats for the authenticated user is supported."""

    delete_chat_for_everyone: Optional[bool] = FieldInfo(alias="deleteChatForEveryone", default=None)
    """True if deleting chats for everyone is supported."""

    delete_for_me: Optional[bool] = FieldInfo(alias="deleteForMe", default=None)
    """True if deleting messages only for the authenticated user is supported."""

    delete_max_age: Optional[int] = FieldInfo(alias="deleteMaxAge", default=None)
    """Maximum message age for delete-for-everyone, in seconds."""

    disappearing_timer: Optional[DisappearingTimer] = FieldInfo(alias="disappearingTimer", default=None)
    """Disappearing-message timer capabilities."""

    edit: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    edit_max_age: Optional[int] = FieldInfo(alias="editMaxAge", default=None)
    """Maximum message age for edits, in seconds."""

    edit_max_count: Optional[int] = FieldInfo(alias="editMaxCount", default=None)
    """Maximum number of edits allowed for one message."""

    formatting: Optional[Dict[str, Literal[-2, -1, 0, 1, 2]]] = None
    """
    Supported rich-text formatting features keyed by feature name (for example bold,
    inline_code, code_block.syntax_highlighting). Omitted means no formatting
    support is advertised.
    """

    location_message: Optional[Literal[-2, -1, 0, 1, 2]] = FieldInfo(alias="locationMessage", default=None)
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    mark_as_unread: Optional[bool] = FieldInfo(alias="markAsUnread", default=None)
    """True if marking chats unread is supported."""

    max_text_length: Optional[int] = FieldInfo(alias="maxTextLength", default=None)
    """Maximum length of normal text messages."""

    message_request: Optional[MessageRequest] = FieldInfo(alias="messageRequest", default=None)
    """Message request capabilities."""

    participant_actions: Optional[ParticipantActions] = FieldInfo(alias="participantActions", default=None)
    """Participant management capabilities."""

    poll: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    reaction: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    reaction_count: Optional[int] = FieldInfo(alias="reactionCount", default=None)
    """Maximum number of reactions allowed on a single message."""

    read_receipts: Optional[bool] = FieldInfo(alias="readReceipts", default=None)
    """True if read receipts are supported."""

    reply: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    state: Optional[ChatStateCapabilities] = None
    """Chat state update capabilities."""

    thread: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    typing_notifications: Optional[bool] = FieldInfo(alias="typingNotifications", default=None)
    """True if typing notifications are supported."""
