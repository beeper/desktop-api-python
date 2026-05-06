# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .shared.message import Message

__all__ = ["MessageUpdateResponse"]


class MessageUpdateResponse(Message):
    message_id: str = FieldInfo(alias="messageID")
    """DEPRECATED - use id instead. Compatibility alias for older clients."""

    success: Literal[True]
    """DEPRECATED - compatibility field.

    Successful responses are already represented by the 200 status code.
    """
