# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ReactionAddResponse"]


class ReactionAddResponse(BaseModel):
    chat_id: str = FieldInfo(alias="chatID")
    """Chat ID.

    Input routes also accept the local chat ID from this installation when
    available.
    """

    message_id: str = FieldInfo(alias="messageID")
    """Message ID."""

    reaction_key: str = FieldInfo(alias="reactionKey")
    """Reaction key that was added."""

    success: Literal[True]
    """Always true.

    Indicates the reaction was queued; failures return an error response.
    """

    transaction_id: str = FieldInfo(alias="transactionID")
    """Transaction ID used for send tracking."""
