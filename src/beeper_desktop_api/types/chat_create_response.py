# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ChatCreateResponse"]


class ChatCreateResponse(BaseModel):
    chat_id: str = FieldInfo(alias="chatID")
    """Newly created chat ID."""

    status: Optional[Literal["existing", "created"]] = None
    """Only returned in start mode.

    'existing' means an existing chat was reused; 'created' means a new chat was
    created.
    """
