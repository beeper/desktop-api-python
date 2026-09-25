# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageSendResponse"]


class MessageSendResponse(BaseModel):
    chat_id: str = FieldInfo(alias="chatID")
    """Chat the message was actually sent to.

    When sending to a merged chat, this is the member chat the send was routed to.
    """

    pending_message_id: str = FieldInfo(alias="pendingMessageID")
    """Pending ID assigned to the message before the network confirms the send.

    Pass it to GET /v1/chats/{chatID}/messages/{messageID} to resolve, or wait for
    the matching message.upserted over the WebSocket.
    """
