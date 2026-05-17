# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["ResetConfirmParams"]


class ResetConfirmParams(TypedDict, total=False):
    recovery_key: Required[Annotated[str, PropertyInfo(alias="recoveryKey")]]
    """New recovery key returned by the reset step."""
