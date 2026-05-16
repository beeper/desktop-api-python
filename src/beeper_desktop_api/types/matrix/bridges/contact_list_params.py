# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    login_id: str
    """An optional explicit login ID to do the action through."""
