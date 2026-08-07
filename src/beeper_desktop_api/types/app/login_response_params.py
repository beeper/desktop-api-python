# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LoginResponseParams"]


class LoginResponseParams(TypedDict, total=False):
    response: Required[str]
    """Sign-in code from the user email."""

    setup_request_id: Required[Annotated[str, PropertyInfo(alias="setupRequestID")]]
    """Setup request ID returned by the start step."""
