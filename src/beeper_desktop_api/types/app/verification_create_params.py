# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VerificationCreateParams"]


class VerificationCreateParams(TypedDict, total=False):
    purpose: Literal["login", "device"]
    """Why this verification is being started."""

    user_id: Annotated[str, PropertyInfo(alias="userID")]
    """Beeper user ID to verify. Defaults to the signed-in user."""
