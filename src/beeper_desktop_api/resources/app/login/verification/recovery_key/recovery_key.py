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
from ......_types import Body, Query, Headers, NotGiven, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.app.login.verification import recovery_key_verify_params
from ......types.app.login.verification.recovery_key_verify_response import RecoveryKeyVerifyResponse

__all__ = ["RecoveryKeyResource", "AsyncRecoveryKeyResource"]


class RecoveryKeyResource(SyncAPIResource):
    """
    First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
    """

    @cached_property
    def reset(self) -> ResetResource:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return ResetResource(self._client)

    @cached_property
    def with_raw_response(self) -> RecoveryKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return RecoveryKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecoveryKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return RecoveryKeyResourceWithStreamingResponse(self)

    def verify(
        self,
        *,
        recovery_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecoveryKeyVerifyResponse:
        """
        Unlock encrypted messages with the user recovery key.

        Args:
          recovery_key: Recovery key saved by the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/app/setup/verification/recovery-key",
            body=maybe_transform({"recovery_key": recovery_key}, recovery_key_verify_params.RecoveryKeyVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecoveryKeyVerifyResponse,
        )


class AsyncRecoveryKeyResource(AsyncAPIResource):
    """
    First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
    """

    @cached_property
    def reset(self) -> AsyncResetResource:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncResetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRecoveryKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecoveryKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecoveryKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncRecoveryKeyResourceWithStreamingResponse(self)

    async def verify(
        self,
        *,
        recovery_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecoveryKeyVerifyResponse:
        """
        Unlock encrypted messages with the user recovery key.

        Args:
          recovery_key: Recovery key saved by the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/app/setup/verification/recovery-key",
            body=await async_maybe_transform(
                {"recovery_key": recovery_key}, recovery_key_verify_params.RecoveryKeyVerifyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecoveryKeyVerifyResponse,
        )


class RecoveryKeyResourceWithRawResponse:
    def __init__(self, recovery_key: RecoveryKeyResource) -> None:
        self._recovery_key = recovery_key

        self.verify = to_raw_response_wrapper(
            recovery_key.verify,
        )

    @cached_property
    def reset(self) -> ResetResourceWithRawResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return ResetResourceWithRawResponse(self._recovery_key.reset)


class AsyncRecoveryKeyResourceWithRawResponse:
    def __init__(self, recovery_key: AsyncRecoveryKeyResource) -> None:
        self._recovery_key = recovery_key

        self.verify = async_to_raw_response_wrapper(
            recovery_key.verify,
        )

    @cached_property
    def reset(self) -> AsyncResetResourceWithRawResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncResetResourceWithRawResponse(self._recovery_key.reset)


class RecoveryKeyResourceWithStreamingResponse:
    def __init__(self, recovery_key: RecoveryKeyResource) -> None:
        self._recovery_key = recovery_key

        self.verify = to_streamed_response_wrapper(
            recovery_key.verify,
        )

    @cached_property
    def reset(self) -> ResetResourceWithStreamingResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return ResetResourceWithStreamingResponse(self._recovery_key.reset)


class AsyncRecoveryKeyResourceWithStreamingResponse:
    def __init__(self, recovery_key: AsyncRecoveryKeyResource) -> None:
        self._recovery_key = recovery_key

        self.verify = async_to_streamed_response_wrapper(
            recovery_key.verify,
        )

    @cached_property
    def reset(self) -> AsyncResetResourceWithStreamingResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncResetResourceWithStreamingResponse(self._recovery_key.reset)
