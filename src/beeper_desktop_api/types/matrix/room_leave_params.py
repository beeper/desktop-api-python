# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RoomLeaveParams"]


class RoomLeaveParams(TypedDict, total=False):
    reason: str
    """
    Optional reason to be included as the `reason` on the subsequent membership
    event.
    """
