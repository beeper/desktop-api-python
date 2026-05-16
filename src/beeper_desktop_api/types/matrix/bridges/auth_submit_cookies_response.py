# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "AuthSubmitCookiesResponse",
    "UnionMember0",
    "UnionMember0DisplayAndWait",
    "UnionMember1",
    "UnionMember1UserInput",
    "UnionMember1UserInputField",
    "UnionMember1UserInputAttachment",
    "UnionMember1UserInputAttachmentInfo",
    "UnionMember2",
    "UnionMember2Cookies",
    "UnionMember2CookiesField",
    "UnionMember3",
    "UnionMember3Complete",
]


class UnionMember0DisplayAndWait(BaseModel):
    """Parameters for the display and wait login step"""

    type: Literal["qr", "emoji", "code", "nothing"]
    """The type of thing to display"""

    data: Optional[str] = None
    """
    The thing to display (raw data for QR, unicode emoji for emoji, plain string for
    code)
    """

    image_url: Optional[str] = None
    """An image containing the thing to display.

    If present, this is recommended over using data directly. For emojis, the URL to
    the canonical image representation of the emoji
    """


class UnionMember0(BaseModel):
    """Display and wait login step"""

    display_and_wait: UnionMember0DisplayAndWait
    """Parameters for the display and wait login step"""

    type: Literal["display_and_wait"]

    instructions: Optional[str] = None
    """Human-readable instructions for completing this login step."""

    login_id: Optional[str] = None
    """An identifier for the current login process.

    Must be passed to execute more steps of the login.
    """

    step_id: Optional[str] = None
    """An unique ID identifying this step.

    This can be used to implement special behavior in clients.
    """


class UnionMember1UserInputField(BaseModel):
    """A field that the user can fill."""

    id: str
    """The internal ID of the field.

    This must be used as the key in the object when submitting the data back to the
    bridge.
    """

    name: str
    """The name of the field shown to the user."""

    type: Literal["username", "phone_number", "email", "password", "2fa_code", "token", "url", "domain", "select"]
    """The type of field."""

    default_value: Optional[str] = None
    """A default value that the client can pre-fill the field with."""

    description: Optional[str] = None
    """A more detailed description of the field shown to the user."""

    options: Optional[List[str]] = None
    """For fields of type select, the valid options."""

    pattern: Optional[str] = None
    """A regular expression that the field value must match."""


class UnionMember1UserInputAttachmentInfo(BaseModel):
    """Optional but recommended metadata for the attachment.

    Can generally be derived from the raw content if omitted.
    """

    h: Optional[float] = None
    """The height of the media in pixels. Only applicable for images and videos."""

    mimetype: Optional[str] = None
    """The MIME type for the media content."""

    size: Optional[float] = None
    """The size of the media content in number of bytes.

    Strongly recommended to include.
    """

    w: Optional[float] = None
    """The width of the media in pixels. Only applicable for images and videos."""


class UnionMember1UserInputAttachment(BaseModel):
    """A media attachment to show the user."""

    content: str
    """The raw file content for the attachment encoded in base64."""

    filename: str
    """The filename for the media attachment."""

    type: Literal["m.image", "m.audio"]
    """
    The type of media attachment, using the same media type identifiers as Matrix
    attachments. Only some are supported.
    """

    info: Optional[UnionMember1UserInputAttachmentInfo] = None
    """Optional but recommended metadata for the attachment.

    Can generally be derived from the raw content if omitted.
    """


class UnionMember1UserInput(BaseModel):
    """Parameters for the user input login step"""

    fields: List[UnionMember1UserInputField]
    """The list of fields that the user is requested to fill."""

    attachments: Optional[List[UnionMember1UserInputAttachment]] = None
    """A list of media attachments to show the user alongside the form fields."""


class UnionMember1(BaseModel):
    """User input login step"""

    type: Literal["user_input"]

    user_input: UnionMember1UserInput
    """Parameters for the user input login step"""

    instructions: Optional[str] = None
    """Human-readable instructions for completing this login step."""

    login_id: Optional[str] = None
    """An identifier for the current login process.

    Must be passed to execute more steps of the login.
    """

    step_id: Optional[str] = None
    """An unique ID identifying this step.

    This can be used to implement special behavior in clients.
    """


class UnionMember2CookiesField(BaseModel):
    """An individual cookie or other stored data item that must be extracted."""

    name: str
    """The name of the item to extract."""

    type: Literal["cookie", "local_storage", "request_header", "request_body", "special"]
    """The type of data to extract."""

    cookie_domain: Optional[str] = None
    """For the `cookie` type, the domain of the cookie."""

    request_url_regex: Optional[str] = None
    """
    For the `request_header` and `request_body` types, a regex that matches the URLs
    from which the values can be extracted.
    """


class UnionMember2Cookies(BaseModel):
    """Parameters for the cookie login step"""

    fields: List[UnionMember2CookiesField]
    """The list of cookies or other stored data that must be extracted."""

    url: str
    """The URL to open when using a webview to extract cookies."""

    extract_js: Optional[str] = None
    """
    A JavaScript snippet that can extract some or all of the fields. The snippet
    will evaluate to a promise that resolves when the relevant fields are found.
    Fields that are not present in the promise result must be extracted another way.
    """

    user_agent: Optional[str] = None
    """An optional user agent that the webview should use."""

    wait_for_url_pattern: Optional[str] = None
    """A regex pattern that the URL should match before the client closes the webview.

    The client may submit the login if the user closes the webview after all cookies
    are collected even if this URL is not reached, but it should only automatically
    close the webview after both cookies and the URL match.
    """


class UnionMember2(BaseModel):
    """Cookie login step"""

    cookies: UnionMember2Cookies
    """Parameters for the cookie login step"""

    type: Literal["cookies"]

    instructions: Optional[str] = None
    """Human-readable instructions for completing this login step."""

    login_id: Optional[str] = None
    """An identifier for the current login process.

    Must be passed to execute more steps of the login.
    """

    step_id: Optional[str] = None
    """An unique ID identifying this step.

    This can be used to implement special behavior in clients.
    """


class UnionMember3Complete(BaseModel):
    """Information about the completed login"""

    user_login_id: Optional[str] = None
    """The unique ID of a login. Defined by the network connector."""


class UnionMember3(BaseModel):
    """Login complete"""

    complete: UnionMember3Complete
    """Information about the completed login"""

    type: Literal["complete"]

    instructions: Optional[str] = None
    """Human-readable instructions for completing this login step."""

    login_id: Optional[str] = None
    """An identifier for the current login process.

    Must be passed to execute more steps of the login.
    """

    step_id: Optional[str] = None
    """An unique ID identifying this step.

    This can be used to implement special behavior in clients.
    """


AuthSubmitCookiesResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3]
