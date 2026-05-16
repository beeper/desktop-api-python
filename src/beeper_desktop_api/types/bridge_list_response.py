# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .bridge_availability import BridgeAvailability

__all__ = ["BridgeListResponse"]


class BridgeListResponse(BaseModel):
    """Bridge-backed account types and their connected accounts."""

    items: List[BridgeAvailability]
