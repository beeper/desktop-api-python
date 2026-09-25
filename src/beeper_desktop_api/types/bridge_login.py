# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user import User

__all__ = ["BridgeLogin"]


class BridgeLogin(BaseModel):
    """Signed-in identity for a bridge.

    One bridge login can contain multiple chat accounts.
    """

    bridge_id: str = FieldInfo(alias="bridgeID")
    """Bridge ID."""

    login_id: str = FieldInfo(alias="loginID")
    """Bridge login ID."""

    remove_scopes: List[Literal["current-device", "all-devices"]] = FieldInfo(alias="removeScopes")

    status: Literal["connected", "connecting", "needs_login", "logged_out", "unknown"]

    account_ids: Optional[List[str]] = FieldInfo(alias="accountIDs", default=None)
    """Chat accounts that belong to this bridge login, when known."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Human-friendly bridge login status text."""

    user: Optional[User] = None
    """User the account belongs to."""
