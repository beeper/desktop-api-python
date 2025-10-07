# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactSearchParams"]


class ContactSearchParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]
    """Account ID this resource belongs to."""

    query: Required[str]
    """Text to search users by. Network-specific behavior."""
