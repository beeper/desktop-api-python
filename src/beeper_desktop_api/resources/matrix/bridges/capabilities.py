# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.matrix.bridges.capability_retrieve_response import CapabilityRetrieveResponse

__all__ = ["CapabilitiesResource", "AsyncCapabilitiesResource"]


class CapabilitiesResource(SyncAPIResource):
    """Matrix-compatible APIs for accounts and connected network bridges."""

    @cached_property
    def with_raw_response(self) -> CapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return CapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return CapabilitiesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CapabilityRetrieveResponse:
        """
        Get bridge capabilities

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/capabilities",
                bridge_id=bridge_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CapabilityRetrieveResponse,
        )


class AsyncCapabilitiesResource(AsyncAPIResource):
    """Matrix-compatible APIs for accounts and connected network bridges."""

    @cached_property
    def with_raw_response(self) -> AsyncCapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncCapabilitiesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CapabilityRetrieveResponse:
        """
        Get bridge capabilities

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return await self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/capabilities",
                bridge_id=bridge_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CapabilityRetrieveResponse,
        )


class CapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.retrieve = to_raw_response_wrapper(
            capabilities.retrieve,
        )


class AsyncCapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.retrieve = async_to_raw_response_wrapper(
            capabilities.retrieve,
        )


class CapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.retrieve = to_streamed_response_wrapper(
            capabilities.retrieve,
        )


class AsyncCapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.retrieve = async_to_streamed_response_wrapper(
            capabilities.retrieve,
        )
