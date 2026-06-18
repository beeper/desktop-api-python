# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.app.verifications import qr_scan_params
from ....types.app.verifications.qr_scan_response import QrScanResponse
from ....types.app.verifications.qr_confirm_scanned_response import QrConfirmScannedResponse

__all__ = ["QrResource", "AsyncQrResource"]


class QrResource(SyncAPIResource):
    """
    First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
    """

    @cached_property
    def with_raw_response(self) -> QrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return QrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return QrResourceWithStreamingResponse(self)

    def confirm_scanned(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QrConfirmScannedResponse:
        """
        Confirm that another device scanned this device QR code.

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
            path_template(
                "/v1/app/setup/verifications/{verification_id}/qr/confirm-scanned", verification_id=verification_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QrConfirmScannedResponse,
        )

    def scan(
        self,
        *,
        data: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QrScanResponse:
        """
        Submit the QR code scanned from another signed-in device.

        Args:
          data: QR code payload scanned from the other device.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/app/setup/verifications/qr/scan",
            body=maybe_transform({"data": data}, qr_scan_params.QrScanParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QrScanResponse,
        )


class AsyncQrResource(AsyncAPIResource):
    """
    First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
    """

    @cached_property
    def with_raw_response(self) -> AsyncQrResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQrResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQrResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncQrResourceWithStreamingResponse(self)

    async def confirm_scanned(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QrConfirmScannedResponse:
        """
        Confirm that another device scanned this device QR code.

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
            path_template(
                "/v1/app/setup/verifications/{verification_id}/qr/confirm-scanned", verification_id=verification_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QrConfirmScannedResponse,
        )

    async def scan(
        self,
        *,
        data: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QrScanResponse:
        """
        Submit the QR code scanned from another signed-in device.

        Args:
          data: QR code payload scanned from the other device.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/app/setup/verifications/qr/scan",
            body=await async_maybe_transform({"data": data}, qr_scan_params.QrScanParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QrScanResponse,
        )


class QrResourceWithRawResponse:
    def __init__(self, qr: QrResource) -> None:
        self._qr = qr

        self.confirm_scanned = to_raw_response_wrapper(
            qr.confirm_scanned,
        )
        self.scan = to_raw_response_wrapper(
            qr.scan,
        )


class AsyncQrResourceWithRawResponse:
    def __init__(self, qr: AsyncQrResource) -> None:
        self._qr = qr

        self.confirm_scanned = async_to_raw_response_wrapper(
            qr.confirm_scanned,
        )
        self.scan = async_to_raw_response_wrapper(
            qr.scan,
        )


class QrResourceWithStreamingResponse:
    def __init__(self, qr: QrResource) -> None:
        self._qr = qr

        self.confirm_scanned = to_streamed_response_wrapper(
            qr.confirm_scanned,
        )
        self.scan = to_streamed_response_wrapper(
            qr.scan,
        )


class AsyncQrResourceWithStreamingResponse:
    def __init__(self, qr: AsyncQrResource) -> None:
        self._qr = qr

        self.confirm_scanned = async_to_streamed_response_wrapper(
            qr.confirm_scanned,
        )
        self.scan = async_to_streamed_response_wrapper(
            qr.scan,
        )
