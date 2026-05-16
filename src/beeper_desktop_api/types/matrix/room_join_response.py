# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RoomJoinResponse"]


class RoomJoinResponse(BaseModel):
    room_id: str
    """The joined room ID."""
