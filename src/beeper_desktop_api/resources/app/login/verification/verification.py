# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from .recovery_key.recovery_key import (
    RecoveryKeyResource,
    AsyncRecoveryKeyResource,
    RecoveryKeyResourceWithRawResponse,
    AsyncRecoveryKeyResourceWithRawResponse,
    RecoveryKeyResourceWithStreamingResponse,
    AsyncRecoveryKeyResourceWithStreamingResponse,
)

__all__ = ["VerificationResource", "AsyncVerificationResource"]


class VerificationResource(SyncAPIResource):
    @cached_property
    def recovery_key(self) -> RecoveryKeyResource:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return RecoveryKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> VerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return VerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return VerificationResourceWithStreamingResponse(self)


class AsyncVerificationResource(AsyncAPIResource):
    @cached_property
    def recovery_key(self) -> AsyncRecoveryKeyResource:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncRecoveryKeyResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncVerificationResourceWithStreamingResponse(self)


class VerificationResourceWithRawResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

    @cached_property
    def recovery_key(self) -> RecoveryKeyResourceWithRawResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return RecoveryKeyResourceWithRawResponse(self._verification.recovery_key)


class AsyncVerificationResourceWithRawResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

    @cached_property
    def recovery_key(self) -> AsyncRecoveryKeyResourceWithRawResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncRecoveryKeyResourceWithRawResponse(self._verification.recovery_key)


class VerificationResourceWithStreamingResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

    @cached_property
    def recovery_key(self) -> RecoveryKeyResourceWithStreamingResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return RecoveryKeyResourceWithStreamingResponse(self._verification.recovery_key)


class AsyncVerificationResourceWithStreamingResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

    @cached_property
    def recovery_key(self) -> AsyncRecoveryKeyResourceWithStreamingResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncRecoveryKeyResourceWithStreamingResponse(self._verification.recovery_key)
