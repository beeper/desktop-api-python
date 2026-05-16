# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LoginRegisterParams"]


class LoginRegisterParams(TypedDict, total=False):
    accept_terms: Required[Annotated[Literal[True], PropertyInfo(alias="acceptTerms")]]
    """
    Confirms that the user accepted the Terms of Use and acknowledged the Privacy
    Policy.
    """

    lead_token: Required[Annotated[str, PropertyInfo(alias="leadToken")]]
    """Registration token returned by Beeper."""

    request: Required[str]
    """Login request ID returned by the start step."""

    username: Required[str]
    """Username selected by the user."""
