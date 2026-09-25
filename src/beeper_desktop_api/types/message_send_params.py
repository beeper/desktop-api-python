# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageSendParams", "Attachment", "AttachmentSize"]


class MessageSendParams(TypedDict, total=False):
    attachment: Attachment
    """Single attachment to send with the message"""

    reply_to_message_id: Annotated[str, PropertyInfo(alias="replyToMessageID")]
    """Provide a message ID to send this as a reply to an existing message"""

    text: str
    """Draft text.

    Plain text and Markdown are converted to Beeper rich text with the same rules
    used by send and edit.
    """


class AttachmentSize(TypedDict, total=False):
    """Dimensions (optional override of cached value)"""

    height: Required[float]

    width: Required[float]


class Attachment(TypedDict, total=False):
    """Single attachment to send with the message"""

    upload_id: Required[Annotated[str, PropertyInfo(alias="uploadID")]]
    """Upload ID from uploadAsset endpoint. Required to reference uploaded files."""

    duration: float
    """Duration in seconds (optional override of cached value)"""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Filename (optional override of cached value)"""

    mime_type: Annotated[str, PropertyInfo(alias="mimeType")]
    """MIME type (optional override of cached value)"""

    size: AttachmentSize
    """Dimensions (optional override of cached value)"""

    type: Literal["image", "video", "audio", "file", "gif", "voice-note", "sticker"]
    """Attachment type hint (image, video, audio, file, gif, voice-note, sticker).

    If omitted, auto-detected from mimeType
    """
