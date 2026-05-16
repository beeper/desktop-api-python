# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuthStartLoginParams"]


class AuthStartLoginParams(TypedDict, total=False):
    bridge_id: Required[Annotated[str, PropertyInfo(alias="bridgeID")]]

    login_id: str
    """An existing login ID to re-login as.

    If this is specified and the user logs into a different account, the provided ID
    will be logged out.
    """
