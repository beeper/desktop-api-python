# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RoomCreateResponse"]


class RoomCreateResponse(BaseModel):
    """Information about the newly created room."""

    room_id: str
    """The created room's ID."""
