# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChatArchiveParams"]


class ChatArchiveParams(TypedDict, total=False):
    chat_id: Required[Annotated[str, PropertyInfo(alias="chatID")]]
    """
    The identifier of the chat to archive or unarchive (accepts both chatID and
    local chat ID)
    """

    archived: bool
    """True to archive, false to unarchive"""
