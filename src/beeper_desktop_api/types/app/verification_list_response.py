# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VerificationListResponse", "Item", "ItemError", "ItemOtherDevice", "ItemQr", "ItemSAS"]


class ItemError(BaseModel):
    """Verification error details, if verification stopped."""

    code: str
    """Verification error code."""

    reason: str
    """User-facing verification error message."""


class ItemOtherDevice(BaseModel):
    """Other device participating in verification."""

    id: str
    """Other device ID."""

    name: Optional[str] = None
    """Other device display name, if known."""


class ItemQr(BaseModel):
    """QR verification data."""

    data: str
    """QR code payload to display for verification."""


class ItemSAS(BaseModel):
    """Emoji or number comparison data for verification."""

    emojis: str
    """Emoji sequence to compare on both devices."""

    decimals: Optional[str] = None
    """Number sequence to compare on both devices."""


class Item(BaseModel):
    """Trusted device verification progress."""

    id: str
    """Verification ID to pass in verification action paths."""

    available_actions: List[Literal["accept", "cancel", "qr.confirmScanned", "sas.start", "sas.confirm"]] = FieldInfo(
        alias="availableActions"
    )
    """Verification actions that are valid for the current state."""

    direction: Literal["incoming", "outgoing"]
    """Whether this device started or received the verification."""

    methods: List[Literal["qr", "sas"]]
    """Verification methods supported for this transaction."""

    purpose: Literal["login", "device"]
    """Why this verification exists."""

    state: Literal["requested", "ready", "sas_ready", "qr_scanned", "done", "cancelled", "error"]
    """Current trusted-device verification state."""

    error: Optional[ItemError] = None
    """Verification error details, if verification stopped."""

    other_device: Optional[ItemOtherDevice] = FieldInfo(alias="otherDevice", default=None)
    """Other device participating in verification."""

    other_user_id: Optional[str] = FieldInfo(alias="otherUserID", default=None)
    """Other Beeper user participating in verification."""

    qr: Optional[ItemQr] = None
    """QR verification data."""

    sas: Optional[ItemSAS] = None
    """Emoji or number comparison data for verification."""


class VerificationListResponse(BaseModel):
    items: List[Item]
