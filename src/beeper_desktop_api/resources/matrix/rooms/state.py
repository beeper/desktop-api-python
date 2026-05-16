# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.matrix.rooms import state_retrieve_params
from ....types.matrix.rooms.state_list_response import StateListResponse
from ....types.matrix.rooms.state_retrieve_response import StateRetrieveResponse

__all__ = ["StateResource", "AsyncStateResource"]


class StateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return StateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return StateResourceWithStreamingResponse(self)

    def retrieve(
        self,
        state_key: str,
        *,
        room_id: str,
        event_type: str,
        format: Literal["content", "event"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StateRetrieveResponse:
        """Looks up the contents of a state event in a room.

        If the user is joined to the
        room then the state is taken from the current state of the room. If the user has
        left the room then the state is taken from the state of the room when they left.

        Args:
          format: The format to use for the returned data. `content` (the default) will return
              only the content of the state event. `event` will return the entire event in the
              usual format suitable for clients, including fields like event ID, sender and
              timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        if not event_type:
            raise ValueError(f"Expected a non-empty value for `event_type` but received {event_type!r}")
        if not state_key:
            raise ValueError(f"Expected a non-empty value for `state_key` but received {state_key!r}")
        return self._get(
            path_template(
                "/_matrix/client/v3/rooms/{room_id}/state/{event_type}/{state_key}",
                room_id=room_id,
                event_type=event_type,
                state_key=state_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, state_retrieve_params.StateRetrieveParams),
            ),
            cast_to=StateRetrieveResponse,
        )

    def list(
        self,
        room_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StateListResponse:
        """
        Get the state events for the current state of a room.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return self._get(
            path_template("/_matrix/client/v3/rooms/{room_id}/state", room_id=room_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateListResponse,
        )


class AsyncStateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncStateResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        state_key: str,
        *,
        room_id: str,
        event_type: str,
        format: Literal["content", "event"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StateRetrieveResponse:
        """Looks up the contents of a state event in a room.

        If the user is joined to the
        room then the state is taken from the current state of the room. If the user has
        left the room then the state is taken from the state of the room when they left.

        Args:
          format: The format to use for the returned data. `content` (the default) will return
              only the content of the state event. `event` will return the entire event in the
              usual format suitable for clients, including fields like event ID, sender and
              timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        if not event_type:
            raise ValueError(f"Expected a non-empty value for `event_type` but received {event_type!r}")
        if not state_key:
            raise ValueError(f"Expected a non-empty value for `state_key` but received {state_key!r}")
        return await self._get(
            path_template(
                "/_matrix/client/v3/rooms/{room_id}/state/{event_type}/{state_key}",
                room_id=room_id,
                event_type=event_type,
                state_key=state_key,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, state_retrieve_params.StateRetrieveParams),
            ),
            cast_to=StateRetrieveResponse,
        )

    async def list(
        self,
        room_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StateListResponse:
        """
        Get the state events for the current state of a room.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        return await self._get(
            path_template("/_matrix/client/v3/rooms/{room_id}/state", room_id=room_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateListResponse,
        )


class StateResourceWithRawResponse:
    def __init__(self, state: StateResource) -> None:
        self._state = state

        self.retrieve = to_raw_response_wrapper(
            state.retrieve,
        )
        self.list = to_raw_response_wrapper(
            state.list,
        )


class AsyncStateResourceWithRawResponse:
    def __init__(self, state: AsyncStateResource) -> None:
        self._state = state

        self.retrieve = async_to_raw_response_wrapper(
            state.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            state.list,
        )


class StateResourceWithStreamingResponse:
    def __init__(self, state: StateResource) -> None:
        self._state = state

        self.retrieve = to_streamed_response_wrapper(
            state.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            state.list,
        )


class AsyncStateResourceWithStreamingResponse:
    def __init__(self, state: AsyncStateResource) -> None:
        self._state = state

        self.retrieve = async_to_streamed_response_wrapper(
            state.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            state.list,
        )
