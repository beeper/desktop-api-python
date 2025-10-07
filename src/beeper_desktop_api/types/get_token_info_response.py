# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GetTokenInfoResponse"]


class GetTokenInfoResponse(BaseModel):
    iat: float
    """Issued at timestamp (Unix epoch seconds)"""

    scope: str
    """Granted scopes"""

    sub: str
    """Subject identifier (token ID)"""

    token_use: Literal["access"]
    """Token type"""

    aud: Optional[str] = None
    """Audience (client ID)"""

    client_id: Optional[str] = None
    """Client identifier"""

    exp: Optional[float] = None
    """Expiration timestamp (Unix epoch seconds)"""
