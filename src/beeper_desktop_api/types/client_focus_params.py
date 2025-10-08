# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientFocusParams"]


class ClientFocusParams(TypedDict, total=False):
    chat_id: Annotated[str, PropertyInfo(alias="chatID")]
    """Optional Beeper chat ID (or local chat ID) to focus after opening the app.

    If omitted, only opens/focuses the app.
    """

    draft_attachment_path: Annotated[str, PropertyInfo(alias="draftAttachmentPath")]
    """Optional draft attachment path to populate in the message input field."""

    draft_text: Annotated[str, PropertyInfo(alias="draftText")]
    """Optional draft text to populate in the message input field."""

    message_id: Annotated[str, PropertyInfo(alias="messageID")]
    """Optional message ID. Jumps to that message in the chat when opening."""
