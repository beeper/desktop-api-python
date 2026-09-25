# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .account import Account
from .._models import BaseModel

__all__ = ["Bridge"]


class Bridge(BaseModel):
    """Available bridge that can connect or reconnect chat accounts."""

    id: str
    """Bridge ID. Use with bridge endpoints."""

    accounts: List[Account]
    """Connected accounts for this bridge.

    Uses the same Account schema as GET /v1/accounts.
    """

    active_account_count: int = FieldInfo(alias="activeAccountCount")
    """Number of active accounts for this network on this device."""

    display_name: str = FieldInfo(alias="displayName")
    """Human-friendly bridge name shown in Beeper."""

    provider: Literal["cloud", "self-hosted", "local", "platform-sdk"]
    """Where accounts for this bridge run: on this device or in Beeper Cloud."""

    status: Literal["available", "connected", "limit_reached", "temporarily_unavailable", "disabled"]
    """Whether this bridge can currently be used to connect new accounts."""

    supports_multiple_accounts: bool = FieldInfo(alias="supportsMultipleAccounts")
    """Whether this bridge can have multiple active accounts for the same network."""

    type: str
    """
    Underlying bridge type, such as matrix, discordgo, slackgo, whatsapp, telegram,
    or twitter.
    """

    network: Optional[str] = None
    """Network grouping used for account counts and limits."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Human-friendly status text matching Beeper account management language."""
