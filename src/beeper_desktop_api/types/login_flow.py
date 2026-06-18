# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LoginFlow"]


class LoginFlow(BaseModel):
    """Connect or reconnect flow option for a bridge."""

    id: str
    """Flow ID to pass when creating a bridge login session."""

    description: Optional[str] = None
    """Short explanation for when to use this flow, when provided."""

    name: Optional[str] = None
    """Display name for the flow, when provided."""
