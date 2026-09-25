# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .account import Account
from .._models import BaseModel
from .bridge_login import BridgeLogin
from .cookie_field import CookieField
from .shared.api_error import APIError
from .login_input_field import LoginInputField

__all__ = [
    "LoginSession",
    "CurrentStep",
    "CurrentStepUserInput",
    "CurrentStepCookies",
    "CurrentStepDisplayAndWait",
    "CurrentStepDisplayAndWaitDisplay",
    "CurrentStepDisplayAndWaitDisplayQRCode",
    "CurrentStepDisplayAndWaitDisplayEmoji",
    "CurrentStepDisplayAndWaitDisplayCode",
    "CurrentStepDisplayAndWaitDisplayEmpty",
    "CurrentStepComplete",
]


class CurrentStepUserInput(BaseModel):
    fields: List[LoginInputField]

    step_id: str = FieldInfo(alias="stepID")

    type: Literal["user_input"]

    attachments: Optional[List[Optional[object]]] = None

    instructions: Optional[str] = None
    """User-facing instructions for this step."""


class CurrentStepCookies(BaseModel):
    fields: List[CookieField]

    step_id: str = FieldInfo(alias="stepID")

    type: Literal["cookies"]

    url: str
    """URL to open for the user."""

    expected_final_url_regex: Optional[str] = FieldInfo(alias="expectedFinalURLRegex", default=None)
    """Regular expression that identifies the final URL after sign-in."""

    extract_js: Optional[str] = FieldInfo(alias="extractJS", default=None)
    """Optional extraction script for browser-based sign-in helpers.

    Treat as an opaque helper value.
    """

    instructions: Optional[str] = None
    """User-facing instructions for this browser step."""

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)
    """Suggested user agent for the browser session."""


class CurrentStepDisplayAndWaitDisplayQRCode(BaseModel):
    data: str

    type: Literal["qr"]


class CurrentStepDisplayAndWaitDisplayEmoji(BaseModel):
    image_url: str = FieldInfo(alias="imageURL")

    type: Literal["emoji"]


class CurrentStepDisplayAndWaitDisplayCode(BaseModel):
    data: str

    type: Literal["code"]


class CurrentStepDisplayAndWaitDisplayEmpty(BaseModel):
    type: Literal["nothing"]


CurrentStepDisplayAndWaitDisplay: TypeAlias = Union[
    CurrentStepDisplayAndWaitDisplayQRCode,
    CurrentStepDisplayAndWaitDisplayEmoji,
    CurrentStepDisplayAndWaitDisplayCode,
    CurrentStepDisplayAndWaitDisplayEmpty,
]


class CurrentStepDisplayAndWait(BaseModel):
    display: CurrentStepDisplayAndWaitDisplay

    step_id: str = FieldInfo(alias="stepID")

    type: Literal["display_and_wait"]

    instructions: Optional[str] = None
    """User-facing instructions for this step."""


class CurrentStepComplete(BaseModel):
    type: Literal["complete"]

    account: Optional[Account] = None
    """A chat account added to Beeper."""

    instructions: Optional[str] = None
    """Completion instructions, when provided."""

    login: Optional[BridgeLogin] = None
    """Signed-in identity for a bridge.

    One bridge login can contain multiple chat accounts.
    """

    step_id: Optional[str] = FieldInfo(alias="stepID", default=None)


CurrentStep: TypeAlias = Union[CurrentStepUserInput, CurrentStepCookies, CurrentStepDisplayAndWait, CurrentStepComplete]


class LoginSession(BaseModel):
    bridge_id: str = FieldInfo(alias="bridgeID")
    """Bridge ID."""

    login_session_id: str = FieldInfo(alias="loginSessionID")
    """Temporary bridge login session ID."""

    status: Literal[
        "waiting_for_input", "waiting_for_cookies", "waiting_for_display", "complete", "cancelled", "failed"
    ]

    account: Optional[Account] = None
    """A chat account added to Beeper."""

    account_id: Optional[str] = FieldInfo(alias="accountID", default=None)
    """Chat account ID for reconnect flows, when known."""

    current_step: Optional[CurrentStep] = FieldInfo(alias="currentStep", default=None)
    """Step the client should show or complete next.

    Omitted when the session is complete, cancelled, or failed.
    """

    error: Optional[APIError] = None

    login: Optional[BridgeLogin] = None
    """Signed-in identity for a bridge.

    One bridge login can contain multiple chat accounts.
    """

    login_id: Optional[str] = FieldInfo(alias="loginID", default=None)
    """Bridge login ID for reconnect flows, when known."""
