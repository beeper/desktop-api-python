# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user import User
from .account_bridge import AccountBridge

__all__ = ["Account"]


class Account(BaseModel):
    """A chat account added to Beeper."""

    account_id: str = FieldInfo(alias="accountID")
    """Chat account added to Beeper.

    Use this to route account-scoped actions. Examples include matrix for
    Beeper/Matrix, discordgo for a cloud bridge, slackgo.TEAM-USER for
    workspace-scoped cloud bridges, and local-whatsapp*ba*... for local bridges.
    """

    bridge: AccountBridge
    """Bridge metadata for the account. Available in Beeper Desktop v4.2.785+."""

    status: Literal[
        "connected",
        "connecting",
        "backfilling",
        "connection_required",
        "reconnect_required",
        "attention_required",
        "disconnected",
        "disabled",
    ]
    """Current connection status for this account."""

    user: User
    """User the account belongs to."""

    capabilities: Optional[Dict[str, Optional[object]]] = None
    """Runtime chat/message capabilities for this connected account, when available."""

    login_id: Optional[str] = FieldInfo(alias="loginID", default=None)
    """Bridge login ID for this account, when known.

    One bridge login can contain multiple chat accounts.
    """

    network: Optional[str] = None
    """Human-friendly network name for the account.

    Omitted when the network is unknown.
    """

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Human-friendly account status text."""
