# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .label import Label
from .._models import BaseModel
from .shared.user import User
from .shared.chat_draft import ChatDraft
from .shared.chat_capabilities import ChatCapabilities

__all__ = ["Chat", "Participants", "ParticipantsItem", "Merge", "Reminder", "Snooze"]


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


class Merge(BaseModel):
    """
    Present when this chat is a merged chat: one person whose conversations across networks (or across accounts on the same network) are grouped into a single chat. A merged chat holds no messages of its own - read messages from the member chats, and send either to a member directly or to the merged chat ID to route automatically.
    """

    chat_ids: List[str] = FieldInfo(alias="chatIDs")
    """Chat IDs of the member chats grouped by this merged chat."""

    default_chat_id: Optional[str] = FieldInfo(alias="defaultChatID", default=None)
    """
    Member chat that receives messages sent to the merged chat, when the user has
    picked one. This preference is per-device; when absent, sends route to the most
    recently active member.
    """


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

    capabilities: Optional[ChatCapabilities] = None
    """Chat capabilities reported by the platform."""

    description: Optional[str] = None
    """Group chat description/topic when available."""

    draft: Optional[ChatDraft] = None
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

    labels: Optional[List[Label]] = None
    """Labels applied to this chat.

    Absent when the chat has none, or when labels are not enabled for this user.
    """

    last_activity: Optional[datetime] = FieldInfo(alias="lastActivity", default=None)
    """Timestamp of last activity."""

    last_read_message_sort_key: Optional[str] = FieldInfo(alias="lastReadMessageSortKey", default=None)
    """Last read message sortKey."""

    local_chat_id: Optional[str] = FieldInfo(alias="localChatID", default=None)
    """Local chat ID specific to this installation."""

    merge: Optional[Merge] = None
    """
    Present when this chat is a merged chat: one person whose conversations across
    networks (or across accounts on the same network) are grouped into a single
    chat. A merged chat holds no messages of its own - read messages from the member
    chats, and send either to a member directly or to the merged chat ID to route
    automatically.
    """

    merged_into_chat_id: Optional[str] = FieldInfo(alias="mergedIntoChatID", default=None)
    """When this chat is a member of a merged chat, the ID of that merged chat.

    Clients that render merged chats as one conversation should list the merged chat
    and hide chats carrying this field.
    """

    message_expiry_seconds: Optional[int] = FieldInfo(alias="messageExpirySeconds", default=None)
    """Disappearing-message timer in seconds when available."""

    reminder: Optional[Reminder] = None
    """Current reminder for this chat, or null when no reminder is set."""

    snooze: Optional[Snooze] = None
    """Current snooze state for this chat, or null when no snooze is set."""

    unread_mentions_count: Optional[int] = FieldInfo(alias="unreadMentionsCount", default=None)
    """Number of unread messages that mention the authenticated user or @room."""
