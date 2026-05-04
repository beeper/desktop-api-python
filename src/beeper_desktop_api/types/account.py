# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user import User

__all__ = ["Account", "Bridge"]


class Bridge(BaseModel):
    """Bridge metadata for the account. Available in Beeper Desktop v4.2.799+."""

    id: str
    """Bridge instance identifier. Available in Beeper Desktop v4.2.799+."""

    provider: Literal["cloud", "self-hosted", "local", "platform-sdk"]
    """Bridge provider for the account. Available in Beeper Desktop v4.2.799+."""

    type: str
    """Bridge type. Available in Beeper Desktop v4.2.799+."""


class Account(BaseModel):
    """A chat account added to Beeper."""

    account_id: str = FieldInfo(alias="accountID")
    """Chat account added to Beeper. Use this to route account-scoped actions."""

    bridge: Bridge
    """Bridge metadata for the account. Available in Beeper Desktop v4.2.799+."""

    user: User
    """User the account belongs to."""

    network: Optional[str] = None
    """Human-friendly network name for the account.

    Omitted when the network is unknown.
    """
