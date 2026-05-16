# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["LoginStartResponse"]


class LoginStartResponse(BaseModel):
    request: str
    """Login request ID to use in the next sign-in step."""

    type: List[str]
    """Available sign-in methods for this request."""
