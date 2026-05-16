# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["UserResolveResponse"]


class UserResolveResponse(BaseModel):
    """A successfully resolved identifier."""

    id: str
    """The internal user ID of the resolved user."""

    avatar_url: Optional[str] = None
    """The avatar of the user on the remote network."""

    dm_room_mxid: Optional[str] = None
    """The Matrix room ID of the direct chat with the user."""

    identifiers: Optional[List[str]] = None
    """A list of identifiers for the user on the remote network."""

    mxid: Optional[str] = None
    """The Matrix user ID of the ghost representing the user."""

    name: Optional[str] = None
    """The name of the user on the remote network."""
