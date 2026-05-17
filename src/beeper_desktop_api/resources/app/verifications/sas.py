# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.app.verifications.sas_start_response import SASStartResponse
from ....types.app.verifications.sas_confirm_response import SASConfirmResponse

__all__ = ["SASResource", "AsyncSASResource"]


class SASResource(SyncAPIResource):
    """
    First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
    """

    @cached_property
    def with_raw_response(self) -> SASResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return SASResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SASResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return SASResourceWithStreamingResponse(self)

    def confirm(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SASConfirmResponse:
        """
        Confirm that the emoji or number sequence matches on both devices.

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
            path_template("/v1/app/setup/verifications/{verification_id}/sas/confirm", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SASConfirmResponse,
        )

    def start(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SASStartResponse:
        """
        Start emoji comparison for device verification.

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
            path_template("/v1/app/setup/verifications/{verification_id}/sas/start", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SASStartResponse,
        )


class AsyncSASResource(AsyncAPIResource):
    """
    First-party sign-in and encrypted messaging setup for Beeper Desktop and Beeper Server.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSASResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSASResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSASResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncSASResourceWithStreamingResponse(self)

    async def confirm(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SASConfirmResponse:
        """
        Confirm that the emoji or number sequence matches on both devices.

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
            path_template("/v1/app/setup/verifications/{verification_id}/sas/confirm", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SASConfirmResponse,
        )

    async def start(
        self,
        verification_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SASStartResponse:
        """
        Start emoji comparison for device verification.

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
            path_template("/v1/app/setup/verifications/{verification_id}/sas/start", verification_id=verification_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SASStartResponse,
        )


class SASResourceWithRawResponse:
    def __init__(self, sas: SASResource) -> None:
        self._sas = sas

        self.confirm = to_raw_response_wrapper(
            sas.confirm,
        )
        self.start = to_raw_response_wrapper(
            sas.start,
        )


class AsyncSASResourceWithRawResponse:
    def __init__(self, sas: AsyncSASResource) -> None:
        self._sas = sas

        self.confirm = async_to_raw_response_wrapper(
            sas.confirm,
        )
        self.start = async_to_raw_response_wrapper(
            sas.start,
        )


class SASResourceWithStreamingResponse:
    def __init__(self, sas: SASResource) -> None:
        self._sas = sas

        self.confirm = to_streamed_response_wrapper(
            sas.confirm,
        )
        self.start = to_streamed_response_wrapper(
            sas.start,
        )


class AsyncSASResourceWithStreamingResponse:
    def __init__(self, sas: AsyncSASResource) -> None:
        self._sas = sas

        self.confirm = async_to_streamed_response_wrapper(
            sas.confirm,
        )
        self.start = async_to_streamed_response_wrapper(
            sas.start,
        )
