# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AuthWhoamiResponse", "LoginFlow", "Login", "LoginProfile", "LoginState", "Network"]


class LoginFlow(BaseModel):
    """An individual login flow which can be used to sign into the remote network."""

    id: str
    """
    An internal ID that is passed to the /login/start call to start a login with
    this flow.
    """

    description: str
    """A human-readable description of the login flow."""

    name: str
    """A human-readable name for the login flow."""


class LoginProfile(BaseModel):
    """The profile info of the logged-in user on the remote network."""

    avatar: Optional[str] = None
    """The user's avatar"""

    email: Optional[str] = None
    """The user's email address"""

    name: Optional[str] = None
    """The user's displayname"""

    phone: Optional[str] = None
    """The user's phone number"""

    username: Optional[str] = None
    """The user's username"""


class LoginState(BaseModel):
    """The connection status of an individual login"""

    state_event: Literal["CONNECTING", "CONNECTED", "TRANSIENT_DISCONNECT", "BAD_CREDENTIALS", "UNKNOWN_ERROR"]
    """The current state of this login."""

    timestamp: float
    """The time when the state was last updated."""

    error: Optional[str] = None
    """An error code defined by the network connector."""

    info: Optional[object] = None
    """Additional arbitrary info provided by the network connector."""

    message: Optional[str] = None
    """A human-readable error message defined by the network connector."""

    reason: Optional[str] = None
    """A reason code for non-error states that aren't exactly successes either."""


class Login(BaseModel):
    """The info of an individual login"""

    id: str
    """The unique ID of a login. Defined by the network connector."""

    name: str
    """A human-readable name for the login. Defined by the network connector."""

    profile: LoginProfile
    """The profile info of the logged-in user on the remote network."""

    state: LoginState
    """The connection status of an individual login"""

    space_room: Optional[str] = None
    """The personal filtering space room ID for this login."""


class Network(BaseModel):
    """Info about the network that the bridge is bridging to."""

    beeper_bridge_type: str
    """An identifier uniquely identifying the bridge software."""

    displayname: str
    """The displayname of the network."""

    network_icon: str
    """The icon of the network as a `mxc://` URI."""

    network_id: str
    """An identifier uniquely identifying the network."""

    network_url: str
    """The URL to the website of the network."""


class AuthWhoamiResponse(BaseModel):
    """Info about the bridge and user"""

    bridge_bot: str
    """The Matrix user ID of the bridge bot."""

    command_prefix: str
    """The command prefix used by this bridge."""

    homeserver: str
    """The server name the bridge is running on."""

    login_flows: List[LoginFlow]
    """The login flows that the bridge supports."""

    logins: List[Login]
    """The logins of the user who made the /whoami call"""

    network: Network
    """Info about the network that the bridge is bridging to."""

    management_room: Optional[str] = None
    """The Matrix management room ID of the user who made the /whoami call."""
