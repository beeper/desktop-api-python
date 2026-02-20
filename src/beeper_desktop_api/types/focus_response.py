# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FocusResponse"]


class FocusResponse(BaseModel):
    """Response indicating successful app focus action."""

    success: bool
    """Whether the app was successfully opened/focused."""
