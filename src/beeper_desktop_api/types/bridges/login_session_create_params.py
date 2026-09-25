# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LoginSessionCreateParams"]


class LoginSessionCreateParams(TypedDict, total=False):
    account_id: Annotated[str, PropertyInfo(alias="accountID")]
    """Existing chat account ID to reconnect. Omit to connect a new account."""

    flow_id: Annotated[str, PropertyInfo(alias="flowID")]
    """Optional flow ID returned by the list login flows endpoint.

    If omitted, Beeper chooses the default flow.
    """

    login_id: Annotated[str, PropertyInfo(alias="loginID")]
    """Existing bridge login ID to reconnect. Omit to connect a new account."""
