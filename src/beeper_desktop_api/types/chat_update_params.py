# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChatUpdateParams", "Draft", "DraftAttachments", "DraftAttachmentsSize"]


class ChatUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """Group chat description/topic.

    Support depends on the chat account and chat permissions.
    """

    draft: Optional[Draft]
    """Draft object to set or clear.

    Non-empty drafts are only accepted when the current draft is empty. Send
    draft=null to clear text and attachments together before setting a new draft.
    """

    img_url: Annotated[Optional[str], PropertyInfo(alias="imgURL")]
    """Local filesystem path to a group chat avatar image.

    Support depends on the chat account and chat permissions.
    """

    is_archived: Annotated[bool, PropertyInfo(alias="isArchived")]
    """Archive or unarchive the chat."""

    is_low_priority: Annotated[bool, PropertyInfo(alias="isLowPriority")]
    """Mark or unmark the chat as low priority when supported by the account."""

    is_muted: Annotated[bool, PropertyInfo(alias="isMuted")]
    """Mute or unmute the chat."""

    is_pinned: Annotated[bool, PropertyInfo(alias="isPinned")]
    """Pin or unpin the chat when supported by the account."""

    message_expiry_seconds: Annotated[Optional[int], PropertyInfo(alias="messageExpirySeconds")]
    """Disappearing-message timer in seconds, or null to clear when supported."""

    title: Optional[str]
    """Custom chat title. Support depends on the chat account and chat permissions."""


class DraftAttachmentsSize(TypedDict, total=False):
    """Dimensions (optional override of cached value)"""

    height: Required[float]

    width: Required[float]


class DraftAttachments(TypedDict, total=False):
    upload_id: Required[Annotated[str, PropertyInfo(alias="uploadID")]]
    """Upload ID from uploadAsset endpoint. Required to reference uploaded files."""

    id: str
    """Optional draft attachment identifier.

    If omitted, a new identifier is generated.
    """

    duration: float
    """Duration in seconds (optional override of cached value)"""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Filename (optional override of cached value)"""

    mime_type: Annotated[str, PropertyInfo(alias="mimeType")]
    """MIME type (optional override of cached value)"""

    size: DraftAttachmentsSize
    """Dimensions (optional override of cached value)"""

    type: Literal["image", "video", "audio", "file", "gif", "voice-note", "sticker"]
    """Attachment type hint (image, video, audio, file, gif, voice-note, sticker).

    If omitted, auto-detected from mimeType
    """


class Draft(TypedDict, total=False):
    """Draft object to set or clear.

    Non-empty drafts are only accepted when the current draft is empty. Send draft=null to clear text and attachments together before setting a new draft.
    """

    text: Required[str]
    """Draft text.

    Plain text and Markdown are converted to Matrix HTML with the same rules used by
    send and edit.
    """

    attachments: Dict[str, DraftAttachments]
    """Draft attachments keyed by attachment ID.

    Each attachment must reference an uploadID returned by the upload file endpoint.
    """
