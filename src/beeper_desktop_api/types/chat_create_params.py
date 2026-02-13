# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ChatCreateParams", "Variant0", "Variant1", "Variant1User"]


class Variant0(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]
    """Account to create the chat on."""

    participant_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="participantIDs")]]
    """User IDs to include in the new chat."""

    type: Required[Literal["single", "group"]]
    """
    Chat type to create: 'single' requires exactly one participantID; 'group'
    supports multiple participants and optional title.
    """

    message_text: Annotated[str, PropertyInfo(alias="messageText")]
    """Optional first message content if the platform requires it to create the chat."""

    mode: Literal["create"]
    """Create mode. Defaults to 'create' when omitted."""

    title: str
    """Optional title for group chats; ignored for single chats on most platforms."""


class Variant1(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]
    """Account to start the chat on."""

    mode: Required[Literal["start"]]
    """Start mode for resolving/creating a direct chat from merged contact data."""

    user: Required[Variant1User]
    """Merged user-like contact payload used to resolve the best identifier."""

    allow_invite: Annotated[bool, PropertyInfo(alias="allowInvite")]
    """Whether invite-based DM creation is allowed when required by the platform."""

    message_text: Annotated[str, PropertyInfo(alias="messageText")]
    """Optional first message content if the platform requires it to create the chat."""


class Variant1User(TypedDict, total=False):
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


ChatCreateParams: TypeAlias = Union[Variant0, Variant1]
