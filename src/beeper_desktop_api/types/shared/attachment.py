# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Attachment", "Size"]


class Size(BaseModel):
    height: Optional[float] = None

    width: Optional[float] = None


class Attachment(BaseModel):
    type: Literal["unknown", "img", "video", "audio"]
    """Attachment type."""

    duration: Optional[float] = None
    """Duration in seconds (audio/video)."""

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)
    """Original filename if available."""

    file_size: Optional[float] = FieldInfo(alias="fileSize", default=None)
    """File size in bytes if known."""

    is_gif: Optional[bool] = FieldInfo(alias="isGif", default=None)
    """True if the attachment is a GIF."""

    is_sticker: Optional[bool] = FieldInfo(alias="isSticker", default=None)
    """True if the attachment is a sticker."""

    is_voice_note: Optional[bool] = FieldInfo(alias="isVoiceNote", default=None)
    """True if the attachment is a voice note."""

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """MIME type if known (e.g., 'image/png')."""

    poster_img: Optional[str] = FieldInfo(alias="posterImg", default=None)
    """Preview image URL for video attachments (poster frame).

    May be temporary or local-only to this device; download promptly if durable
    access is needed.
    """

    size: Optional[Size] = None
    """Pixel dimensions of the attachment: width/height in px."""

    src_url: Optional[str] = FieldInfo(alias="srcURL", default=None)
    """Public URL or local file path to fetch the asset.

    May be temporary or local-only to this device; download promptly if durable
    access is needed.
    """
