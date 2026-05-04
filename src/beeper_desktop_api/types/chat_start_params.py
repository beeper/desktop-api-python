# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChatStartParams", "User"]


class ChatStartParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]
    """Account to create or start the chat on."""

    user: Required[User]
    """Merged user-like contact payload used to resolve the best identifier."""

    allow_invite: Annotated[bool, PropertyInfo(alias="allowInvite")]
    """Whether invite-based DM creation is allowed when required by the platform."""

    message_text: Annotated[str, PropertyInfo(alias="messageText")]
    """Optional first message content if the platform requires it to create the chat."""


class User(TypedDict, total=False):
    """Merged user-like contact payload used to resolve the best identifier."""

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
