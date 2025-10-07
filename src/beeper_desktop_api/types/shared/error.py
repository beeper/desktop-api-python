# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["Error"]


class Error(BaseModel):
    error: str
    """Error message"""

    code: Optional[str] = None
    """Error code"""

    details: Optional[Dict[str, str]] = None
    """Additional error details"""
