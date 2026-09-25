# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DraftAttachment", "Size"]


class Size(BaseModel):
    """Pixel dimensions of the attachment."""

    height: Optional[float] = None

    width: Optional[float] = None


class DraftAttachment(BaseModel):
    id: str
    """Draft attachment identifier."""

    type: Literal["file", "gif", "recorded_audio"]
    """Draft attachment type. GIF and recorded audio are mutually exclusive types."""

    audio_duration_seconds: Optional[float] = FieldInfo(alias="audioDurationSeconds", default=None)
    """Audio duration in seconds if known."""

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)
    """Original filename if available."""

    file_path: Optional[str] = FieldInfo(alias="filePath", default=None)
    """Local filesystem path for the draft attachment."""

    file_size: Optional[float] = FieldInfo(alias="fileSize", default=None)
    """File size in bytes if known."""

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """MIME type if known."""

    size: Optional[Size] = None
    """Pixel dimensions of the attachment."""

    sticker_id: Optional[str] = FieldInfo(alias="stickerID", default=None)
    """Sticker identifier if the draft attachment is a sticker."""
