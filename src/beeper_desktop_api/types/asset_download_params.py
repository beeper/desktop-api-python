# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssetDownloadParams"]


class AssetDownloadParams(TypedDict, total=False):
    url: Required[str]
    """Matrix content URL (mxc:// or localmxc://) for the asset to download."""
