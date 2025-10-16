# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AssetDownloadResponse"]


class AssetDownloadResponse(BaseModel):
    error: Optional[str] = None
    """Error message if the download failed."""

    src_url: Optional[str] = FieldInfo(alias="srcURL", default=None)
    """Local file URL to the downloaded asset."""
