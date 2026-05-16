# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .reset import (
    ResetResource,
    AsyncResetResource,
    ResetResourceWithRawResponse,
    AsyncResetResourceWithRawResponse,
    ResetResourceWithStreamingResponse,
    AsyncResetResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.app.e2ee import recovery_code_verify_params
from .....types.app.e2ee.recovery_code_verify_response import RecoveryCodeVerifyResponse
from .....types.app.e2ee.recovery_code_mark_backed_up_response import RecoveryCodeMarkBackedUpResponse

__all__ = ["RecoveryCodeResource", "AsyncRecoveryCodeResource"]


class RecoveryCodeResource(SyncAPIResource):
    """First-party sign-in and encrypted messaging setup for Beeper Desktop."""

    @cached_property
    def reset(self) -> ResetResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return ResetResource(self._client)

    @cached_property
    def with_raw_response(self) -> RecoveryCodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return RecoveryCodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecoveryCodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return RecoveryCodeResourceWithStreamingResponse(self)

    def mark_backed_up(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecoveryCodeMarkBackedUpResponse:
        """Record that the user saved their recovery key."""
        return self._post(
            "/v1/app/e2ee/recovery-code/mark-backed-up",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecoveryCodeMarkBackedUpResponse,
        )

    def verify(
        self,
        *,
        recovery_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecoveryCodeVerifyResponse:
        """
        Unlock encrypted messages with the user recovery key.

        Args:
          recovery_code: Recovery key saved by the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/app/e2ee/recovery-code/verify",
            body=maybe_transform(
                {"recovery_code": recovery_code}, recovery_code_verify_params.RecoveryCodeVerifyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecoveryCodeVerifyResponse,
        )


class AsyncRecoveryCodeResource(AsyncAPIResource):
    """First-party sign-in and encrypted messaging setup for Beeper Desktop."""

    @cached_property
    def reset(self) -> AsyncResetResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncResetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRecoveryCodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecoveryCodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecoveryCodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncRecoveryCodeResourceWithStreamingResponse(self)

    async def mark_backed_up(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecoveryCodeMarkBackedUpResponse:
        """Record that the user saved their recovery key."""
        return await self._post(
            "/v1/app/e2ee/recovery-code/mark-backed-up",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecoveryCodeMarkBackedUpResponse,
        )

    async def verify(
        self,
        *,
        recovery_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecoveryCodeVerifyResponse:
        """
        Unlock encrypted messages with the user recovery key.

        Args:
          recovery_code: Recovery key saved by the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/app/e2ee/recovery-code/verify",
            body=await async_maybe_transform(
                {"recovery_code": recovery_code}, recovery_code_verify_params.RecoveryCodeVerifyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecoveryCodeVerifyResponse,
        )


class RecoveryCodeResourceWithRawResponse:
    def __init__(self, recovery_code: RecoveryCodeResource) -> None:
        self._recovery_code = recovery_code

        self.mark_backed_up = to_raw_response_wrapper(
            recovery_code.mark_backed_up,
        )
        self.verify = to_raw_response_wrapper(
            recovery_code.verify,
        )

    @cached_property
    def reset(self) -> ResetResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return ResetResourceWithRawResponse(self._recovery_code.reset)


class AsyncRecoveryCodeResourceWithRawResponse:
    def __init__(self, recovery_code: AsyncRecoveryCodeResource) -> None:
        self._recovery_code = recovery_code

        self.mark_backed_up = async_to_raw_response_wrapper(
            recovery_code.mark_backed_up,
        )
        self.verify = async_to_raw_response_wrapper(
            recovery_code.verify,
        )

    @cached_property
    def reset(self) -> AsyncResetResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncResetResourceWithRawResponse(self._recovery_code.reset)


class RecoveryCodeResourceWithStreamingResponse:
    def __init__(self, recovery_code: RecoveryCodeResource) -> None:
        self._recovery_code = recovery_code

        self.mark_backed_up = to_streamed_response_wrapper(
            recovery_code.mark_backed_up,
        )
        self.verify = to_streamed_response_wrapper(
            recovery_code.verify,
        )

    @cached_property
    def reset(self) -> ResetResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return ResetResourceWithStreamingResponse(self._recovery_code.reset)


class AsyncRecoveryCodeResourceWithStreamingResponse:
    def __init__(self, recovery_code: AsyncRecoveryCodeResource) -> None:
        self._recovery_code = recovery_code

        self.mark_backed_up = async_to_streamed_response_wrapper(
            recovery_code.mark_backed_up,
        )
        self.verify = async_to_streamed_response_wrapper(
            recovery_code.verify,
        )

    @cached_property
    def reset(self) -> AsyncResetResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncResetResourceWithStreamingResponse(self._recovery_code.reset)
