# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageUpdateResponse"]


class MessageUpdateResponse(BaseModel):
    chat_id: str = FieldInfo(alias="chatID")
    """Unique identifier of the chat."""

    message_id: str = FieldInfo(alias="messageID")
    """Message ID."""

    success: bool
    """Whether the message was successfully edited"""
