# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user import User

__all__ = ["Account", "Bridge"]


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


class Account(BaseModel):
    """A chat account added to Beeper."""

    account_id: str = FieldInfo(alias="accountID")
    """Chat account added to Beeper.

    Use this to route account-scoped actions. Examples include matrix for
    Beeper/Matrix, discordgo for a cloud bridge, slackgo.TEAM-USER for
    workspace-scoped cloud bridges, and local-whatsapp*ba*... for local bridges.
    """

    bridge: Bridge
    """Bridge metadata for the account. Available in Beeper Desktop v4.2.785+."""

    user: User
    """User the account belongs to."""

    network: Optional[str] = None
    """Human-friendly network name for the account.

    Omitted when the network is unknown.
    """
