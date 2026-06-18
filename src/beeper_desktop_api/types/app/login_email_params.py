# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LoginEmailParams"]


class LoginEmailParams(TypedDict, total=False):
    email: Required[str]
    """Email address to send the sign-in code to."""

    setup_request_id: Required[Annotated[str, PropertyInfo(alias="setupRequestID")]]
    """Setup request ID returned by the start step."""
