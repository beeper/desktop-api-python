# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageUpdateParams"]


class MessageUpdateParams(TypedDict, total=False):
    chat_id: Required[Annotated[str, PropertyInfo(alias="chatID")]]
    """Unique identifier of the chat."""

    text: Required[str]
    """New text content for the message"""
