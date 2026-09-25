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
from ..types.info_retrieve_response import InfoRetrieveResponse

__all__ = ["InfoResource", "AsyncInfoResource"]


class InfoResource(SyncAPIResource):
    """Server discovery and capability metadata.

    Use /v1/info before authentication setup.
    """

    @cached_property
    def with_raw_response(self) -> InfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return InfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return InfoResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InfoRetrieveResponse:
        """
        Returns app, platform, server, endpoint discovery, OAuth, and WebSocket metadata
        for this Beeper Client API server.
        """
        return self._get(
            "/v1/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=InfoRetrieveResponse,
        )


class AsyncInfoResource(AsyncAPIResource):
    """Server discovery and capability metadata.

    Use /v1/info before authentication setup.
    """

    @cached_property
    def with_raw_response(self) -> AsyncInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncInfoResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InfoRetrieveResponse:
        """
        Returns app, platform, server, endpoint discovery, OAuth, and WebSocket metadata
        for this Beeper Client API server.
        """
        return await self._get(
            "/v1/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=InfoRetrieveResponse,
        )


class InfoResourceWithRawResponse:
    def __init__(self, info: InfoResource) -> None:
        self._info = info

        self.retrieve = to_raw_response_wrapper(
            info.retrieve,
        )


class AsyncInfoResourceWithRawResponse:
    def __init__(self, info: AsyncInfoResource) -> None:
        self._info = info

        self.retrieve = async_to_raw_response_wrapper(
            info.retrieve,
        )


class InfoResourceWithStreamingResponse:
    def __init__(self, info: InfoResource) -> None:
        self._info = info

        self.retrieve = to_streamed_response_wrapper(
            info.retrieve,
        )


class AsyncInfoResourceWithStreamingResponse:
    def __init__(self, info: AsyncInfoResource) -> None:
        self._info = info

        self.retrieve = async_to_streamed_response_wrapper(
            info.retrieve,
        )
