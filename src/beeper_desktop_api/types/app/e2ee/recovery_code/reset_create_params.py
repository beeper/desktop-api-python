# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ResetCreateParams"]


class ResetCreateParams(TypedDict, total=False):
    recovery_code: Annotated[str, PropertyInfo(alias="recoveryCode")]
    """Existing recovery key, if the user has it."""
