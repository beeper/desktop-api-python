# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .qr import (
    QrResource,
    AsyncQrResource,
    QrResourceWithRawResponse,
    AsyncQrResourceWithRawResponse,
    QrResourceWithStreamingResponse,
    AsyncQrResourceWithStreamingResponse,
)
from .sas import (
    SasResource,
    AsyncSasResource,
    SasResourceWithRawResponse,
    AsyncSasResourceWithRawResponse,
    SasResourceWithStreamingResponse,
    AsyncSasResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.app.e2ee import verification_cancel_params, verification_create_params
from .....types.app.e2ee.verification_accept_response import VerificationAcceptResponse
from .....types.app.e2ee.verification_cancel_response import VerificationCancelResponse
from .....types.app.e2ee.verification_create_response import VerificationCreateResponse

__all__ = ["VerificationResource", "AsyncVerificationResource"]


class VerificationResource(SyncAPIResource):
    """First-party sign-in and encrypted messaging setup for Beeper Desktop."""

    @cached_property
    def qr(self) -> QrResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return QrResource(self._client)

    @cached_property
    def sas(self) -> SasResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return SasResource(self._client)

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

    def create(
        self,
        *,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        """
        Start verifying this device from another signed-in device.

        Args:
          user_id: User ID to verify. Defaults to the signed-in user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/app/e2ee/verification",
            body=maybe_transform({"user_id": user_id}, verification_create_params.VerificationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCreateResponse,
        )

    def accept(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationAcceptResponse:
        """
        Accept an incoming device verification request.

        Args:
          verification_id: Verification ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return self._post(
            path_template("/v1/app/e2ee/verification/{verification_id}/accept", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationAcceptResponse,
        )

    def cancel(
        self,
        verification_id: str,
        *,
        code: str | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCancelResponse:
        """
        Cancel an active device verification request.

        Args:
          verification_id: Verification ID.

          code: Optional cancellation code.

          reason: Optional user-facing cancellation reason.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return self._post(
            path_template("/v1/app/e2ee/verification/{verification_id}/cancel", verification_id=verification_id),
            body=maybe_transform(
                {
                    "code": code,
                    "reason": reason,
                },
                verification_cancel_params.VerificationCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCancelResponse,
        )


class AsyncVerificationResource(AsyncAPIResource):
    """First-party sign-in and encrypted messaging setup for Beeper Desktop."""

    @cached_property
    def qr(self) -> AsyncQrResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncQrResource(self._client)

    @cached_property
    def sas(self) -> AsyncSasResource:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncSasResource(self._client)

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

    async def create(
        self,
        *,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCreateResponse:
        """
        Start verifying this device from another signed-in device.

        Args:
          user_id: User ID to verify. Defaults to the signed-in user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/app/e2ee/verification",
            body=await async_maybe_transform({"user_id": user_id}, verification_create_params.VerificationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCreateResponse,
        )

    async def accept(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationAcceptResponse:
        """
        Accept an incoming device verification request.

        Args:
          verification_id: Verification ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return await self._post(
            path_template("/v1/app/e2ee/verification/{verification_id}/accept", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationAcceptResponse,
        )

    async def cancel(
        self,
        verification_id: str,
        *,
        code: str | Omit = omit,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationCancelResponse:
        """
        Cancel an active device verification request.

        Args:
          verification_id: Verification ID.

          code: Optional cancellation code.

          reason: Optional user-facing cancellation reason.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return await self._post(
            path_template("/v1/app/e2ee/verification/{verification_id}/cancel", verification_id=verification_id),
            body=await async_maybe_transform(
                {
                    "code": code,
                    "reason": reason,
                },
                verification_cancel_params.VerificationCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCancelResponse,
        )


class VerificationResourceWithRawResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

        self.create = to_raw_response_wrapper(
            verification.create,
        )
        self.accept = to_raw_response_wrapper(
            verification.accept,
        )
        self.cancel = to_raw_response_wrapper(
            verification.cancel,
        )

    @cached_property
    def qr(self) -> QrResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return QrResourceWithRawResponse(self._verification.qr)

    @cached_property
    def sas(self) -> SasResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return SasResourceWithRawResponse(self._verification.sas)


class AsyncVerificationResourceWithRawResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

        self.create = async_to_raw_response_wrapper(
            verification.create,
        )
        self.accept = async_to_raw_response_wrapper(
            verification.accept,
        )
        self.cancel = async_to_raw_response_wrapper(
            verification.cancel,
        )

    @cached_property
    def qr(self) -> AsyncQrResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncQrResourceWithRawResponse(self._verification.qr)

    @cached_property
    def sas(self) -> AsyncSasResourceWithRawResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncSasResourceWithRawResponse(self._verification.sas)


class VerificationResourceWithStreamingResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

        self.create = to_streamed_response_wrapper(
            verification.create,
        )
        self.accept = to_streamed_response_wrapper(
            verification.accept,
        )
        self.cancel = to_streamed_response_wrapper(
            verification.cancel,
        )

    @cached_property
    def qr(self) -> QrResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return QrResourceWithStreamingResponse(self._verification.qr)

    @cached_property
    def sas(self) -> SasResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return SasResourceWithStreamingResponse(self._verification.sas)


class AsyncVerificationResourceWithStreamingResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

        self.create = async_to_streamed_response_wrapper(
            verification.create,
        )
        self.accept = async_to_streamed_response_wrapper(
            verification.accept,
        )
        self.cancel = async_to_streamed_response_wrapper(
            verification.cancel,
        )

    @cached_property
    def qr(self) -> AsyncQrResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncQrResourceWithStreamingResponse(self._verification.qr)

    @cached_property
    def sas(self) -> AsyncSasResourceWithStreamingResponse:
        """First-party sign-in and encrypted messaging setup for Beeper Desktop."""
        return AsyncSasResourceWithStreamingResponse(self._verification.sas)
