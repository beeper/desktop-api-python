# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
    SASResource,
    AsyncSASResource,
    SASResourceWithRawResponse,
    AsyncSASResourceWithRawResponse,
    SASResourceWithStreamingResponse,
    AsyncSASResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.app import verification_cancel_params, verification_create_params
from ...._base_client import make_request_options
from ....types.app.verification_list_response import VerificationListResponse
from ....types.app.verification_accept_response import VerificationAcceptResponse
from ....types.app.verification_cancel_response import VerificationCancelResponse
from ....types.app.verification_create_response import VerificationCreateResponse
from ....types.app.verification_retrieve_response import VerificationRetrieveResponse

__all__ = ["VerificationsResource", "AsyncVerificationsResource"]


class VerificationsResource(SyncAPIResource):
    """Manage device verification transactions"""

    @cached_property
    def qr(self) -> QrResource:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return QrResource(self._client)

    @cached_property
    def sas(self) -> SASResource:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return SASResource(self._client)

    @cached_property
    def with_raw_response(self) -> VerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return VerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return VerificationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        purpose: Literal["login", "device"] | Omit = omit,
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
          purpose: Why this verification is being started.

          user_id: Beeper user ID to verify. Defaults to the signed-in user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/app/setup/verifications",
            body=maybe_transform(
                {
                    "purpose": purpose,
                    "user_id": user_id,
                },
                verification_create_params.VerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCreateResponse,
        )

    def retrieve(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationRetrieveResponse:
        """
        Get the current state of a device verification transaction.

        Args:
          verification_id: Verification ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return self._get(
            path_template("/v1/app/setup/verifications/{verification_id}", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRetrieveResponse,
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
    ) -> VerificationListResponse:
        """List pending and active device verifications.

        Use this to recover state without
        a WebSocket connection.
        """
        return self._get(
            "/v1/app/setup/verifications",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationListResponse,
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
            path_template("/v1/app/setup/verifications/{verification_id}/accept", verification_id=verification_id),
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
            path_template("/v1/app/setup/verifications/{verification_id}/cancel", verification_id=verification_id),
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


class AsyncVerificationsResource(AsyncAPIResource):
    """Manage device verification transactions"""

    @cached_property
    def qr(self) -> AsyncQrResource:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncQrResource(self._client)

    @cached_property
    def sas(self) -> AsyncSASResource:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncSASResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncVerificationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        purpose: Literal["login", "device"] | Omit = omit,
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
          purpose: Why this verification is being started.

          user_id: Beeper user ID to verify. Defaults to the signed-in user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/app/setup/verifications",
            body=await async_maybe_transform(
                {
                    "purpose": purpose,
                    "user_id": user_id,
                },
                verification_create_params.VerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCreateResponse,
        )

    async def retrieve(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationRetrieveResponse:
        """
        Get the current state of a device verification transaction.

        Args:
          verification_id: Verification ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verification_id:
            raise ValueError(f"Expected a non-empty value for `verification_id` but received {verification_id!r}")
        return await self._get(
            path_template("/v1/app/setup/verifications/{verification_id}", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationRetrieveResponse,
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
    ) -> VerificationListResponse:
        """List pending and active device verifications.

        Use this to recover state without
        a WebSocket connection.
        """
        return await self._get(
            "/v1/app/setup/verifications",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationListResponse,
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
            path_template("/v1/app/setup/verifications/{verification_id}/accept", verification_id=verification_id),
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
            path_template("/v1/app/setup/verifications/{verification_id}/cancel", verification_id=verification_id),
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


class VerificationsResourceWithRawResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.create = to_raw_response_wrapper(
            verifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            verifications.retrieve,
        )
        self.list = to_raw_response_wrapper(
            verifications.list,
        )
        self.accept = to_raw_response_wrapper(
            verifications.accept,
        )
        self.cancel = to_raw_response_wrapper(
            verifications.cancel,
        )

    @cached_property
    def qr(self) -> QrResourceWithRawResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return QrResourceWithRawResponse(self._verifications.qr)

    @cached_property
    def sas(self) -> SASResourceWithRawResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return SASResourceWithRawResponse(self._verifications.sas)


class AsyncVerificationsResourceWithRawResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.create = async_to_raw_response_wrapper(
            verifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            verifications.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            verifications.list,
        )
        self.accept = async_to_raw_response_wrapper(
            verifications.accept,
        )
        self.cancel = async_to_raw_response_wrapper(
            verifications.cancel,
        )

    @cached_property
    def qr(self) -> AsyncQrResourceWithRawResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncQrResourceWithRawResponse(self._verifications.qr)

    @cached_property
    def sas(self) -> AsyncSASResourceWithRawResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncSASResourceWithRawResponse(self._verifications.sas)


class VerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: VerificationsResource) -> None:
        self._verifications = verifications

        self.create = to_streamed_response_wrapper(
            verifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            verifications.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            verifications.list,
        )
        self.accept = to_streamed_response_wrapper(
            verifications.accept,
        )
        self.cancel = to_streamed_response_wrapper(
            verifications.cancel,
        )

    @cached_property
    def qr(self) -> QrResourceWithStreamingResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return QrResourceWithStreamingResponse(self._verifications.qr)

    @cached_property
    def sas(self) -> SASResourceWithStreamingResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return SASResourceWithStreamingResponse(self._verifications.sas)


class AsyncVerificationsResourceWithStreamingResponse:
    def __init__(self, verifications: AsyncVerificationsResource) -> None:
        self._verifications = verifications

        self.create = async_to_streamed_response_wrapper(
            verifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            verifications.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            verifications.list,
        )
        self.accept = async_to_streamed_response_wrapper(
            verifications.accept,
        )
        self.cancel = async_to_streamed_response_wrapper(
            verifications.cancel,
        )

    @cached_property
    def qr(self) -> AsyncQrResourceWithStreamingResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncQrResourceWithStreamingResponse(self._verifications.qr)

    @cached_property
    def sas(self) -> AsyncSASResourceWithStreamingResponse:
        """
        First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
        """
        return AsyncSASResourceWithStreamingResponse(self._verifications.sas)
