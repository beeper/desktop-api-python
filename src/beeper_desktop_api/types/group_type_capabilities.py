# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .group_field_capability import GroupFieldCapability

__all__ = ["GroupTypeCapabilities"]


class GroupTypeCapabilities(BaseModel):
    """Group creation capabilities for one group type."""

    type_description: str

    avatar: Optional[GroupFieldCapability] = None
    """Group creation field capability."""

    disappear: Optional[GroupFieldCapability] = None
    """Group creation field capability."""

    name: Optional[GroupFieldCapability] = None
    """Group creation field capability."""

    parent: Optional[GroupFieldCapability] = None
    """Group creation field capability."""

    participants: Optional[GroupFieldCapability] = None
    """Group creation field capability."""

    topic: Optional[GroupFieldCapability] = None
    """Group creation field capability."""

    username: Optional[GroupFieldCapability] = None
    """Group creation field capability."""
