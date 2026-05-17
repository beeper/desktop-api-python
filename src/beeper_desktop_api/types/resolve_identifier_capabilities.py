# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ResolveIdentifierCapabilities"]


class ResolveIdentifierCapabilities(BaseModel):
    """Identifier lookup capabilities for this bridge."""

    any_phone: bool

    contact_list: bool

    create_dm: bool

    lookup_email: bool

    lookup_phone: bool

    lookup_username: bool

    search: bool
