# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VerificationCancelParams"]


class VerificationCancelParams(TypedDict, total=False):
    code: str
    """Optional cancellation code."""

    reason: str
    """Optional user-facing cancellation reason."""
