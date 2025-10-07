# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    chat_id: Required[Annotated[str, PropertyInfo(alias="chatID")]]
    """Unique identifier of the chat."""

    reply_to_message_id: Annotated[str, PropertyInfo(alias="replyToMessageID")]
    """Provide a message ID to send this as a reply to an existing message"""

    text: str
    """Text content of the message you want to send. You may use markdown."""
