# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    chat_id: Required[Annotated[str, PropertyInfo(alias="chatID")]]
    """The chat ID to list messages from"""

    cursor: str
    """Message cursor for pagination. Use with direction to navigate results."""

    direction: Literal["after", "before"]
    """
    Pagination direction used with 'cursor': 'before' fetches older messages,
    'after' fetches newer messages. Defaults to 'before' when only 'cursor' is
    provided.
    """

    limit: int
    """Maximum number of messages to return (1–500). Defaults to 50."""
