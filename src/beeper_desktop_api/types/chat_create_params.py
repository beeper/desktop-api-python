# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ChatCreateParams", "Params", "ParamsUnionMember0", "ParamsUnionMember0User", "ParamsUnionMember1"]


class ChatCreateParams(TypedDict, total=False):
    params: Params


class ParamsUnionMember0User(TypedDict, total=False):
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


class ParamsUnionMember0(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]
    """Account to create or start the chat on."""

    mode: Required[Literal["start"]]
    """Operation mode. Use 'start' to resolve a user/contact and start a direct chat."""

    user: Required[ParamsUnionMember0User]
    """Merged user-like contact payload used to resolve the best identifier."""

    allow_invite: Annotated[bool, PropertyInfo(alias="allowInvite")]
    """Whether invite-based DM creation is allowed when required by the platform.

    Used for mode='start'.
    """

    message_text: Annotated[str, PropertyInfo(alias="messageText")]
    """Optional first message content if the platform requires it to create the chat."""


class ParamsUnionMember1(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]
    """Account to create or start the chat on."""

    participant_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="participantIDs")]]
    """User IDs to include in the new chat."""

    type: Required[Literal["single", "group"]]
    """
    'single' requires exactly one participantID; 'group' supports multiple
    participants and optional title.
    """

    message_text: Annotated[str, PropertyInfo(alias="messageText")]
    """Optional first message content if the platform requires it to create the chat."""

    mode: Literal["create"]
    """Operation mode. Defaults to 'create' when omitted."""

    title: str
    """Optional title for group chats; ignored for single chats on most platforms."""


Params: TypeAlias = Union[ParamsUnionMember0, ParamsUnionMember1]
