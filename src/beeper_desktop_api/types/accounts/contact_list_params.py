# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor; do not inspect. Use together with 'direction'."""

    direction: Literal["after", "before"]
    """
    Pagination direction used with 'cursor': 'before' fetches older results, 'after'
    fetches newer results. Defaults to 'before' when only 'cursor' is provided.
    """

    limit: int
    """Maximum contacts to return per page."""

    query: str
    """Optional search query for blended contact lookup."""
