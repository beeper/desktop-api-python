# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LoginInputField"]


class LoginInputField(BaseModel):
    id: str
    """Field ID to send back in the fields object."""

    initial_value: Optional[str] = FieldInfo(alias="initialValue", default=None)
    """Initial field value, when provided by the network."""

    label: Optional[str] = None
    """Field label to show to the user."""

    optional: Optional[bool] = None
    """True if the user can leave this field empty."""

    placeholder: Optional[str] = None
    """Placeholder text to show when the field is empty."""

    type: Optional[str] = None
    """Suggested input type, such as text, password, or email."""
