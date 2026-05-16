# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .login import (
    LoginResource,
    AsyncLoginResource,
    LoginResourceWithRawResponse,
    AsyncLoginResourceWithRawResponse,
    LoginResourceWithStreamingResponse,
    AsyncLoginResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from .e2ee.e2ee import (
    E2eeResource,
    AsyncE2eeResource,
    E2eeResourceWithRawResponse,
    AsyncE2eeResourceWithRawResponse,
    E2eeResourceWithStreamingResponse,
    AsyncE2eeResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.app_status_response import AppStatusResponse

__all__ = ["AppResource", "AsyncAppResource"]


class AppResource(SyncAPIResource):
    """Manage Beeper app login and encrypted messaging setup"""

    @cached_property
    def login(self) -> LoginResource:
        """Complete first-party Beeper app login"""
        return LoginResource(self._client)

    @cached_property
    def e2ee(self) -> E2eeResource:
        """Manage encrypted messaging setup"""
        return E2eeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AppResourceWithStreamingResponse(self)

    def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppStatusResponse:
        """
        Return the current Beeper Desktop sign-in and encrypted messaging setup state.
        This endpoint is public before sign-in so apps can discover that login is
        needed; after sign-in, pass a read token.
        """
        return self._get(
            "/v1/app/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppStatusResponse,
        )


class AsyncAppResource(AsyncAPIResource):
    """Manage Beeper app login and encrypted messaging setup"""

    @cached_property
    def login(self) -> AsyncLoginResource:
        """Complete first-party Beeper app login"""
        return AsyncLoginResource(self._client)

    @cached_property
    def e2ee(self) -> AsyncE2eeResource:
        """Manage encrypted messaging setup"""
        return AsyncE2eeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncAppResourceWithStreamingResponse(self)

    async def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppStatusResponse:
        """
        Return the current Beeper Desktop sign-in and encrypted messaging setup state.
        This endpoint is public before sign-in so apps can discover that login is
        needed; after sign-in, pass a read token.
        """
        return await self._get(
            "/v1/app/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppStatusResponse,
        )


class AppResourceWithRawResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.status = to_raw_response_wrapper(
            app.status,
        )

    @cached_property
    def login(self) -> LoginResourceWithRawResponse:
        """Complete first-party Beeper app login"""
        return LoginResourceWithRawResponse(self._app.login)

    @cached_property
    def e2ee(self) -> E2eeResourceWithRawResponse:
        """Manage encrypted messaging setup"""
        return E2eeResourceWithRawResponse(self._app.e2ee)


class AsyncAppResourceWithRawResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.status = async_to_raw_response_wrapper(
            app.status,
        )

    @cached_property
    def login(self) -> AsyncLoginResourceWithRawResponse:
        """Complete first-party Beeper app login"""
        return AsyncLoginResourceWithRawResponse(self._app.login)

    @cached_property
    def e2ee(self) -> AsyncE2eeResourceWithRawResponse:
        """Manage encrypted messaging setup"""
        return AsyncE2eeResourceWithRawResponse(self._app.e2ee)


class AppResourceWithStreamingResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.status = to_streamed_response_wrapper(
            app.status,
        )

    @cached_property
    def login(self) -> LoginResourceWithStreamingResponse:
        """Complete first-party Beeper app login"""
        return LoginResourceWithStreamingResponse(self._app.login)

    @cached_property
    def e2ee(self) -> E2eeResourceWithStreamingResponse:
        """Manage encrypted messaging setup"""
        return E2eeResourceWithStreamingResponse(self._app.e2ee)


class AsyncAppResourceWithStreamingResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.status = async_to_streamed_response_wrapper(
            app.status,
        )

    @cached_property
    def login(self) -> AsyncLoginResourceWithStreamingResponse:
        """Complete first-party Beeper app login"""
        return AsyncLoginResourceWithStreamingResponse(self._app.login)

    @cached_property
    def e2ee(self) -> AsyncE2eeResourceWithStreamingResponse:
        """Manage encrypted messaging setup"""
        return AsyncE2eeResourceWithStreamingResponse(self._app.e2ee)
