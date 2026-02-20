# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ReactionAddResponse"]


class ReactionAddResponse(BaseModel):
    chat_id: str = FieldInfo(alias="chatID")
    """Unique identifier of the chat."""

    message_id: str = FieldInfo(alias="messageID")
    """Message ID."""

    reaction_key: str = FieldInfo(alias="reactionKey")
    """Reaction key that was added"""

    success: Literal[True]
    """Whether the reaction was successfully added"""

    transaction_id: str = FieldInfo(alias="transactionID")
    """Transaction ID used for the reaction event"""
