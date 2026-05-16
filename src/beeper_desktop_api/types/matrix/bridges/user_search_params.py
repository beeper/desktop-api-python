# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserSearchParams"]


class UserSearchParams(TypedDict, total=False):
    login_id: str
    """An optional explicit login ID to do the action through."""

    query: str
    """The search query to send to the remote network"""
