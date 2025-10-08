# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    cursor: str
    """Message cursor for pagination. Use with direction to navigate results."""

    direction: Literal["after", "before"]
    """
    Pagination direction used with 'cursor': 'before' fetches older messages,
    'after' fetches newer messages. Defaults to 'before' when only 'cursor' is
    provided.
    """
