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
    """
    Provide an array of account IDs to filter chats from specific messaging accounts
    only
    """

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
    """
    Provide an ISO datetime string to only retrieve chats with last activity after
    this time
    """

    last_activity_before: Annotated[Union[str, datetime], PropertyInfo(alias="lastActivityBefore", format="iso8601")]
    """
    Provide an ISO datetime string to only retrieve chats with last activity before
    this time
    """

    limit: int
    """Set the maximum number of chats to retrieve. Valid range: 1-200, default is 50"""

    query: str
    """Literal token search (non-semantic).

    Use single words users type (e.g., "dinner"). When multiple words provided, ALL
    must match. Case-insensitive.
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
