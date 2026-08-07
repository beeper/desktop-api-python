# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["StepSubmitParams"]


class StepSubmitParams(TypedDict, total=False):
    bridge_id: Required[Annotated[str, PropertyInfo(alias="bridgeID")]]
    """Bridge ID."""

    login_session_id: Required[Annotated[str, PropertyInfo(alias="loginSessionID")]]
    """Temporary bridge login session ID."""

    type: Required[Literal["user_input", "cookies", "display_and_wait"]]

    fields: Dict[str, str]
    """Field values keyed by the field IDs from the current step."""

    last_url: Annotated[str, PropertyInfo(alias="lastURL")]
    """Last browser URL reached during a cookies step, if available."""

    source: Literal["api", "webview", "browser_extension"]
    """How the step was completed.

    Omit unless the client needs to distinguish an embedded webview or browser
    extension.
    """
