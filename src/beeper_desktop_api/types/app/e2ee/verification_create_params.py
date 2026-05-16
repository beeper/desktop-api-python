# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VerificationCreateParams"]


class VerificationCreateParams(TypedDict, total=False):
    user_id: Annotated[str, PropertyInfo(alias="userID")]
    """User ID to verify. Defaults to the signed-in user."""
