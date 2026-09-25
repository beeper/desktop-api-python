# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoginRemoveResponse"]


class LoginRemoveResponse(BaseModel):
    bridge_id: str = FieldInfo(alias="bridgeID")

    login_id: str = FieldInfo(alias="loginID")

    scope: Literal["current-device", "all-devices"]
    """Where this bridge login should be removed."""

    status: Literal["removed"]

    affected_account_ids: Optional[List[str]] = FieldInfo(alias="affectedAccountIDs", default=None)
