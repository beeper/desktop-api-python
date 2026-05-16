# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["RoomCreateGroupParams", "Avatar", "Disappear", "Name", "Topic"]


class RoomCreateGroupParams(TypedDict, total=False):
    bridge_id: Required[Annotated[str, PropertyInfo(alias="bridgeID")]]

    login_id: str
    """An optional explicit login ID to do the action through."""

    avatar: Avatar
    """The `m.room.avatar` event content for the room."""

    disappear: Disappear
    """The `com.beeper.disappearing_timer` event content for the room."""

    name: Name
    """The `m.room.name` event content for the room."""

    parent: object

    participants: SequenceNotStr[str]
    """The users to add to the group initially."""

    room_id: str
    """
    An existing Matrix room ID to bridge to. The other parameters must be already in
    sync with the room state when using this parameter.
    """

    topic: Topic
    """The `m.room.topic` event content for the room."""

    type: str
    """The type of group to create."""

    username: str
    """The public username for the created group."""


class Avatar(TypedDict, total=False):
    """The `m.room.avatar` event content for the room."""

    url: str


class Disappear(TypedDict, total=False):
    """The `com.beeper.disappearing_timer` event content for the room."""

    timer: float

    type: str


class Name(TypedDict, total=False):
    """The `m.room.name` event content for the room."""

    name: str


class Topic(TypedDict, total=False):
    """The `m.room.topic` event content for the room."""

    topic: str
