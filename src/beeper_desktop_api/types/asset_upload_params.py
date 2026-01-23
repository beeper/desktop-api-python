# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetUploadParams"]


class AssetUploadParams(TypedDict, total=False):
    content: Required[str]
    """Base64-encoded file content (max ~500MB decoded)"""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Original filename. Generated if omitted"""

    mime_type: Annotated[str, PropertyInfo(alias="mimeType")]
    """MIME type. Auto-detected from magic bytes if omitted"""
