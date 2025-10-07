# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user import User

__all__ = ["Account"]


class Account(BaseModel):
    account_id: str = FieldInfo(alias="accountID")
    """Chat account added to Beeper. Use this to route account-scoped actions."""

    network: str
    """Display-only human-readable network name (e.g., 'WhatsApp', 'Messenger')."""

    user: User
    """User the account belongs to."""
