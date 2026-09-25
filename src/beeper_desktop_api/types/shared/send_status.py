# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SendStatus"]


class SendStatus(BaseModel):
    """Message send status for this message, when reported by the bridge."""

    status: Literal["SUCCESS", "PENDING", "FAIL_RETRIABLE", "FAIL_PERMANENT"]
    """Current status of the message send attempt."""

    timestamp: datetime
    """Timestamp for the send status event."""

    delivered_to_users: Optional[List[str]] = FieldInfo(alias="deliveredToUsers", default=None)
    """User IDs the message was delivered to, when reported by the network."""

    internal_error: Optional[str] = FieldInfo(alias="internalError", default=None)
    """Diagnostic error detail from the messaging network adapter.

    Do not show directly to users.
    """

    message: Optional[str] = None
    """Human-readable send status or failure message."""

    reason: Optional[str] = None
    """Machine-readable failure reason. Present when the send status is a failure."""
