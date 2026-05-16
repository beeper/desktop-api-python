# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...._base_client import make_request_options
from ....types.matrix.bridges import room_create_dm_params, room_create_group_params
from ....types.matrix.bridges.room_create_dm_response import RoomCreateDmResponse
from ....types.matrix.bridges.room_create_group_response import RoomCreateGroupResponse

__all__ = ["RoomsResource", "AsyncRoomsResource"]


class RoomsResource(SyncAPIResource):
    """Matrix-compatible APIs for accounts and connected network bridges."""

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

    def create_dm(
        self,
        identifier: str,
        *,
        bridge_id: str,
        login_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomCreateDmResponse:
        """
        Create a direct chat with a user on the remote network.

        Args:
          login_id: An optional explicit login ID to do the action through.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._post(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/create_dm/{identifier}",
                bridge_id=bridge_id,
                identifier=identifier,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"login_id": login_id}, room_create_dm_params.RoomCreateDmParams),
            ),
            cast_to=RoomCreateDmResponse,
        )

    def create_group(
        self,
        group_type: str,
        *,
        bridge_id: str,
        login_id: str | Omit = omit,
        avatar: room_create_group_params.Avatar | Omit = omit,
        disappear: room_create_group_params.Disappear | Omit = omit,
        name: room_create_group_params.Name | Omit = omit,
        parent: object | Omit = omit,
        participants: SequenceNotStr[str] | Omit = omit,
        room_id: str | Omit = omit,
        topic: room_create_group_params.Topic | Omit = omit,
        type: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomCreateGroupResponse:
        """
        Create a group chat on the remote network.

        Args:
          login_id: An optional explicit login ID to do the action through.

          avatar: The `m.room.avatar` event content for the room.

          disappear: The `com.beeper.disappearing_timer` event content for the room.

          name: The `m.room.name` event content for the room.

          participants: The users to add to the group initially.

          room_id: An existing Matrix room ID to bridge to. The other parameters must be already in
              sync with the room state when using this parameter.

          topic: The `m.room.topic` event content for the room.

          type: The type of group to create.

          username: The public username for the created group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not group_type:
            raise ValueError(f"Expected a non-empty value for `group_type` but received {group_type!r}")
        return self._post(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/create_group/{group_type}",
                bridge_id=bridge_id,
                group_type=group_type,
            ),
            body=maybe_transform(
                {
                    "avatar": avatar,
                    "disappear": disappear,
                    "name": name,
                    "parent": parent,
                    "participants": participants,
                    "room_id": room_id,
                    "topic": topic,
                    "type": type,
                    "username": username,
                },
                room_create_group_params.RoomCreateGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"login_id": login_id}, room_create_group_params.RoomCreateGroupParams),
            ),
            cast_to=RoomCreateGroupResponse,
        )


class AsyncRoomsResource(AsyncAPIResource):
    """Matrix-compatible APIs for accounts and connected network bridges."""

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

    async def create_dm(
        self,
        identifier: str,
        *,
        bridge_id: str,
        login_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomCreateDmResponse:
        """
        Create a direct chat with a user on the remote network.

        Args:
          login_id: An optional explicit login ID to do the action through.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._post(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/create_dm/{identifier}",
                bridge_id=bridge_id,
                identifier=identifier,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"login_id": login_id}, room_create_dm_params.RoomCreateDmParams),
            ),
            cast_to=RoomCreateDmResponse,
        )

    async def create_group(
        self,
        group_type: str,
        *,
        bridge_id: str,
        login_id: str | Omit = omit,
        avatar: room_create_group_params.Avatar | Omit = omit,
        disappear: room_create_group_params.Disappear | Omit = omit,
        name: room_create_group_params.Name | Omit = omit,
        parent: object | Omit = omit,
        participants: SequenceNotStr[str] | Omit = omit,
        room_id: str | Omit = omit,
        topic: room_create_group_params.Topic | Omit = omit,
        type: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoomCreateGroupResponse:
        """
        Create a group chat on the remote network.

        Args:
          login_id: An optional explicit login ID to do the action through.

          avatar: The `m.room.avatar` event content for the room.

          disappear: The `com.beeper.disappearing_timer` event content for the room.

          name: The `m.room.name` event content for the room.

          participants: The users to add to the group initially.

          room_id: An existing Matrix room ID to bridge to. The other parameters must be already in
              sync with the room state when using this parameter.

          topic: The `m.room.topic` event content for the room.

          type: The type of group to create.

          username: The public username for the created group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not group_type:
            raise ValueError(f"Expected a non-empty value for `group_type` but received {group_type!r}")
        return await self._post(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/create_group/{group_type}",
                bridge_id=bridge_id,
                group_type=group_type,
            ),
            body=await async_maybe_transform(
                {
                    "avatar": avatar,
                    "disappear": disappear,
                    "name": name,
                    "parent": parent,
                    "participants": participants,
                    "room_id": room_id,
                    "topic": topic,
                    "type": type,
                    "username": username,
                },
                room_create_group_params.RoomCreateGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"login_id": login_id}, room_create_group_params.RoomCreateGroupParams
                ),
            ),
            cast_to=RoomCreateGroupResponse,
        )


class RoomsResourceWithRawResponse:
    def __init__(self, rooms: RoomsResource) -> None:
        self._rooms = rooms

        self.create_dm = to_raw_response_wrapper(
            rooms.create_dm,
        )
        self.create_group = to_raw_response_wrapper(
            rooms.create_group,
        )


class AsyncRoomsResourceWithRawResponse:
    def __init__(self, rooms: AsyncRoomsResource) -> None:
        self._rooms = rooms

        self.create_dm = async_to_raw_response_wrapper(
            rooms.create_dm,
        )
        self.create_group = async_to_raw_response_wrapper(
            rooms.create_group,
        )


class RoomsResourceWithStreamingResponse:
    def __init__(self, rooms: RoomsResource) -> None:
        self._rooms = rooms

        self.create_dm = to_streamed_response_wrapper(
            rooms.create_dm,
        )
        self.create_group = to_streamed_response_wrapper(
            rooms.create_group,
        )


class AsyncRoomsResourceWithStreamingResponse:
    def __init__(self, rooms: AsyncRoomsResource) -> None:
        self._rooms = rooms

        self.create_dm = async_to_streamed_response_wrapper(
            rooms.create_dm,
        )
        self.create_group = async_to_streamed_response_wrapper(
            rooms.create_group,
        )
