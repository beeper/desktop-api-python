# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageSendResponse"]


class MessageSendResponse(BaseModel):
    chat_id: str = FieldInfo(alias="chatID")
    """Unique identifier of the chat."""

    pending_message_id: str = FieldInfo(alias="pendingMessageID")
    """Pending message ID"""
