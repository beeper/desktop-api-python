# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user import User

__all__ = [
    "Chat",
    "Participants",
    "ParticipantsItem",
    "Capabilities",
    "CapabilitiesAttachments",
    "CapabilitiesDisappearingTimer",
    "CapabilitiesMessageRequest",
    "CapabilitiesParticipantActions",
    "CapabilitiesState",
    "CapabilitiesStateAvatar",
    "CapabilitiesStateDescription",
    "CapabilitiesStateDisappearingTimer",
    "CapabilitiesStateTitle",
    "Draft",
    "DraftAttachments",
    "DraftAttachmentsSize",
    "Reminder",
    "Snooze",
]


class ParticipantsItem(User):
    """A chat participant. Extends User with chat membership metadata."""

    is_admin: Optional[bool] = FieldInfo(alias="isAdmin", default=None)
    """True if this participant has admin privileges in the chat."""

    is_network_bot: Optional[bool] = FieldInfo(alias="isNetworkBot", default=None)
    """True if this participant represents an automated network account."""

    is_pending: Optional[bool] = FieldInfo(alias="isPending", default=None)
    """True if this participant has been invited but has not joined yet."""


class Participants(BaseModel):
    """Chat participants information."""

    has_more: bool = FieldInfo(alias="hasMore")
    """True if there are more participants than included in items."""

    items: List[ParticipantsItem]
    """Participants returned for this chat (limited by the request; may be a subset)."""

    total: int
    """Total number of participants in the chat."""


class CapabilitiesAttachments(BaseModel):
    """Capabilities for one attachment message type."""

    mime_types: Dict[str, Literal[-2, -1, 0, 1, 2]] = FieldInfo(alias="mimeTypes")
    """Supported MIME types or MIME patterns for this file message type.

    Missing MIME types should be treated as rejected.
    """

    caption: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    max_caption_length: Optional[int] = FieldInfo(alias="maxCaptionLength", default=None)
    """Maximum caption length when captions are supported."""

    max_duration: Optional[int] = FieldInfo(alias="maxDuration", default=None)
    """Maximum audio or video duration in seconds."""

    max_height: Optional[int] = FieldInfo(alias="maxHeight", default=None)
    """Maximum image or video height in pixels."""

    max_size: Optional[int] = FieldInfo(alias="maxSize", default=None)
    """Maximum file size in bytes."""

    max_width: Optional[int] = FieldInfo(alias="maxWidth", default=None)
    """Maximum image or video width in pixels."""

    view_once: Optional[bool] = FieldInfo(alias="viewOnce", default=None)
    """True if this file type can be sent as view-once media."""


class CapabilitiesDisappearingTimer(BaseModel):
    """Disappearing-message timer capabilities."""

    omit_empty_timer: Optional[bool] = FieldInfo(alias="omitEmptyTimer", default=None)
    """True if empty timer objects should be omitted from message content."""

    timers: Optional[List[int]] = None
    """Allowed disappearing timer values in milliseconds.

    Omitted means any timer is allowed.
    """

    types: Optional[List[Literal["afterRead", "afterSend"]]] = None
    """Supported disappearing timer types."""


class CapabilitiesMessageRequest(BaseModel):
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


class CapabilitiesParticipantActions(BaseModel):
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


class CapabilitiesStateAvatar(BaseModel):
    """Chat avatar state capability."""

    level: Literal[-2, -1, 0, 1, 2]
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class CapabilitiesStateDescription(BaseModel):
    """Chat description/topic state capability."""

    level: Literal[-2, -1, 0, 1, 2]
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class CapabilitiesStateDisappearingTimer(BaseModel):
    """Disappearing-message timer state capability."""

    level: Literal[-2, -1, 0, 1, 2]
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class CapabilitiesStateTitle(BaseModel):
    """Chat title state capability."""

    level: Literal[-2, -1, 0, 1, 2]
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class CapabilitiesState(BaseModel):
    """Chat state update capabilities."""

    avatar: Optional[CapabilitiesStateAvatar] = None
    """Chat avatar state capability."""

    description: Optional[CapabilitiesStateDescription] = None
    """Chat description/topic state capability."""

    disappearing_timer: Optional[CapabilitiesStateDisappearingTimer] = FieldInfo(
        alias="disappearingTimer", default=None
    )
    """Disappearing-message timer state capability."""

    title: Optional[CapabilitiesStateTitle] = None
    """Chat title state capability."""


class Capabilities(BaseModel):
    """Chat capabilities reported by the platform."""

    allowed_reactions: Optional[List[str]] = FieldInfo(alias="allowedReactions", default=None)
    """Allowed Unicode reactions. Omitted means all emoji reactions are allowed."""

    archive: Optional[bool] = None
    """True if archive/unarchive is supported."""

    attachments: Optional[Dict[str, CapabilitiesAttachments]] = None
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

    disappearing_timer: Optional[CapabilitiesDisappearingTimer] = FieldInfo(alias="disappearingTimer", default=None)
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

    message_request: Optional[CapabilitiesMessageRequest] = FieldInfo(alias="messageRequest", default=None)
    """Message request capabilities."""

    participant_actions: Optional[CapabilitiesParticipantActions] = FieldInfo(alias="participantActions", default=None)
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

    state: Optional[CapabilitiesState] = None
    """Chat state update capabilities."""

    thread: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    typing_notifications: Optional[bool] = FieldInfo(alias="typingNotifications", default=None)
    """True if typing notifications are supported."""


class DraftAttachmentsSize(BaseModel):
    """Pixel dimensions of the attachment."""

    height: Optional[float] = None

    width: Optional[float] = None


class DraftAttachments(BaseModel):
    id: str
    """Draft attachment identifier."""

    type: Literal["file", "gif", "recorded_audio"]
    """Draft attachment type. GIF and recorded audio are mutually exclusive types."""

    audio_duration_seconds: Optional[float] = FieldInfo(alias="audioDurationSeconds", default=None)
    """Audio duration in seconds if known."""

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)
    """Original filename if available."""

    file_path: Optional[str] = FieldInfo(alias="filePath", default=None)
    """Local filesystem path for the draft attachment."""

    file_size: Optional[float] = FieldInfo(alias="fileSize", default=None)
    """File size in bytes if known."""

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """MIME type if known."""

    size: Optional[DraftAttachmentsSize] = None
    """Pixel dimensions of the attachment."""

    sticker_id: Optional[str] = FieldInfo(alias="stickerID", default=None)
    """Sticker identifier if the draft attachment is a sticker."""


class Draft(BaseModel):
    """Current draft object for this chat, or null when no draft is set."""

    text: str
    """Rich-text draft body as returned by Beeper."""

    attachments: Optional[Dict[str, DraftAttachments]] = None
    """Draft attachments keyed by attachment ID."""


class Reminder(BaseModel):
    """Current reminder for this chat, or null when no reminder is set."""

    dismiss_on_incoming_message: Optional[bool] = FieldInfo(alias="dismissOnIncomingMessage", default=None)
    """Cancel reminder if someone messages in the chat."""

    remind_at: Optional[datetime] = FieldInfo(alias="remindAt", default=None)
    """Timestamp when the reminder should trigger."""


class Snooze(BaseModel):
    """Current snooze state for this chat, or null when no snooze is set."""

    snooze_until: Optional[datetime] = FieldInfo(alias="snoozeUntil", default=None)
    """Timestamp when the snooze expires."""

    user_snoozed_at: Optional[datetime] = FieldInfo(alias="userSnoozedAt", default=None)
    """Timestamp when the user set the snooze."""


class Chat(BaseModel):
    id: str
    """Unique identifier of the chat across Beeper."""

    account_id: str = FieldInfo(alias="accountID")
    """Account ID this chat belongs to."""

    network: str
    """Display-only human-readable account/network name."""

    participants: Participants
    """Chat participants information."""

    title: str
    """Display title of the chat as computed by the client/server."""

    type: Literal["single", "group"]
    """Chat type: 'single' for direct messages, 'group' for group chats."""

    unread_count: int = FieldInfo(alias="unreadCount")
    """Number of unread messages."""

    capabilities: Optional[Capabilities] = None
    """Chat capabilities reported by the platform."""

    description: Optional[str] = None
    """Group chat description/topic when available."""

    draft: Optional[Draft] = None
    """Current draft object for this chat, or null when no draft is set."""

    img_url: Optional[str] = FieldInfo(alias="imgURL", default=None)
    """Local filesystem path to the chat avatar image when available."""

    is_archived: Optional[bool] = FieldInfo(alias="isArchived", default=None)
    """True if chat is archived."""

    is_low_priority: Optional[bool] = FieldInfo(alias="isLowPriority", default=None)
    """True if chat is marked low priority."""

    is_marked_unread: Optional[bool] = FieldInfo(alias="isMarkedUnread", default=None)
    """True if the chat was explicitly marked unread by the authenticated user."""

    is_muted: Optional[bool] = FieldInfo(alias="isMuted", default=None)
    """True if chat notifications are muted."""

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)
    """True if chat is pinned."""

    is_read_only: Optional[bool] = FieldInfo(alias="isReadOnly", default=None)
    """True if messages cannot be sent in this chat."""

    last_activity: Optional[datetime] = FieldInfo(alias="lastActivity", default=None)
    """Timestamp of last activity."""

    last_read_message_sort_key: Optional[str] = FieldInfo(alias="lastReadMessageSortKey", default=None)
    """Last read message sortKey."""

    local_chat_id: Optional[str] = FieldInfo(alias="localChatID", default=None)
    """Local chat ID specific to this installation."""

    message_expiry_seconds: Optional[int] = FieldInfo(alias="messageExpirySeconds", default=None)
    """Disappearing-message timer in seconds when available."""

    reminder: Optional[Reminder] = None
    """Current reminder for this chat, or null when no reminder is set."""

    snooze: Optional[Snooze] = None
    """Current snooze state for this chat, or null when no snooze is set."""

    unread_mentions_count: Optional[int] = FieldInfo(alias="unreadMentionsCount", default=None)
    """Number of unread messages that mention the authenticated user or @room."""
