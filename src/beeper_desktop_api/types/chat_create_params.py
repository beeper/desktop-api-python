# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ChatCreateParams"]


class ChatCreateParams(TypedDict, total=False):
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

    title: str
    """Optional title for group chats; ignored for single chats on most platforms."""
