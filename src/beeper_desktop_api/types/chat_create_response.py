# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ChatCreateResponse"]


class ChatCreateResponse(BaseModel):
    chat_id: str = FieldInfo(alias="chatID")
    """Newly created chat ID."""
