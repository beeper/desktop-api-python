# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Label"]


class Label(BaseModel):
    """A user-created label that organizes chats across accounts."""

    id: str
    """Unique identifier of the label."""

    name: str
    """Display name of the label."""
