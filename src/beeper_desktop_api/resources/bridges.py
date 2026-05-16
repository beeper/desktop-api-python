# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.bridge_list_response import BridgeListResponse

__all__ = ["BridgesResource", "AsyncBridgesResource"]


class BridgesResource(SyncAPIResource):
    """Manage bridge-backed account types and account availability"""

    @cached_property
    def with_raw_response(self) -> BridgesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return BridgesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BridgesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return BridgesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BridgeListResponse:
        """
        List bridge-backed account types that can be shown in add-account flows, grouped
        with connected accounts that use the same Account schema as GET /v1/accounts.
        """
        return self._get(
            "/v1/bridges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeListResponse,
        )


class AsyncBridgesResource(AsyncAPIResource):
    """Manage bridge-backed account types and account availability"""

    @cached_property
    def with_raw_response(self) -> AsyncBridgesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBridgesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBridgesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncBridgesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BridgeListResponse:
        """
        List bridge-backed account types that can be shown in add-account flows, grouped
        with connected accounts that use the same Account schema as GET /v1/accounts.
        """
        return await self._get(
            "/v1/bridges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeListResponse,
        )


class BridgesResourceWithRawResponse:
    def __init__(self, bridges: BridgesResource) -> None:
        self._bridges = bridges

        self.list = to_raw_response_wrapper(
            bridges.list,
        )


class AsyncBridgesResourceWithRawResponse:
    def __init__(self, bridges: AsyncBridgesResource) -> None:
        self._bridges = bridges

        self.list = async_to_raw_response_wrapper(
            bridges.list,
        )


class BridgesResourceWithStreamingResponse:
    def __init__(self, bridges: BridgesResource) -> None:
        self._bridges = bridges

        self.list = to_streamed_response_wrapper(
            bridges.list,
        )


class AsyncBridgesResourceWithStreamingResponse:
    def __init__(self, bridges: AsyncBridgesResource) -> None:
        self._bridges = bridges

        self.list = async_to_streamed_response_wrapper(
            bridges.list,
        )
