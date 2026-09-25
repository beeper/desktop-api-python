# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..bridge_login import BridgeLogin

__all__ = ["LoginListResponse"]


class LoginListResponse(BaseModel):
    items: List[BridgeLogin]
