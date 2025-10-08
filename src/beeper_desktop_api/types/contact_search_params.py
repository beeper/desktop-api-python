# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContactSearchParams"]


class ContactSearchParams(TypedDict, total=False):
    query: Required[str]
    """Text to search users by. Network-specific behavior."""
