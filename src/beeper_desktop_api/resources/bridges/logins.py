# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.bridges import login_remove_params
from ...types.bridge_login import BridgeLogin
from ...types.bridges.login_list_response import LoginListResponse
from ...types.bridges.login_remove_response import LoginRemoveResponse

__all__ = ["LoginsResource", "AsyncLoginsResource"]


class LoginsResource(SyncAPIResource):
    """
    Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
    """

    @cached_property
    def with_raw_response(self) -> LoginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return LoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return LoginsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        login_id: str,
        *,
        bridge_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BridgeLogin:
        """
        Get one bridge login.

        Args:
          bridge_id: Bridge ID.

          login_id: Bridge login ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_id:
            raise ValueError(f"Expected a non-empty value for `login_id` but received {login_id!r}")
        return self._get(
            path_template("/v1/bridges/{bridge_id}/logins/{login_id}", bridge_id=bridge_id, login_id=login_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeLogin,
        )

    def list(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginListResponse:
        """List bridge logins.

        A bridge login is a signed-in identity for a bridge and can
        contain one or more chat accounts.

        Args:
          bridge_id: Bridge ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return self._get(
            path_template("/v1/bridges/{bridge_id}/logins", bridge_id=bridge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginListResponse,
        )

    def remove(
        self,
        login_id: str,
        *,
        bridge_id: str,
        scope: Literal["current-device", "all-devices"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginRemoveResponse:
        """
        Remove a bridge login from this device or, when supported by the bridge, from
        all devices.

        Args:
          bridge_id: Bridge ID.

          login_id: Bridge login ID.

          scope: Where this bridge login should be removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_id:
            raise ValueError(f"Expected a non-empty value for `login_id` but received {login_id!r}")
        return self._post(
            path_template("/v1/bridges/{bridge_id}/logins/{login_id}/remove", bridge_id=bridge_id, login_id=login_id),
            body=maybe_transform({"scope": scope}, login_remove_params.LoginRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginRemoveResponse,
        )


class AsyncLoginsResource(AsyncAPIResource):
    """
    Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
    """

    @cached_property
    def with_raw_response(self) -> AsyncLoginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncLoginsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        login_id: str,
        *,
        bridge_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BridgeLogin:
        """
        Get one bridge login.

        Args:
          bridge_id: Bridge ID.

          login_id: Bridge login ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_id:
            raise ValueError(f"Expected a non-empty value for `login_id` but received {login_id!r}")
        return await self._get(
            path_template("/v1/bridges/{bridge_id}/logins/{login_id}", bridge_id=bridge_id, login_id=login_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeLogin,
        )

    async def list(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginListResponse:
        """List bridge logins.

        A bridge login is a signed-in identity for a bridge and can
        contain one or more chat accounts.

        Args:
          bridge_id: Bridge ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return await self._get(
            path_template("/v1/bridges/{bridge_id}/logins", bridge_id=bridge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginListResponse,
        )

    async def remove(
        self,
        login_id: str,
        *,
        bridge_id: str,
        scope: Literal["current-device", "all-devices"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginRemoveResponse:
        """
        Remove a bridge login from this device or, when supported by the bridge, from
        all devices.

        Args:
          bridge_id: Bridge ID.

          login_id: Bridge login ID.

          scope: Where this bridge login should be removed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_id:
            raise ValueError(f"Expected a non-empty value for `login_id` but received {login_id!r}")
        return await self._post(
            path_template("/v1/bridges/{bridge_id}/logins/{login_id}/remove", bridge_id=bridge_id, login_id=login_id),
            body=await async_maybe_transform({"scope": scope}, login_remove_params.LoginRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginRemoveResponse,
        )


class LoginsResourceWithRawResponse:
    def __init__(self, logins: LoginsResource) -> None:
        self._logins = logins

        self.retrieve = to_raw_response_wrapper(
            logins.retrieve,
        )
        self.list = to_raw_response_wrapper(
            logins.list,
        )
        self.remove = to_raw_response_wrapper(
            logins.remove,
        )


class AsyncLoginsResourceWithRawResponse:
    def __init__(self, logins: AsyncLoginsResource) -> None:
        self._logins = logins

        self.retrieve = async_to_raw_response_wrapper(
            logins.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            logins.list,
        )
        self.remove = async_to_raw_response_wrapper(
            logins.remove,
        )


class LoginsResourceWithStreamingResponse:
    def __init__(self, logins: LoginsResource) -> None:
        self._logins = logins

        self.retrieve = to_streamed_response_wrapper(
            logins.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            logins.list,
        )
        self.remove = to_streamed_response_wrapper(
            logins.remove,
        )


class AsyncLoginsResourceWithStreamingResponse:
    def __init__(self, logins: AsyncLoginsResource) -> None:
        self._logins = logins

        self.retrieve = async_to_streamed_response_wrapper(
            logins.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            logins.list,
        )
        self.remove = async_to_streamed_response_wrapper(
            logins.remove,
        )
