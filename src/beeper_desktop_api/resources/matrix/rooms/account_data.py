# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.matrix.rooms import account_data_update_params

__all__ = ["AccountDataResource", "AsyncAccountDataResource"]


class AccountDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AccountDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AccountDataResourceWithStreamingResponse(self)

    def retrieve(
        self,
        type: str,
        *,
        user_id: str,
        room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get some account data for the client on a given room.

        This config is only
        visible to the user that set the account data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return self._get(
            path_template(
                "/_matrix/client/v3/user/{user_id}/rooms/{room_id}/account_data/{type}",
                user_id=user_id,
                room_id=room_id,
                type=type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update(
        self,
        type: str,
        *,
        user_id: str,
        room_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Set some account data for the client on a given room.

        This config is only
        visible to the user that set the account data. The config will be delivered to
        clients in the per-room entries via
        [/sync](https://spec.matrix.org/v1.18/client-server-api/#get_matrixclientv3sync).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return self._put(
            path_template(
                "/_matrix/client/v3/user/{user_id}/rooms/{room_id}/account_data/{type}",
                user_id=user_id,
                room_id=room_id,
                type=type,
            ),
            body=maybe_transform(body, account_data_update_params.AccountDataUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAccountDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncAccountDataResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        type: str,
        *,
        user_id: str,
        room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Get some account data for the client on a given room.

        This config is only
        visible to the user that set the account data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return await self._get(
            path_template(
                "/_matrix/client/v3/user/{user_id}/rooms/{room_id}/account_data/{type}",
                user_id=user_id,
                room_id=room_id,
                type=type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update(
        self,
        type: str,
        *,
        user_id: str,
        room_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Set some account data for the client on a given room.

        This config is only
        visible to the user that set the account data. The config will be delivered to
        clients in the per-room entries via
        [/sync](https://spec.matrix.org/v1.18/client-server-api/#get_matrixclientv3sync).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not room_id:
            raise ValueError(f"Expected a non-empty value for `room_id` but received {room_id!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return await self._put(
            path_template(
                "/_matrix/client/v3/user/{user_id}/rooms/{room_id}/account_data/{type}",
                user_id=user_id,
                room_id=room_id,
                type=type,
            ),
            body=await async_maybe_transform(body, account_data_update_params.AccountDataUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AccountDataResourceWithRawResponse:
    def __init__(self, account_data: AccountDataResource) -> None:
        self._account_data = account_data

        self.retrieve = to_raw_response_wrapper(
            account_data.retrieve,
        )
        self.update = to_raw_response_wrapper(
            account_data.update,
        )


class AsyncAccountDataResourceWithRawResponse:
    def __init__(self, account_data: AsyncAccountDataResource) -> None:
        self._account_data = account_data

        self.retrieve = async_to_raw_response_wrapper(
            account_data.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            account_data.update,
        )


class AccountDataResourceWithStreamingResponse:
    def __init__(self, account_data: AccountDataResource) -> None:
        self._account_data = account_data

        self.retrieve = to_streamed_response_wrapper(
            account_data.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            account_data.update,
        )


class AsyncAccountDataResourceWithStreamingResponse:
    def __init__(self, account_data: AsyncAccountDataResource) -> None:
        self._account_data = account_data

        self.retrieve = async_to_streamed_response_wrapper(
            account_data.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            account_data.update,
        )
