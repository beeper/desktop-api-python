# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoginSessionCancelResponse"]


class LoginSessionCancelResponse(BaseModel):
    bridge_id: str = FieldInfo(alias="bridgeID")

    login_session_id: str = FieldInfo(alias="loginSessionID")

    status: Literal["cancelled"]
