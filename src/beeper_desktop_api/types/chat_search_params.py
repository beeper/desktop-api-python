# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ChatSearchParams"]


class ChatSearchParams(TypedDict, total=False):
    account_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="accountIDs")]
    """Limit results to specific chat accounts."""

    cursor: str
    """Opaque pagination cursor; do not inspect. Use together with 'direction'."""

    direction: Literal["after", "before"]
    """
    Pagination direction used with 'cursor': 'before' fetches older results, 'after'
    fetches newer results. Defaults to 'before' when only 'cursor' is provided.
    """

    inbox: Literal["primary", "low-priority", "archive"]
    """
    Filter by inbox type: "primary" (non-archived, non-low-priority),
    "low-priority", or "archive". If not specified, shows all chats.
    """

    include_muted: Annotated[Optional[bool], PropertyInfo(alias="includeMuted")]
    """Include chats marked as Muted by the user, which are usually less important.

    Default: true. Set to false if the user wants a more refined search.
    """

    last_activity_after: Annotated[Union[str, datetime], PropertyInfo(alias="lastActivityAfter", format="iso8601")]
    """Only include chats with last activity after this ISO 8601 datetime."""

    last_activity_before: Annotated[Union[str, datetime], PropertyInfo(alias="lastActivityBefore", format="iso8601")]
    """Only include chats with last activity before this ISO 8601 datetime."""

    limit: int
    """Set the maximum number of chats to retrieve. Valid range: 1-200, default is 50"""

    query: str
    """Literal chat search.

    Use words the user typed, such as "dinner". When multiple words are provided,
    all must match. Case-insensitive.
    """

    scope: Literal["titles", "participants"]
    """
    Search scope: 'titles' matches title + network; 'participants' matches
    participant names.
    """

    type: Literal["single", "group", "any"]
    """
    Specify the type of chats to retrieve: use "single" for direct messages, "group"
    for group chats, or "any" to get all types
    """

    unread_only: Annotated[Optional[bool], PropertyInfo(alias="unreadOnly")]
    """Set to true to only retrieve chats that have unread messages"""
