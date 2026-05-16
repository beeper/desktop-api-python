# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["RoomCreateGroupResponse"]


class RoomCreateGroupResponse(BaseModel):
    """A successfully created group chat."""

    id: str
    """The internal chat ID of the created group."""

    mxid: str
    """The Matrix room ID of the portal."""
