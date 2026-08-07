# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .login.login import (
    LoginResource,
    AsyncLoginResource,
    LoginResourceWithRawResponse,
    AsyncLoginResourceWithRawResponse,
    LoginResourceWithStreamingResponse,
    AsyncLoginResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .verifications.verifications import (
    VerificationsResource,
    AsyncVerificationsResource,
    VerificationsResourceWithRawResponse,
    AsyncVerificationsResourceWithRawResponse,
    VerificationsResourceWithStreamingResponse,
    AsyncVerificationsResourceWithStreamingResponse,
)
from ...types.app_session_response import AppSessionResponse

__all__ = ["AppResource", "AsyncAppResource"]


class AppResource(SyncAPIResource):
    """Manage Beeper app login and encrypted messaging setup"""

    @cached_property
    def login(self) -> LoginResource:
        """Complete first-party Beeper app login"""
        return LoginResource(self._client)

    @cached_property
    def verifications(self) -> VerificationsResource:
        """Manage device verification transactions"""
        return VerificationsResource(self._client)

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

    def session(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppSessionResponse:
        """
        Return the current Beeper Desktop or Beeper Server sign-in and encrypted
        messaging setup state. This endpoint is public before sign-in so apps can
        discover that sign-in is needed; after sign-in, pass a read token.
        """
        return self._get(
            "/v1/app/setup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppSessionResponse,
        )


class AsyncAppResource(AsyncAPIResource):
    """Manage Beeper app login and encrypted messaging setup"""

    @cached_property
    def login(self) -> AsyncLoginResource:
        """Complete first-party Beeper app login"""
        return AsyncLoginResource(self._client)

    @cached_property
    def verifications(self) -> AsyncVerificationsResource:
        """Manage device verification transactions"""
        return AsyncVerificationsResource(self._client)

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

    async def session(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppSessionResponse:
        """
        Return the current Beeper Desktop or Beeper Server sign-in and encrypted
        messaging setup state. This endpoint is public before sign-in so apps can
        discover that sign-in is needed; after sign-in, pass a read token.
        """
        return await self._get(
            "/v1/app/setup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppSessionResponse,
        )


class AppResourceWithRawResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.session = to_raw_response_wrapper(
            app.session,
        )

    @cached_property
    def login(self) -> LoginResourceWithRawResponse:
        """Complete first-party Beeper app login"""
        return LoginResourceWithRawResponse(self._app.login)

    @cached_property
    def verifications(self) -> VerificationsResourceWithRawResponse:
        """Manage device verification transactions"""
        return VerificationsResourceWithRawResponse(self._app.verifications)


class AsyncAppResourceWithRawResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.session = async_to_raw_response_wrapper(
            app.session,
        )

    @cached_property
    def login(self) -> AsyncLoginResourceWithRawResponse:
        """Complete first-party Beeper app login"""
        return AsyncLoginResourceWithRawResponse(self._app.login)

    @cached_property
    def verifications(self) -> AsyncVerificationsResourceWithRawResponse:
        """Manage device verification transactions"""
        return AsyncVerificationsResourceWithRawResponse(self._app.verifications)


class AppResourceWithStreamingResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.session = to_streamed_response_wrapper(
            app.session,
        )

    @cached_property
    def login(self) -> LoginResourceWithStreamingResponse:
        """Complete first-party Beeper app login"""
        return LoginResourceWithStreamingResponse(self._app.login)

    @cached_property
    def verifications(self) -> VerificationsResourceWithStreamingResponse:
        """Manage device verification transactions"""
        return VerificationsResourceWithStreamingResponse(self._app.verifications)


class AsyncAppResourceWithStreamingResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.session = async_to_streamed_response_wrapper(
            app.session,
        )

    @cached_property
    def login(self) -> AsyncLoginResourceWithStreamingResponse:
        """Complete first-party Beeper app login"""
        return AsyncLoginResourceWithStreamingResponse(self._app.login)

    @cached_property
    def verifications(self) -> AsyncVerificationsResourceWithStreamingResponse:
        """Manage device verification transactions"""
        return AsyncVerificationsResourceWithStreamingResponse(self._app.verifications)
