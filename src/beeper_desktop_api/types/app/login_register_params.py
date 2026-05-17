# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LoginRegisterParams"]


class LoginRegisterParams(TypedDict, total=False):
    accept_terms: Required[Annotated[Literal[True], PropertyInfo(alias="acceptTerms")]]
    """
    Confirms that the user agreed to our
    [terms of use](https://www.beeper.com/terms-onboarding) and has read our
    [privacy policy](https://www.beeper.com/privacy).
    """

    lead_token: Required[Annotated[str, PropertyInfo(alias="leadToken")]]
    """Registration token returned by Beeper."""

    setup_request_id: Required[Annotated[str, PropertyInfo(alias="setupRequestID")]]
    """Setup request ID returned by the start step."""

    username: Required[str]
    """Username selected by the user."""
