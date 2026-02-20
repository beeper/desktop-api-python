# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReactionAddParams"]


class ReactionAddParams(TypedDict, total=False):
    chat_id: Required[Annotated[str, PropertyInfo(alias="chatID")]]
    """Unique identifier of the chat."""

    reaction_key: Required[Annotated[str, PropertyInfo(alias="reactionKey")]]
    """Reaction key to add (emoji, shortcode, or custom emoji key)"""

    transaction_id: Annotated[str, PropertyInfo(alias="transactionID")]
    """Optional transaction ID for deduplication and local echo tracking"""
