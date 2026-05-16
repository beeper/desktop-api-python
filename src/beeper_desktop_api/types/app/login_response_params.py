# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoginResponseParams"]


class LoginResponseParams(TypedDict, total=False):
    request: Required[str]
    """Login request ID returned by the start step."""

    response: Required[str]
    """Sign-in code from the user email."""
