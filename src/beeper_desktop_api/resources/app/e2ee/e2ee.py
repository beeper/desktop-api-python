# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .verification.verification import (
    VerificationResource,
    AsyncVerificationResource,
    VerificationResourceWithRawResponse,
    AsyncVerificationResourceWithRawResponse,
    VerificationResourceWithStreamingResponse,
    AsyncVerificationResourceWithStreamingResponse,
)
from .recovery_code.recovery_code import (
    RecoveryCodeResource,
    AsyncRecoveryCodeResource,
    RecoveryCodeResourceWithRawResponse,
    AsyncRecoveryCodeResourceWithRawResponse,
    RecoveryCodeResourceWithStreamingResponse,
    AsyncRecoveryCodeResourceWithStreamingResponse,
)

__all__ = ["E2eeResource", "AsyncE2eeResource"]


class E2eeResource(SyncAPIResource):
    """Manage encrypted messaging setup"""

    @cached_property
    def recovery_code(self) -> RecoveryCodeResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return RecoveryCodeResource(self._client)

    @cached_property
    def verification(self) -> VerificationResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return VerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> E2eeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return E2eeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> E2eeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return E2eeResourceWithStreamingResponse(self)


class AsyncE2eeResource(AsyncAPIResource):
    """Manage encrypted messaging setup"""

    @cached_property
    def recovery_code(self) -> AsyncRecoveryCodeResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncRecoveryCodeResource(self._client)

    @cached_property
    def verification(self) -> AsyncVerificationResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncVerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncE2eeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncE2eeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncE2eeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncE2eeResourceWithStreamingResponse(self)


class E2eeResourceWithRawResponse:
    def __init__(self, e2ee: E2eeResource) -> None:
        self._e2ee = e2ee

    @cached_property
    def recovery_code(self) -> RecoveryCodeResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return RecoveryCodeResourceWithRawResponse(self._e2ee.recovery_code)

    @cached_property
    def verification(self) -> VerificationResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return VerificationResourceWithRawResponse(self._e2ee.verification)


class AsyncE2eeResourceWithRawResponse:
    def __init__(self, e2ee: AsyncE2eeResource) -> None:
        self._e2ee = e2ee

    @cached_property
    def recovery_code(self) -> AsyncRecoveryCodeResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncRecoveryCodeResourceWithRawResponse(self._e2ee.recovery_code)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncVerificationResourceWithRawResponse(self._e2ee.verification)


class E2eeResourceWithStreamingResponse:
    def __init__(self, e2ee: E2eeResource) -> None:
        self._e2ee = e2ee

    @cached_property
    def recovery_code(self) -> RecoveryCodeResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return RecoveryCodeResourceWithStreamingResponse(self._e2ee.recovery_code)

    @cached_property
    def verification(self) -> VerificationResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return VerificationResourceWithStreamingResponse(self._e2ee.verification)


class AsyncE2eeResourceWithStreamingResponse:
    def __init__(self, e2ee: AsyncE2eeResource) -> None:
        self._e2ee = e2ee

    @cached_property
    def recovery_code(self) -> AsyncRecoveryCodeResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncRecoveryCodeResourceWithStreamingResponse(self._e2ee.recovery_code)

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncVerificationResourceWithStreamingResponse(self._e2ee.verification)
