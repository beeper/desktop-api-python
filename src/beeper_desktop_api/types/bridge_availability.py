# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .account import Account
from .._models import BaseModel

__all__ = ["BridgeAvailability", "Bridge"]


class Bridge(BaseModel):
    """Bridge metadata for the account. Available in Beeper Desktop v4.2.785+."""

    id: str
    """Bridge instance identifier.

    Matrix and cloud bridges often use the bridge type (for example matrix or
    discordgo); local bridges use a local bridge ID (for example local-whatsapp).
    Available in Beeper Desktop v4.2.785+.
    """

    provider: Literal["cloud", "self-hosted", "local", "platform-sdk"]
    """Bridge provider for the account. Available in Beeper Desktop v4.2.785+."""

    type: str
    """Bridge type, such as matrix, discordgo, slackgo, whatsapp, telegram, or twitter.

    Available in Beeper Desktop v4.2.785+.
    """


class BridgeAvailability(BaseModel):
    """Bridge-backed account type that can be shown in add-account flows."""

    accounts: List[Account]
    """Connected accounts for this bridge.

    Uses the same Account schema as GET /v1/accounts.
    """

    active_account_count: int = FieldInfo(alias="activeAccountCount")
    """Number of active accounts for this network on this device."""

    bridge: Bridge
    """Bridge metadata for the account. Available in Beeper Desktop v4.2.785+."""

    display_name: str = FieldInfo(alias="displayName")
    """Human-friendly account type name shown in Beeper Desktop."""

    login_mode: str = FieldInfo(alias="loginMode")
    """Login mode used by Beeper Desktop for this bridge."""

    status: Literal["available", "connected", "limit_reached", "temporarily_unavailable"]
    """Whether this bridge can currently be used to add an account."""

    network: Optional[str] = None
    """Network grouping used for account counts and limits."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Human-friendly status text matching Beeper Desktop account management language."""
