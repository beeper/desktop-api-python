# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssetServeParams"]


class AssetServeParams(TypedDict, total=False):
    url: Required[str]
    """File URL to serve. Accepts mxc://, localmxc://, or file:// URLs."""
