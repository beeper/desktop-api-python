# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.bridges.login_flow_list_response import LoginFlowListResponse

__all__ = ["LoginFlowsResource", "AsyncLoginFlowsResource"]


class LoginFlowsResource(SyncAPIResource):
    """
    Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
    """

    @cached_property
    def with_raw_response(self) -> LoginFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return LoginFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return LoginFlowsResourceWithStreamingResponse(self)

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
    ) -> LoginFlowListResponse:
        """List connect and reconnect flow options for a bridge.

        Use a flowID when creating
        a bridge login session.

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
            path_template("/v1/bridges/{bridge_id}/login-flows", bridge_id=bridge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginFlowListResponse,
        )


class AsyncLoginFlowsResource(AsyncAPIResource):
    """
    Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
    """

    @cached_property
    def with_raw_response(self) -> AsyncLoginFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoginFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncLoginFlowsResourceWithStreamingResponse(self)

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
    ) -> LoginFlowListResponse:
        """List connect and reconnect flow options for a bridge.

        Use a flowID when creating
        a bridge login session.

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
            path_template("/v1/bridges/{bridge_id}/login-flows", bridge_id=bridge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginFlowListResponse,
        )


class LoginFlowsResourceWithRawResponse:
    def __init__(self, login_flows: LoginFlowsResource) -> None:
        self._login_flows = login_flows

        self.list = to_raw_response_wrapper(
            login_flows.list,
        )


class AsyncLoginFlowsResourceWithRawResponse:
    def __init__(self, login_flows: AsyncLoginFlowsResource) -> None:
        self._login_flows = login_flows

        self.list = async_to_raw_response_wrapper(
            login_flows.list,
        )


class LoginFlowsResourceWithStreamingResponse:
    def __init__(self, login_flows: LoginFlowsResource) -> None:
        self._login_flows = login_flows

        self.list = to_streamed_response_wrapper(
            login_flows.list,
        )


class AsyncLoginFlowsResourceWithStreamingResponse:
    def __init__(self, login_flows: AsyncLoginFlowsResource) -> None:
        self._login_flows = login_flows

        self.list = async_to_streamed_response_wrapper(
            login_flows.list,
        )
