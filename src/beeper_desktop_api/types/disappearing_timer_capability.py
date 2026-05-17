# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DisappearingTimerCapability"]


class DisappearingTimerCapability(BaseModel):
    """Disappearing-message timer capability."""

    types: List[Literal["", "after_read", "after_send"]]

    omit_empty_timer: Optional[Literal[True]] = None

    timers: Optional[List[int]] = None
