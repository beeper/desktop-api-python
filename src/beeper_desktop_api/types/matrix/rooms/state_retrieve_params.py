# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["StateRetrieveParams"]


class StateRetrieveParams(TypedDict, total=False):
    room_id: Required[Annotated[str, PropertyInfo(alias="roomId")]]

    event_type: Required[Annotated[str, PropertyInfo(alias="eventType")]]

    format: Literal["content", "event"]
    """The format to use for the returned data.

    `content` (the default) will return only the content of the state event. `event`
    will return the entire event in the usual format suitable for clients, including
    fields like event ID, sender and timestamp.
    """
