# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountBridge"]


class AccountBridge(BaseModel):
    """Bridge metadata for the account. Available in Beeper Desktop v4.2.785+."""

    id: str
    """Bridge identifier.

    Beeper Cloud accounts often use the network type (for example matrix or
    discordgo); on-device accounts use a local bridge ID (for example
    local-whatsapp). Available in Beeper Desktop v4.2.785+.
    """

    provider: Literal["cloud", "self-hosted", "local", "platform-sdk"]
    """Where this account runs: on this device or in Beeper Cloud.

    Available in Beeper Desktop v4.2.785+.
    """

    type: str
    """Bridge type, such as matrix, discordgo, slackgo, whatsapp, telegram, or twitter.

    Available in Beeper Desktop v4.2.785+.
    """
