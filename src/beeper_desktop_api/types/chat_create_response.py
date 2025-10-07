# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .shared.base_response import BaseResponse

__all__ = ["ChatCreateResponse"]


class ChatCreateResponse(BaseResponse):
    chat_id: Optional[str] = FieldInfo(alias="chatID", default=None)
    """Newly created chat if available."""
