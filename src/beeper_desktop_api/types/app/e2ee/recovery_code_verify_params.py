# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RecoveryCodeVerifyParams"]


class RecoveryCodeVerifyParams(TypedDict, total=False):
    recovery_code: Required[Annotated[str, PropertyInfo(alias="recoveryCode")]]
    """Recovery key saved by the user."""
