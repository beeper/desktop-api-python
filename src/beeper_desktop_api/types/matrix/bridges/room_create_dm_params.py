# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RoomCreateDmParams"]


class RoomCreateDmParams(TypedDict, total=False):
    bridge_id: Required[Annotated[str, PropertyInfo(alias="bridgeID")]]

    login_id: str
    """An optional explicit login ID to do the action through."""
