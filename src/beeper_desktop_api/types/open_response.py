# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["OpenResponse"]


class OpenResponse(BaseModel):
    success: bool
    """Whether the app was successfully opened/focused."""
