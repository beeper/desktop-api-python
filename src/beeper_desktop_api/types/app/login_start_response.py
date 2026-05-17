# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LoginStartResponse"]


class LoginStartResponse(BaseModel):
    setup_request_id: str = FieldInfo(alias="setupRequestID")
    """Setup request ID to use in the next sign-in step."""

    sign_in_methods: List[str] = FieldInfo(alias="signInMethods")
    """Available sign-in methods for this setup request."""
