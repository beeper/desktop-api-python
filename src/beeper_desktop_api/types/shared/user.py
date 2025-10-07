# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str
    """Stable Beeper user ID. Use as the primary key when referencing a person."""

    cannot_message: Optional[bool] = FieldInfo(alias="cannotMessage", default=None)
    """
    True if Beeper cannot initiate messages to this user (e.g., blocked, network
    restriction, or no DM path). The user may still message you.
    """

    email: Optional[str] = None
    """Email address if known. Not guaranteed verified."""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """Display name as shown in clients (e.g., 'Alice Example'). May include emojis."""

    img_url: Optional[str] = FieldInfo(alias="imgURL", default=None)
    """Avatar image URL if available.

    May be temporary or local-only to this device; download promptly if durable
    access is needed.
    """

    is_self: Optional[bool] = FieldInfo(alias="isSelf", default=None)
    """True if this user represents the authenticated account's own identity."""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """User's phone number in E.164 format (e.g., '+14155552671'). Omit if unknown."""

    username: Optional[str] = None
    """Human-readable handle if available (e.g., '@alice').

    May be network-specific and not globally unique.
    """
