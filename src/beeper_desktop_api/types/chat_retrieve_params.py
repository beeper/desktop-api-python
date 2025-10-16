# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChatRetrieveParams"]


class ChatRetrieveParams(TypedDict, total=False):
    max_participant_count: Annotated[Optional[int], PropertyInfo(alias="maxParticipantCount")]
    """Maximum number of participants to return.

    Use -1 for all; otherwise 0–500. Defaults to all (-1).
    """
