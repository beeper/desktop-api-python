# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RoomJoinParams", "ThirdPartySigned"]


class RoomJoinParams(TypedDict, total=False):
    via: SequenceNotStr[str]
    """The servers to attempt to join the room through.

    One of the servers must be participating in the room.
    """

    reason: str
    """
    Optional reason to be included as the `reason` on the subsequent membership
    event.
    """

    third_party_signed: ThirdPartySigned
    """
    A signature of an `m.third_party_invite` token to prove that this user owns a
    third-party identity which has been invited to the room.
    """


class ThirdPartySigned(TypedDict, total=False):
    """
    A signature of an `m.third_party_invite` token to prove that this user
    owns a third-party identity which has been invited to the room.
    """

    token: Required[str]
    """The state key of the m.third_party_invite event."""

    mxid: Required[str]
    """The Matrix ID of the invitee."""

    sender: Required[str]
    """The Matrix ID of the user who issued the invite."""

    signatures: Required[Dict[str, Dict[str, str]]]
    """A signatures object containing a signature of the entire signed object."""
