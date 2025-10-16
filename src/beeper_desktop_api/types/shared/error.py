# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["Error", "Details", "DetailsIssues", "DetailsIssuesIssue"]


class DetailsIssuesIssue(BaseModel):
    code: str
    """Validation issue code"""

    message: str
    """Human-readable description of the validation issue"""

    path: List[Union[str, float]]
    """Path pointing to the invalid field within the payload"""


class DetailsIssues(BaseModel):
    issues: List[DetailsIssuesIssue]
    """List of validation issues"""


Details: TypeAlias = Union[DetailsIssues, Dict[str, Optional[object]], Optional[object]]


class Error(BaseModel):
    code: str
    """Machine-readable error code"""

    message: str
    """Error message"""

    details: Optional[Details] = None
    """Additional error details for debugging"""
