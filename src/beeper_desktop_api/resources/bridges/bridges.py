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
from .login_flows import (
    LoginFlowsResource,
    AsyncLoginFlowsResource,
    LoginFlowsResourceWithRawResponse,
    AsyncLoginFlowsResourceWithRawResponse,
    LoginFlowsResourceWithStreamingResponse,
    AsyncLoginFlowsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.bridge_list_response import BridgeListResponse
from .login_sessions.login_sessions import (
    LoginSessionsResource,
    AsyncLoginSessionsResource,
    LoginSessionsResourceWithRawResponse,
    AsyncLoginSessionsResourceWithRawResponse,
    LoginSessionsResourceWithStreamingResponse,
    AsyncLoginSessionsResourceWithStreamingResponse,
)
from ...types.bridge_retrieve_response import BridgeRetrieveResponse
from ...types.provisioning_capabilities import ProvisioningCapabilities

__all__ = ["BridgesResource", "AsyncBridgesResource"]


class BridgesResource(SyncAPIResource):
    """Manage bridge-backed account types, connections, and login sessions"""

    @cached_property
    def login_flows(self) -> LoginFlowsResource:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return LoginFlowsResource(self._client)

    @cached_property
    def login_sessions(self) -> LoginSessionsResource:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return LoginSessionsResource(self._client)

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
    ) -> BridgeRetrieveResponse:
        """
        Get one bridge, including the chat accounts connected through it.

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
            path_template("/v1/bridges/{bridge_id}", bridge_id=bridge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeRetrieveResponse,
        )

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
        """List available bridges.

        A bridge is a chat-network connector that can connect or
        reconnect chat accounts. Connected accounts use the same Account schema as GET
        /v1/accounts.
        """
        return self._get(
            "/v1/bridges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeListResponse,
        )

    def retrieve_capabilities(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProvisioningCapabilities:
        """Get advanced network capabilities for a bridge.

        This endpoint is intended for
        clients that build custom connect or chat-creation flows.

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
            path_template("/v1/bridges/{bridge_id}/capabilities", bridge_id=bridge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProvisioningCapabilities,
        )


class AsyncBridgesResource(AsyncAPIResource):
    """Manage bridge-backed account types, connections, and login sessions"""

    @cached_property
    def login_flows(self) -> AsyncLoginFlowsResource:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return AsyncLoginFlowsResource(self._client)

    @cached_property
    def login_sessions(self) -> AsyncLoginSessionsResource:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return AsyncLoginSessionsResource(self._client)

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
    ) -> BridgeRetrieveResponse:
        """
        Get one bridge, including the chat accounts connected through it.

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
            path_template("/v1/bridges/{bridge_id}", bridge_id=bridge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeRetrieveResponse,
        )

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
        """List available bridges.

        A bridge is a chat-network connector that can connect or
        reconnect chat accounts. Connected accounts use the same Account schema as GET
        /v1/accounts.
        """
        return await self._get(
            "/v1/bridges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BridgeListResponse,
        )

    async def retrieve_capabilities(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProvisioningCapabilities:
        """Get advanced network capabilities for a bridge.

        This endpoint is intended for
        clients that build custom connect or chat-creation flows.

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
            path_template("/v1/bridges/{bridge_id}/capabilities", bridge_id=bridge_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProvisioningCapabilities,
        )


class BridgesResourceWithRawResponse:
    def __init__(self, bridges: BridgesResource) -> None:
        self._bridges = bridges

        self.retrieve = to_raw_response_wrapper(
            bridges.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bridges.list,
        )
        self.retrieve_capabilities = to_raw_response_wrapper(
            bridges.retrieve_capabilities,
        )

    @cached_property
    def login_flows(self) -> LoginFlowsResourceWithRawResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return LoginFlowsResourceWithRawResponse(self._bridges.login_flows)

    @cached_property
    def login_sessions(self) -> LoginSessionsResourceWithRawResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return LoginSessionsResourceWithRawResponse(self._bridges.login_sessions)


class AsyncBridgesResourceWithRawResponse:
    def __init__(self, bridges: AsyncBridgesResource) -> None:
        self._bridges = bridges

        self.retrieve = async_to_raw_response_wrapper(
            bridges.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bridges.list,
        )
        self.retrieve_capabilities = async_to_raw_response_wrapper(
            bridges.retrieve_capabilities,
        )

    @cached_property
    def login_flows(self) -> AsyncLoginFlowsResourceWithRawResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return AsyncLoginFlowsResourceWithRawResponse(self._bridges.login_flows)

    @cached_property
    def login_sessions(self) -> AsyncLoginSessionsResourceWithRawResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return AsyncLoginSessionsResourceWithRawResponse(self._bridges.login_sessions)


class BridgesResourceWithStreamingResponse:
    def __init__(self, bridges: BridgesResource) -> None:
        self._bridges = bridges

        self.retrieve = to_streamed_response_wrapper(
            bridges.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bridges.list,
        )
        self.retrieve_capabilities = to_streamed_response_wrapper(
            bridges.retrieve_capabilities,
        )

    @cached_property
    def login_flows(self) -> LoginFlowsResourceWithStreamingResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return LoginFlowsResourceWithStreamingResponse(self._bridges.login_flows)

    @cached_property
    def login_sessions(self) -> LoginSessionsResourceWithStreamingResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return LoginSessionsResourceWithStreamingResponse(self._bridges.login_sessions)


class AsyncBridgesResourceWithStreamingResponse:
    def __init__(self, bridges: AsyncBridgesResource) -> None:
        self._bridges = bridges

        self.retrieve = async_to_streamed_response_wrapper(
            bridges.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bridges.list,
        )
        self.retrieve_capabilities = async_to_streamed_response_wrapper(
            bridges.retrieve_capabilities,
        )

    @cached_property
    def login_flows(self) -> AsyncLoginFlowsResourceWithStreamingResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return AsyncLoginFlowsResourceWithStreamingResponse(self._bridges.login_flows)

    @cached_property
    def login_sessions(self) -> AsyncLoginSessionsResourceWithStreamingResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return AsyncLoginSessionsResourceWithStreamingResponse(self._bridges.login_sessions)
