# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CookieField"]


class CookieField(BaseModel):
    id: str
    """Field ID to send back in the fields object."""

    name: Optional[str] = None
    """Cookie, header, or local storage key to collect."""

    type: Optional[Literal["cookie", "header", "local_storage"]] = None
    """Browser storage source for this value."""
