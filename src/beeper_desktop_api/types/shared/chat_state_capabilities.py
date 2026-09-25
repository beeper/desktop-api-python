# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ChatStateCapabilities", "Avatar", "Description", "DisappearingTimer", "Title"]


class Avatar(BaseModel):
    """Chat avatar state capability."""

    level: Literal[-2, -1, 0, 1, 2]
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class Description(BaseModel):
    """Chat description/topic state capability."""

    level: Literal[-2, -1, 0, 1, 2]
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class DisappearingTimer(BaseModel):
    """Disappearing-message timer state capability."""

    level: Literal[-2, -1, 0, 1, 2]
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class Title(BaseModel):
    """Chat title state capability."""

    level: Literal[-2, -1, 0, 1, 2]
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """


class ChatStateCapabilities(BaseModel):
    """Chat state update capabilities."""

    avatar: Optional[Avatar] = None
    """Chat avatar state capability."""

    description: Optional[Description] = None
    """Chat description/topic state capability."""

    disappearing_timer: Optional[DisappearingTimer] = FieldInfo(alias="disappearingTimer", default=None)
    """Disappearing-message timer state capability."""

    title: Optional[Title] = None
    """Chat title state capability."""
