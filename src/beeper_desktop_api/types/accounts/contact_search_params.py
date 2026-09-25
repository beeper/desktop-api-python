# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContactSearchParams"]


class ContactSearchParams(TypedDict, total=False):
    query: Required[str]
    """Text to search contacts by.

    A phone number, email address, or username written with a leading @ is
    additionally looked up as an exact identifier on the network; any other text,
    such as a bare handle or a person or business name, searches existing contacts
    only. Matching behavior depends on the network.
    """
