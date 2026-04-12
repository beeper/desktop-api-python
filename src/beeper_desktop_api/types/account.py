# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user import User

__all__ = ["Account", "Bridge"]


class Bridge(BaseModel):
    """Bridge metadata for the account. Available from Beeper Desktop v.4.2.719+."""

    id: str
    """Bridge instance identifier."""

    provider: Literal["cloud", "self-hosted", "local", "platform-sdk"]
    """Bridge provider for the account."""

    type: str
    """Bridge type."""


class Account(BaseModel):
    """A chat account added to Beeper"""

    account_id: str = FieldInfo(alias="accountID")
    """Chat account added to Beeper. Use this to route account-scoped actions."""

    bridge: Bridge
    """Bridge metadata for the account. Available from Beeper Desktop v.4.2.719+."""

    network: str
    """Human-friendly network name for the account."""

    user: User
    """User the account belongs to."""
