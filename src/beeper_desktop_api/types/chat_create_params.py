# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ChatCreateParams", "User"]


class ChatCreateParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]
    """Account to create or start the chat on."""

    allow_invite: Annotated[bool, PropertyInfo(alias="allowInvite")]
    """Only used for mode='start'.

    Whether invite-based DM creation is allowed when required by the platform.
    """

    message_text: Annotated[str, PropertyInfo(alias="messageText")]
    """Optional first message content if the platform requires it to create the chat."""

    mode: Literal["start", "create"]
    """Operation mode.

    Use 'start' to resolve a user/contact and start a direct chat. Omit or set
    'create' to create a chat directly.
    """

    participant_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="participantIDs")]
    """Required for create mode.

    Provide exactly one user ID for 'single' chats and one or more for 'group'
    chats.
    """

    title: str
    """Optional title for group chats; ignored for single chats on most networks."""

    type: Literal["single", "group"]
    """Required for create mode.

    'single' creates a direct message chat; 'group' creates a group chat.
    """

    user: User
    """Required for mode='start'.

    Merged user-like contact payload used to resolve the best identifier.
    """


class User(TypedDict, total=False):
    """Required for mode='start'.

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
