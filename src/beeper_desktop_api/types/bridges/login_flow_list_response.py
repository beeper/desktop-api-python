# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..login_flow import LoginFlow

__all__ = ["LoginFlowListResponse"]


class LoginFlowListResponse(BaseModel):
    items: List[LoginFlow]
