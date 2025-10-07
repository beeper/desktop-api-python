# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ChatListParams"]


class ChatListParams(TypedDict, total=False):
    account_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="accountIDs")]
    """Limit to specific account IDs. If omitted, fetches from all accounts."""

    cursor: str
    """Timestamp cursor (milliseconds since epoch) for pagination.

    Use with direction to navigate results.
    """

    direction: Literal["after", "before"]
    """
    Pagination direction used with 'cursor': 'before' fetches older results, 'after'
    fetches newer results. Defaults to 'before' when only 'cursor' is provided.
    """

    limit: int
    """Maximum number of chats to return (1–200). Defaults to 50."""
