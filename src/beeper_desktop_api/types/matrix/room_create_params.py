# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RoomCreateParams", "InitialState", "Invite3pid"]


class RoomCreateParams(TypedDict, total=False):
    creation_content: object
    """
    Extra keys, such as `m.federate`, to be added to the content of the
    [`m.room.create`](https://spec.matrix.org/v1.18/client-server-api/#mroomcreate)
    event.

    The server will overwrite the following keys: `creator`, `room_version`. Future
    versions of the specification may allow the server to overwrite other keys.

    When using the `trusted_private_chat` preset, the server SHOULD combine
    `additional_creators` specified here and the `invite` array into the eventual
    `m.room.create` event's `additional_creators`, deduplicating between the two
    parameters.
    """

    initial_state: Iterable[InitialState]
    """A list of state events to set in the new room.

    This allows the user to override the default state events set in the new room.
    The expected format of the state events are an object with type, state_key and
    content keys set.

    Takes precedence over events set by `preset`, but gets overridden by `name` and
    `topic` keys.
    """

    invite: SequenceNotStr[str]
    """A list of user IDs to invite to the room.

    This will tell the server to invite everyone in the list to the newly created
    room.
    """

    invite_3pid: Iterable[Invite3pid]
    """A list of objects representing third-party IDs to invite into the room."""

    is_direct: bool
    """
    This flag makes the server set the `is_direct` flag on the `m.room.member`
    events sent to the users in `invite` and `invite_3pid`. See
    [Direct Messaging](https://spec.matrix.org/v1.18/client-server-api/#direct-messaging)
    for more information.
    """

    name: str
    """
    If this is included, an
    [`m.room.name`](https://spec.matrix.org/v1.18/client-server-api/#mroomname)
    event will be sent into the room to indicate the name for the room. This
    overwrites any
    [`m.room.name`](https://spec.matrix.org/v1.18/client-server-api/#mroomname)
    event in `initial_state`.
    """

    power_level_content_override: object
    """The power level content to override in the default power level event.

    This object is applied on top of the generated
    [`m.room.power_levels`](https://spec.matrix.org/v1.18/client-server-api/#mroompower_levels)
    event content prior to it being sent to the room. Defaults to overriding
    nothing.
    """

    preset: Literal["private_chat", "public_chat", "trusted_private_chat"]
    """
    Convenience parameter for setting various default state events based on a
    preset.

    If unspecified, the server should use the `visibility` to determine which preset
    to use. A visibility of `public` equates to a preset of `public_chat` and
    `private` visibility equates to a preset of `private_chat`.
    """

    room_alias_name: str
    """The desired room alias **local part**.

    If this is included, a room alias will be created and mapped to the newly
    created room. The alias will belong on the _same_ homeserver which created the
    room. For example, if this was set to "foo" and sent to the homeserver
    "example.com" the complete room alias would be `#foo:example.com`.

    The complete room alias will become the canonical alias for the room and an
    `m.room.canonical_alias` event will be sent into the room.
    """

    room_version: str
    """The room version to set for the room.

    If not provided, the homeserver is to use its configured default. If provided,
    the homeserver will return a 400 error with the errcode
    `M_UNSUPPORTED_ROOM_VERSION` if it does not support the room version.
    """

    topic: str
    """
    If this is included, an
    [`m.room.topic`](https://spec.matrix.org/v1.18/client-server-api/#mroomtopic)
    event with a `text/plain` mimetype will be sent into the room to indicate the
    topic for the room. This overwrites any
    [`m.room.topic`](https://spec.matrix.org/v1.18/client-server-api/#mroomtopic)
    event in `initial_state`.
    """

    visibility: Literal["public", "private"]
    """
    The room's visibility in the server's
    [published room directory](https://spec.matrix.org/v1.18/client-server-api#published-room-directory).
    Defaults to `private`.
    """


class InitialState(TypedDict, total=False):
    content: Required[object]
    """The content of the event."""

    type: Required[str]
    """The type of event to send."""

    state_key: str
    """The state_key of the state event. Defaults to an empty string."""


class Invite3pid(TypedDict, total=False):
    address: Required[str]
    """The invitee's third-party identifier."""

    id_access_token: Required[str]
    """An access token previously registered with the identity server.

    Servers can treat this as optional to distinguish between r0.5-compatible
    clients and this specification version.
    """

    id_server: Required[str]
    """
    The hostname+port of the identity server which should be used for third-party
    identifier lookups.
    """

    medium: Required[str]
    """
    The kind of address being passed in the address field, for example `email` (see
    [the list of recognised values](https://spec.matrix.org/v1.18/appendices/#3pid-types)).
    """
