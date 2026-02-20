# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ChatCreateParams", "Chat", "ChatUser"]


class ChatCreateParams(TypedDict, total=False):
    chat: Required[Chat]


class ChatUser(TypedDict, total=False):
    """Required when mode='start'.

    Merged user-like contact payload used to resolve the best identifier.
    """

    id: str
    """Known user ID when available."""

    email: str
    """Email candidate."""

    full_name: Annotated[str, PropertyInfo(alias="fullName")]
    """Display name hint used for ranking only."""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Phone number candidate (E.164 preferred)."""

    username: str
    """Username/handle candidate."""


class Chat(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]
    """Account to create or start the chat on."""

    allow_invite: Annotated[bool, PropertyInfo(alias="allowInvite")]
    """Whether invite-based DM creation is allowed when required by the platform.

    Used for mode='start'.
    """

    message_text: Annotated[str, PropertyInfo(alias="messageText")]
    """Optional first message content if the platform requires it to create the chat."""

    mode: Literal["create", "start"]
    """Operation mode. Defaults to 'create' when omitted."""

    participant_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="participantIDs")]
    """Required when mode='create'. User IDs to include in the new chat."""

    title: str
    """
    Optional title for group chats when mode='create'; ignored for single chats on
    most platforms.
    """

    type: Literal["single", "group"]
    """Required when mode='create'.

    'single' requires exactly one participantID; 'group' supports multiple
    participants and optional title.
    """

    user: ChatUser
    """Required when mode='start'.

    Merged user-like contact payload used to resolve the best identifier.
    """
