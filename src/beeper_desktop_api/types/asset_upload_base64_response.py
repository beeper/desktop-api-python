# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AssetUploadBase64Response"]


class AssetUploadBase64Response(BaseModel):
    duration: Optional[float] = None
    """Duration in seconds (audio/videos)"""

    error: Optional[str] = None
    """Error message if upload failed"""

    file_name: Optional[str] = FieldInfo(alias="fileName", default=None)
    """Resolved filename"""

    file_size: Optional[float] = FieldInfo(alias="fileSize", default=None)
    """File size in bytes"""

    height: Optional[float] = None
    """Height in pixels (images/videos)"""

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """Detected or provided MIME type"""

    src_url: Optional[str] = FieldInfo(alias="srcURL", default=None)
    """Local file URL (file://) for the uploaded file"""

    upload_id: Optional[str] = FieldInfo(alias="uploadID", default=None)
    """Unique upload ID for this temporary file"""

    width: Optional[float] = None
    """Width in pixels (images/videos)"""
