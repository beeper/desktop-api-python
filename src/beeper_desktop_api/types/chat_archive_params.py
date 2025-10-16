# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChatArchiveParams"]


class ChatArchiveParams(TypedDict, total=False):
    archived: bool
    """True to archive, false to unarchive"""
