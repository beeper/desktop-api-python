# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageDeleteParams"]


class MessageDeleteParams(TypedDict, total=False):
    chat_id: Required[Annotated[str, PropertyInfo(alias="chatID")]]
    """Chat ID.

    Input routes also accept the local chat ID from this installation when
    available.
    """

    for_everyone: Annotated[Optional[bool], PropertyInfo(alias="forEveryone")]
    """
    True to request deletion for everyone when the network supports it; false to
    delete only for the authenticated user when supported.
    """
