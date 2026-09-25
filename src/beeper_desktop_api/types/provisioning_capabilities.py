# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .group_type_capabilities import GroupTypeCapabilities
from .resolve_identifier_capabilities import ResolveIdentifierCapabilities

__all__ = ["ProvisioningCapabilities"]


class ProvisioningCapabilities(BaseModel):
    """Advanced network capabilities for account lookup and group creation."""

    group_creation: Dict[str, GroupTypeCapabilities]

    resolve_identifier: ResolveIdentifierCapabilities
    """Identifier lookup capabilities for this bridge."""

    image_pack_import: Optional[bool] = None
