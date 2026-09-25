# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AttachmentCapabilities"]


class AttachmentCapabilities(BaseModel):
    """Capabilities for one attachment message type."""

    mime_types: Dict[str, Literal[-2, -1, 0, 1, 2]] = FieldInfo(alias="mimeTypes")
    """Supported MIME types or MIME patterns for this file message type.

    Missing MIME types should be treated as rejected.
    """

    caption: Optional[Literal[-2, -1, 0, 1, 2]] = None
    """
    -2: rejected, -1: dropped, 0: unsupported, 1: partially supported, 2: fully
    supported.
    """

    max_caption_length: Optional[int] = FieldInfo(alias="maxCaptionLength", default=None)
    """Maximum caption length when captions are supported."""

    max_duration: Optional[int] = FieldInfo(alias="maxDuration", default=None)
    """Maximum audio or video duration in seconds."""

    max_height: Optional[int] = FieldInfo(alias="maxHeight", default=None)
    """Maximum image or video height in pixels."""

    max_size: Optional[int] = FieldInfo(alias="maxSize", default=None)
    """Maximum file size in bytes."""

    max_width: Optional[int] = FieldInfo(alias="maxWidth", default=None)
    """Maximum image or video width in pixels."""

    view_once: Optional[bool] = FieldInfo(alias="viewOnce", default=None)
    """True if this file type can be sent as view-once media."""
