# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .state import (
    StateResource,
    AsyncStateResource,
    StateResourceWithRawResponse,
    AsyncStateResourceWithRawResponse,
    StateResourceWithStreamingResponse,
    AsyncStateResourceWithStreamingResponse,
)
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .account_data import (
    AccountDataResource,
    AsyncAccountDataResource,
    AccountDataResourceWithRawResponse,
    AsyncAccountDataResourceWithRawResponse,
    AccountDataResourceWithStreamingResponse,
    AsyncAccountDataResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.matrix import room_join_params, room_leave_params, room_create_params
from ....types.matrix.room_join_response import RoomJoinResponse
from ....types.matrix.room_create_response import RoomCreateResponse

__all__ = ["RoomsResource", "AsyncRoomsResource"]


class RoomsResource(SyncAPIResource):
    @cached_property
    def account_data(self) -> AccountDataResource:
        return AccountDataResource(self._client)

    @cached_property
    def state(self) -> StateResource:
        return StateResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RoomsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return RoomsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoomsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return RoomsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        creation_content: object | Omit = omit,
        initial_state: Iterable[room_create_params.InitialState] | Omit = omit,
        invite: SequenceNotStr[str] | Omit = omit,
        invite_3pid: Iterable[room_create_params.Invite3pid] | Omit = omit,
        is_direct: bool | Omit = omit,
        name: str | Omit = omit,
        power_level_content_override: object | Omit = omit,
        preset: Literal["private_chat", "public_chat", "trusted_private_chat"] | Omit = omit,
        room_alias_name: str | Omit = omit,
        room_version: str | Omit = omit,
        topic: str | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomCreateResponse:
        """
        Create a new room with various configuration options.

        The server MUST apply the normal state resolution rules when creating the new
        room, including checking power levels for each event. It MUST apply the events
        implied by the request in the following order:

        1. The `m.room.create` event itself. Must be the first event in the room.

        2. An `m.room.member` event for the creator to join the room. This is needed so
           the remaining events can be sent.

        3. A default `m.room.power_levels` event. Overridden by the
           `power_level_content_override` parameter.

           In [room versions](https://spec.matrix.org/v1.18/rooms) 1 through 11, the
           room creator (and not other members) will be given permission to send state
           events.

           In room versions 12 and later, the room creator is given infinite power level
           and cannot be specified in the `users` field of `m.room.power_levels`, so is
           not listed explicitly.

           **Note**: For `trusted_private_chat`, the users specified in the `invite`
           parameter SHOULD also be appended to `additional_creators` by the server, per
           the `creation_content` parameter.

           If the room's version is 12 or higher, the power level for sending
           `m.room.tombstone` events MUST explicitly be higher than `state_default`. For
           example, set to 150 instead of 100.

        4. An `m.room.canonical_alias` event if `room_alias_name` is given.

        5. Events set by the `preset`. Currently these are the `m.room.join_rules`,
           `m.room.history_visibility`, and `m.room.guest_access` state events.

        6. Events listed in `initial_state`, in the order that they are listed.

        7. Events implied by `name` and `topic` (`m.room.name` and `m.room.topic` state
           events).

        8. Invite events implied by `invite` and `invite_3pid` (`m.room.member` with
           `membership: invite` and `m.room.third_party_invite`).

        The available presets do the following with respect to room state:

        | Preset                 | `join_rules` | `history_visibility` | `guest_access` | Other                                                            |
        | ---------------------- | ------------ | -------------------- | -------------- | ---------------------------------------------------------------- |
        | `private_chat`         | `invite`     | `shared`             | `can_join`     |                                                                  |
        | `trusted_private_chat` | `invite`     | `shared`             | `can_join`     | All invitees are given the same power level as the room creator. |
        | `public_chat`          | `public`     | `shared`             | `forbidden`    |                                                                  |

        The server will create a `m.room.create` event in the room with the requesting
        user as the creator, alongside other keys provided in the `creation_content` or
        implied by behaviour of `creation_content`.

        Args:
          creation_content: Extra keys, such as `m.federate`, to be added to the content of the
              [`m.room.create`](https://spec.matrix.org/v1.18/client-server-api/#mroomcreate)
              event.

              The server will overwrite the following keys: `creator`, `room_version`. Future
              versions of the specification may allow the server to overwrite other keys.

              When using the `trusted_private_chat` preset, the server SHOULD combine
              `additional_creators` specified here and the `invite` array into the eventual
              `m.room.create` event's `additional_creators`, deduplicating between the two
              parameters.

          initial_state: A list of state events to set in the new room. This allows the user to override
              the default state events set in the new room. The expected format of the state
              events are an object with type, state_key and content keys set.

              Takes precedence over events set by `preset`, but gets overridden by `name` and
              `topic` keys.

          invite: A list of user IDs to invite to the room. This will tell the server to invite
              everyone in the list to the newly created room.

          invite_3pid: A list of objects representing third-party IDs to invite into the room.

          is_direct: This flag makes the server set the `is_direct` flag on the `m.room.member`
              events sent to the users in `invite` and `invite_3pid`. See
              [Direct Messaging](https://spec.matrix.org/v1.18/client-server-api/#direct-messaging)
              for more information.

          name: If this is included, an
              [`m.room.name`](https://spec.matrix.org/v1.18/client-server-api/#mroomname)
              event will be sent into the room to indicate the name for the room. This
              overwrites any
              [`m.room.name`](https://spec.matrix.org/v1.18/client-server-api/#mroomname)
              event in `initial_state`.

          power_level_content_override: The power level content to override in the default power level event. This
              object is applied on top of the generated
              [`m.room.power_levels`](https://spec.matrix.org/v1.18/client-server-api/#mroompower_levels)
              event content prior to it being sent to the room. Defaults to overriding
              nothing.

          preset: Convenience parameter for setting various default state events based on a
              preset.

              If unspecified, the server should use the `visibility` to determine which preset
              to use. A visibility of `public` equates to a preset of `public_chat` and
              `private` visibility equates to a preset of `private_chat`.

          room_alias_name: The desired room alias **local part**. If this is included, a room alias will be
              created and mapped to the newly created room. The alias will belong on the
              _same_ homeserver which created the room. For example, if this was set to "foo"
              and sent to the homeserver "example.com" the complete room alias would be
              `#foo:example.com`.

              The complete room alias will become the canonical alias for the room and an
              `m.room.canonical_alias` event will be sent into the room.

          room_version: The room version to set for the room. If not provided, the homeserver is to use
              its configured default. If provided, the homeserver will return a 400 error with
              the errcode `M_UNSUPPORTED_ROOM_VERSION` if it does not support the room
              version.

          topic: If this is included, an
              [`m.room.topic`](https://spec.matrix.org/v1.18/client-server-api/#mroomtopic)
              event with a `text/plain` mimetype will be sent into the room to indicate the
              topic for the room. This overwrites any
              [`m.room.topic`](https://spec.matrix.org/v1.18/client-server-api/#mroomtopic)
              event in `initial_state`.

          visibility: The room's visibility in the server's
              [published room directory](https://spec.matrix.org/v1.18/client-server-api#published-room-directory).
              Defaults to `private`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/_matrix/client/v3/createRoom",
            body=maybe_transform(
                {
                    "creation_content": creation_content,
                    "initial_state": initial_state,
                    "invite": invite,
                    "invite_3pid": invite_3pid,
                    "is_direct": is_direct,
                    "name": name,
                    "power_level_content_override": power_level_content_override,
                    "preset": preset,
                    "room_alias_name": room_alias_name,
                    "room_version": room_version,
                    "topic": topic,
                    "visibility": visibility,
                },
                room_create_params.RoomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomCreateResponse,
        )

    def join(
        self,
        room_id_or_alias: str,
        *,
        via: SequenceNotStr[str] | Omit = omit,
        reason: str | Omit = omit,
        third_party_signed: room_join_params.ThirdPartySigned | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomJoinResponse:
        """
        _Note that this API takes either a room ID or alias, unlike_
        `/rooms/{roomId}/join`.

        This API starts a user's participation in a particular room, if that user is
        allowed to participate in that room. After this call, the client is allowed to
        see all current state events in the room, and all subsequent events associated
        with the room until the user leaves the room.

        After a user has joined a room, the room will appear as an entry in the response
        of the
        [`/initialSync`](https://spec.matrix.org/v1.18/client-server-api/#get_matrixclientv3initialsync)
        and
        [`/sync`](https://spec.matrix.org/v1.18/client-server-api/#get_matrixclientv3sync)
        APIs.

        Args:
          via: The servers to attempt to join the room through. One of the servers must be
              participating in the room.

          reason: Optional reason to be included as the `reason` on the subsequent membership
              event.

          third_party_signed: A signature of an `m.third_party_invite` token to prove that this user owns a
              third-party identity which has been invited to the room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id_or_alias:
            raise ValueError(f"Expected a non-empty value for `room_id_or_alias` but received {room_id_or_alias!r}")
        return self._post(
            path_template("/_matrix/client/v3/join/{room_id_or_alias}", room_id_or_alias=room_id_or_alias),
            body=maybe_transform(
                {
                    "reason": reason,
                    "third_party_signed": third_party_signed,
                },
                room_join_params.RoomJoinParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"via": via}, room_join_params.RoomJoinParams),
            ),
            cast_to=RoomJoinResponse,
        )

    def leave(
        self,
        room_id: str,
        *,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        This API stops a user participating in a particular room.

        If the user was already in the room, they will no longer be able to see new
        events in the room. If the room requires an invite to join, they will need to be
        re-invited before they can re-join.

        If the user was invited to the room, but had not joined, this call serves to
        reject the invite.

        Servers MAY additionally forget the room when this endpoint is called – just as
        if the user had also invoked
        [`/forget`](https://spec.matrix.org/v1.18/client-server-api/#post_matrixclientv3roomsroomidforget).
        Servers that do this, MUST inform clients about this behavior using the
        [`m.forget_forced_upon_leave`](https://spec.matrix.org/v1.18/client-server-api/#mforget_forced_upon_leave-capability)
        capability.

        If the server doesn't automatically forget the room, the user will still be
        allowed to retrieve history from the room which they were previously allowed to
        see.

        Args:
          reason: Optional reason to be included as the `reason` on the subsequent membership
              event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return self._post(
            path_template("/_matrix/client/v3/rooms/{room_id}/leave", room_id=room_id),
            body=maybe_transform({"reason": reason}, room_leave_params.RoomLeaveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRoomsResource(AsyncAPIResource):
    @cached_property
    def account_data(self) -> AsyncAccountDataResource:
        return AsyncAccountDataResource(self._client)

    @cached_property
    def state(self) -> AsyncStateResource:
        return AsyncStateResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRoomsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoomsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoomsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncRoomsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        creation_content: object | Omit = omit,
        initial_state: Iterable[room_create_params.InitialState] | Omit = omit,
        invite: SequenceNotStr[str] | Omit = omit,
        invite_3pid: Iterable[room_create_params.Invite3pid] | Omit = omit,
        is_direct: bool | Omit = omit,
        name: str | Omit = omit,
        power_level_content_override: object | Omit = omit,
        preset: Literal["private_chat", "public_chat", "trusted_private_chat"] | Omit = omit,
        room_alias_name: str | Omit = omit,
        room_version: str | Omit = omit,
        topic: str | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomCreateResponse:
        """
        Create a new room with various configuration options.

        The server MUST apply the normal state resolution rules when creating the new
        room, including checking power levels for each event. It MUST apply the events
        implied by the request in the following order:

        1. The `m.room.create` event itself. Must be the first event in the room.

        2. An `m.room.member` event for the creator to join the room. This is needed so
           the remaining events can be sent.

        3. A default `m.room.power_levels` event. Overridden by the
           `power_level_content_override` parameter.

           In [room versions](https://spec.matrix.org/v1.18/rooms) 1 through 11, the
           room creator (and not other members) will be given permission to send state
           events.

           In room versions 12 and later, the room creator is given infinite power level
           and cannot be specified in the `users` field of `m.room.power_levels`, so is
           not listed explicitly.

           **Note**: For `trusted_private_chat`, the users specified in the `invite`
           parameter SHOULD also be appended to `additional_creators` by the server, per
           the `creation_content` parameter.

           If the room's version is 12 or higher, the power level for sending
           `m.room.tombstone` events MUST explicitly be higher than `state_default`. For
           example, set to 150 instead of 100.

        4. An `m.room.canonical_alias` event if `room_alias_name` is given.

        5. Events set by the `preset`. Currently these are the `m.room.join_rules`,
           `m.room.history_visibility`, and `m.room.guest_access` state events.

        6. Events listed in `initial_state`, in the order that they are listed.

        7. Events implied by `name` and `topic` (`m.room.name` and `m.room.topic` state
           events).

        8. Invite events implied by `invite` and `invite_3pid` (`m.room.member` with
           `membership: invite` and `m.room.third_party_invite`).

        The available presets do the following with respect to room state:

        | Preset                 | `join_rules` | `history_visibility` | `guest_access` | Other                                                            |
        | ---------------------- | ------------ | -------------------- | -------------- | ---------------------------------------------------------------- |
        | `private_chat`         | `invite`     | `shared`             | `can_join`     |                                                                  |
        | `trusted_private_chat` | `invite`     | `shared`             | `can_join`     | All invitees are given the same power level as the room creator. |
        | `public_chat`          | `public`     | `shared`             | `forbidden`    |                                                                  |

        The server will create a `m.room.create` event in the room with the requesting
        user as the creator, alongside other keys provided in the `creation_content` or
        implied by behaviour of `creation_content`.

        Args:
          creation_content: Extra keys, such as `m.federate`, to be added to the content of the
              [`m.room.create`](https://spec.matrix.org/v1.18/client-server-api/#mroomcreate)
              event.

              The server will overwrite the following keys: `creator`, `room_version`. Future
              versions of the specification may allow the server to overwrite other keys.

              When using the `trusted_private_chat` preset, the server SHOULD combine
              `additional_creators` specified here and the `invite` array into the eventual
              `m.room.create` event's `additional_creators`, deduplicating between the two
              parameters.

          initial_state: A list of state events to set in the new room. This allows the user to override
              the default state events set in the new room. The expected format of the state
              events are an object with type, state_key and content keys set.

              Takes precedence over events set by `preset`, but gets overridden by `name` and
              `topic` keys.

          invite: A list of user IDs to invite to the room. This will tell the server to invite
              everyone in the list to the newly created room.

          invite_3pid: A list of objects representing third-party IDs to invite into the room.

          is_direct: This flag makes the server set the `is_direct` flag on the `m.room.member`
              events sent to the users in `invite` and `invite_3pid`. See
              [Direct Messaging](https://spec.matrix.org/v1.18/client-server-api/#direct-messaging)
              for more information.

          name: If this is included, an
              [`m.room.name`](https://spec.matrix.org/v1.18/client-server-api/#mroomname)
              event will be sent into the room to indicate the name for the room. This
              overwrites any
              [`m.room.name`](https://spec.matrix.org/v1.18/client-server-api/#mroomname)
              event in `initial_state`.

          power_level_content_override: The power level content to override in the default power level event. This
              object is applied on top of the generated
              [`m.room.power_levels`](https://spec.matrix.org/v1.18/client-server-api/#mroompower_levels)
              event content prior to it being sent to the room. Defaults to overriding
              nothing.

          preset: Convenience parameter for setting various default state events based on a
              preset.

              If unspecified, the server should use the `visibility` to determine which preset
              to use. A visibility of `public` equates to a preset of `public_chat` and
              `private` visibility equates to a preset of `private_chat`.

          room_alias_name: The desired room alias **local part**. If this is included, a room alias will be
              created and mapped to the newly created room. The alias will belong on the
              _same_ homeserver which created the room. For example, if this was set to "foo"
              and sent to the homeserver "example.com" the complete room alias would be
              `#foo:example.com`.

              The complete room alias will become the canonical alias for the room and an
              `m.room.canonical_alias` event will be sent into the room.

          room_version: The room version to set for the room. If not provided, the homeserver is to use
              its configured default. If provided, the homeserver will return a 400 error with
              the errcode `M_UNSUPPORTED_ROOM_VERSION` if it does not support the room
              version.

          topic: If this is included, an
              [`m.room.topic`](https://spec.matrix.org/v1.18/client-server-api/#mroomtopic)
              event with a `text/plain` mimetype will be sent into the room to indicate the
              topic for the room. This overwrites any
              [`m.room.topic`](https://spec.matrix.org/v1.18/client-server-api/#mroomtopic)
              event in `initial_state`.

          visibility: The room's visibility in the server's
              [published room directory](https://spec.matrix.org/v1.18/client-server-api#published-room-directory).
              Defaults to `private`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/_matrix/client/v3/createRoom",
            body=await async_maybe_transform(
                {
                    "creation_content": creation_content,
                    "initial_state": initial_state,
                    "invite": invite,
                    "invite_3pid": invite_3pid,
                    "is_direct": is_direct,
                    "name": name,
                    "power_level_content_override": power_level_content_override,
                    "preset": preset,
                    "room_alias_name": room_alias_name,
                    "room_version": room_version,
                    "topic": topic,
                    "visibility": visibility,
                },
                room_create_params.RoomCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoomCreateResponse,
        )

    async def join(
        self,
        room_id_or_alias: str,
        *,
        via: SequenceNotStr[str] | Omit = omit,
        reason: str | Omit = omit,
        third_party_signed: room_join_params.ThirdPartySigned | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomJoinResponse:
        """
        _Note that this API takes either a room ID or alias, unlike_
        `/rooms/{roomId}/join`.

        This API starts a user's participation in a particular room, if that user is
        allowed to participate in that room. After this call, the client is allowed to
        see all current state events in the room, and all subsequent events associated
        with the room until the user leaves the room.

        After a user has joined a room, the room will appear as an entry in the response
        of the
        [`/initialSync`](https://spec.matrix.org/v1.18/client-server-api/#get_matrixclientv3initialsync)
        and
        [`/sync`](https://spec.matrix.org/v1.18/client-server-api/#get_matrixclientv3sync)
        APIs.

        Args:
          via: The servers to attempt to join the room through. One of the servers must be
              participating in the room.

          reason: Optional reason to be included as the `reason` on the subsequent membership
              event.

          third_party_signed: A signature of an `m.third_party_invite` token to prove that this user owns a
              third-party identity which has been invited to the room.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id_or_alias:
            raise ValueError(f"Expected a non-empty value for `room_id_or_alias` but received {room_id_or_alias!r}")
        return await self._post(
            path_template("/_matrix/client/v3/join/{room_id_or_alias}", room_id_or_alias=room_id_or_alias),
            body=await async_maybe_transform(
                {
                    "reason": reason,
                    "third_party_signed": third_party_signed,
                },
                room_join_params.RoomJoinParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"via": via}, room_join_params.RoomJoinParams),
            ),
            cast_to=RoomJoinResponse,
        )

    async def leave(
        self,
        room_id: str,
        *,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        This API stops a user participating in a particular room.

        If the user was already in the room, they will no longer be able to see new
        events in the room. If the room requires an invite to join, they will need to be
        re-invited before they can re-join.

        If the user was invited to the room, but had not joined, this call serves to
        reject the invite.

        Servers MAY additionally forget the room when this endpoint is called – just as
        if the user had also invoked
        [`/forget`](https://spec.matrix.org/v1.18/client-server-api/#post_matrixclientv3roomsroomidforget).
        Servers that do this, MUST inform clients about this behavior using the
        [`m.forget_forced_upon_leave`](https://spec.matrix.org/v1.18/client-server-api/#mforget_forced_upon_leave-capability)
        capability.

        If the server doesn't automatically forget the room, the user will still be
        allowed to retrieve history from the room which they were previously allowed to
        see.

        Args:
          reason: Optional reason to be included as the `reason` on the subsequent membership
              event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return await self._post(
            path_template("/_matrix/client/v3/rooms/{room_id}/leave", room_id=room_id),
            body=await async_maybe_transform({"reason": reason}, room_leave_params.RoomLeaveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RoomsResourceWithRawResponse:
    def __init__(self, rooms: RoomsResource) -> None:
        self._rooms = rooms

        self.create = to_raw_response_wrapper(
            rooms.create,
        )
        self.join = to_raw_response_wrapper(
            rooms.join,
        )
        self.leave = to_raw_response_wrapper(
            rooms.leave,
        )

    @cached_property
    def account_data(self) -> AccountDataResourceWithRawResponse:
        return AccountDataResourceWithRawResponse(self._rooms.account_data)

    @cached_property
    def state(self) -> StateResourceWithRawResponse:
        return StateResourceWithRawResponse(self._rooms.state)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._rooms.events)


class AsyncRoomsResourceWithRawResponse:
    def __init__(self, rooms: AsyncRoomsResource) -> None:
        self._rooms = rooms

        self.create = async_to_raw_response_wrapper(
            rooms.create,
        )
        self.join = async_to_raw_response_wrapper(
            rooms.join,
        )
        self.leave = async_to_raw_response_wrapper(
            rooms.leave,
        )

    @cached_property
    def account_data(self) -> AsyncAccountDataResourceWithRawResponse:
        return AsyncAccountDataResourceWithRawResponse(self._rooms.account_data)

    @cached_property
    def state(self) -> AsyncStateResourceWithRawResponse:
        return AsyncStateResourceWithRawResponse(self._rooms.state)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._rooms.events)


class RoomsResourceWithStreamingResponse:
    def __init__(self, rooms: RoomsResource) -> None:
        self._rooms = rooms

        self.create = to_streamed_response_wrapper(
            rooms.create,
        )
        self.join = to_streamed_response_wrapper(
            rooms.join,
        )
        self.leave = to_streamed_response_wrapper(
            rooms.leave,
        )

    @cached_property
    def account_data(self) -> AccountDataResourceWithStreamingResponse:
        return AccountDataResourceWithStreamingResponse(self._rooms.account_data)

    @cached_property
    def state(self) -> StateResourceWithStreamingResponse:
        return StateResourceWithStreamingResponse(self._rooms.state)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._rooms.events)


class AsyncRoomsResourceWithStreamingResponse:
    def __init__(self, rooms: AsyncRoomsResource) -> None:
        self._rooms = rooms

        self.create = async_to_streamed_response_wrapper(
            rooms.create,
        )
        self.join = async_to_streamed_response_wrapper(
            rooms.join,
        )
        self.leave = async_to_streamed_response_wrapper(
            rooms.leave,
        )

    @cached_property
    def account_data(self) -> AsyncAccountDataResourceWithStreamingResponse:
        return AsyncAccountDataResourceWithStreamingResponse(self._rooms.account_data)

    @cached_property
    def state(self) -> AsyncStateResourceWithStreamingResponse:
        return AsyncStateResourceWithStreamingResponse(self._rooms.state)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._rooms.events)
