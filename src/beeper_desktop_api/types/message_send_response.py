# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageSendResponse"]


class MessageSendResponse(BaseModel):
    chat_id: str = FieldInfo(alias="chatID")
    """Chat ID.

    Input routes also accept the local chat ID from this Beeper Desktop installation
    when available.
    """

    pending_message_id: str = FieldInfo(alias="pendingMessageID")
    """Pending ID assigned to the message before the network confirms the send.

    Pass it to GET /v1/chats/{chatID}/messages/{messageID} to resolve, or wait for
    the matching message.upserted over the WebSocket.
    """
