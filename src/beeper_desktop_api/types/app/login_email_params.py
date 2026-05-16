# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LoginEmailParams"]


class LoginEmailParams(TypedDict, total=False):
    email: Required[str]
    """Email address to send the sign-in code to."""

    request: Required[str]
    """Login request ID returned by the start step."""
