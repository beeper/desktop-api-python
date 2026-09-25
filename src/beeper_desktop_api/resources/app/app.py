# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .setup.setup import (
    SetupResource,
    AsyncSetupResource,
    SetupResourceWithRawResponse,
    AsyncSetupResourceWithRawResponse,
    SetupResourceWithStreamingResponse,
    AsyncSetupResourceWithStreamingResponse,
)

__all__ = ["AppResource", "AsyncAppResource"]


class AppResource(SyncAPIResource):
    """Manage Beeper account setup and encrypted messaging setup"""

    @cached_property
    def setup(self) -> SetupResource:
        """Complete first-party Beeper app setup"""
        return SetupResource(self._client)

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


class AsyncAppResource(AsyncAPIResource):
    """Manage Beeper account setup and encrypted messaging setup"""

    @cached_property
    def setup(self) -> AsyncSetupResource:
        """Complete first-party Beeper app setup"""
        return AsyncSetupResource(self._client)

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


class AppResourceWithRawResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

    @cached_property
    def setup(self) -> SetupResourceWithRawResponse:
        """Complete first-party Beeper app setup"""
        return SetupResourceWithRawResponse(self._app.setup)


class AsyncAppResourceWithRawResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

    @cached_property
    def setup(self) -> AsyncSetupResourceWithRawResponse:
        """Complete first-party Beeper app setup"""
        return AsyncSetupResourceWithRawResponse(self._app.setup)


class AppResourceWithStreamingResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

    @cached_property
    def setup(self) -> SetupResourceWithStreamingResponse:
        """Complete first-party Beeper app setup"""
        return SetupResourceWithStreamingResponse(self._app.setup)


class AsyncAppResourceWithStreamingResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

    @cached_property
    def setup(self) -> AsyncSetupResourceWithStreamingResponse:
        """Complete first-party Beeper app setup"""
        return AsyncSetupResourceWithStreamingResponse(self._app.setup)
