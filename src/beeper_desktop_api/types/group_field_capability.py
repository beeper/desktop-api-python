# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .disappearing_timer_capability import DisappearingTimerCapability

__all__ = ["GroupFieldCapability"]


class GroupFieldCapability(BaseModel):
    """Group creation field capability."""

    allowed: bool

    max_length: Optional[int] = None

    min_length: Optional[int] = None

    required: Optional[bool] = None

    settings: Optional[DisappearingTimerCapability] = None
    """Disappearing-message timer capability."""
