# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .bridge import Bridge
from .._models import BaseModel

__all__ = ["BridgeListResponse"]


class BridgeListResponse(BaseModel):
    """Available bridges and their connected accounts."""

    items: List[Bridge]
