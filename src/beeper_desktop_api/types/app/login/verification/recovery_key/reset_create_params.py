# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["ResetCreateParams"]


class ResetCreateParams(TypedDict, total=False):
    existing_recovery_key: Annotated[str, PropertyInfo(alias="existingRecoveryKey")]
    """Existing recovery key, if the user has it."""
