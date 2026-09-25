# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LinkPreview", "ImgSize"]


class ImgSize(BaseModel):
    """Preview image dimensions."""

    height: Optional[float] = None

    width: Optional[float] = None


class LinkPreview(BaseModel):
    """Link preview included with a message."""

    title: str
    """Link preview title."""

    url: str
    """Resolved link URL."""

    favicon: Optional[str] = None
    """Favicon URL if available.

    May be temporary or available only on this device; download promptly if durable
    access is needed.
    """

    img: Optional[str] = None
    """Preview image URL if available.

    May be temporary or available only on this device; download promptly if durable
    access is needed.
    """

    img_size: Optional[ImgSize] = FieldInfo(alias="imgSize", default=None)
    """Preview image dimensions."""

    original_url: Optional[str] = FieldInfo(alias="originalURL", default=None)
    """Original URL when the displayed URL is shortened or redirected."""

    summary: Optional[str] = None
    """Link preview summary."""
