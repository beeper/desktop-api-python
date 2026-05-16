# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuthSubmitCookiesParams"]


class AuthSubmitCookiesParams(TypedDict, total=False):
    bridge_id: Required[Annotated[str, PropertyInfo(alias="bridgeID")]]

    login_process_id: Required[Annotated[str, PropertyInfo(alias="loginProcessID")]]

    body: Required[Dict[str, str]]
