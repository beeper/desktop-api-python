# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .chat import Chat

__all__ = ["ChatStartResponse"]


class ChatStartResponse(Chat):
    chat_id: str = FieldInfo(alias="chatID")
    """DEPRECATED - use id instead. Compatibility alias for older clients."""

    status: Optional[Literal["existing", "created"]] = None
    """DEPRECATED - legacy start-chat status for older clients.

    New clients should inspect the returned Chat instead.
    """
