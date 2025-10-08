# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MessageSearchParams"]


class MessageSearchParams(TypedDict, total=False):
    account_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="accountIDs")]
    """Limit search to specific account IDs."""

    chat_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="chatIDs")]
    """Limit search to specific chat IDs."""

    chat_type: Annotated[Literal["group", "single"], PropertyInfo(alias="chatType")]
    """Filter by chat type: 'group' for group chats, 'single' for 1:1 chats."""

    cursor: str
    """Opaque pagination cursor; do not inspect. Use together with 'direction'."""

    date_after: Annotated[Union[str, datetime], PropertyInfo(alias="dateAfter", format="iso8601")]
    """
    Only include messages with timestamp strictly after this ISO 8601 datetime
    (e.g., '2024-07-01T00:00:00Z' or '2024-07-01T00:00:00+02:00').
    """

    date_before: Annotated[Union[str, datetime], PropertyInfo(alias="dateBefore", format="iso8601")]
    """
    Only include messages with timestamp strictly before this ISO 8601 datetime
    (e.g., '2024-07-31T23:59:59Z' or '2024-07-31T23:59:59+02:00').
    """

    direction: Literal["after", "before"]
    """
    Pagination direction used with 'cursor': 'before' fetches older results, 'after'
    fetches newer results. Defaults to 'before' when only 'cursor' is provided.
    """

    exclude_low_priority: Annotated[Optional[bool], PropertyInfo(alias="excludeLowPriority")]
    """Exclude messages marked Low Priority by the user.

    Default: true. Set to false to include all.
    """

    include_muted: Annotated[Optional[bool], PropertyInfo(alias="includeMuted")]
    """
    Include messages in chats marked as Muted by the user, which are usually less
    important. Default: true. Set to false if the user wants a more refined search.
    """

    limit: int
    """Maximum number of messages to return."""

    media_types: Annotated[List[Literal["any", "video", "image", "link", "file"]], PropertyInfo(alias="mediaTypes")]
    """Filter messages by media types.

    Use ['any'] for any media type, or specify exact types like ['video', 'image'].
    Omit for no media filtering.
    """

    query: str
    """Literal word search (NOT semantic).

    Finds messages containing these EXACT words in any order. Use single words users
    actually type, not concepts or phrases. Example: use "dinner" not "dinner
    plans", use "sick" not "health issues". If omitted, returns results filtered
    only by other parameters.
    """

    sender: Union[Literal["me", "others"], str]
    """
    Filter by sender: 'me' (messages sent by the authenticated user), 'others'
    (messages sent by others), or a specific user ID string (user.id).
    """
