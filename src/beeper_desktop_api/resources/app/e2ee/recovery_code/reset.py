# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.app.e2ee.recovery_code import reset_create_params, reset_confirm_params
from .....types.app.e2ee.recovery_code.reset_create_response import ResetCreateResponse
from .....types.app.e2ee.recovery_code.reset_confirm_response import ResetConfirmResponse

__all__ = ["ResetResource", "AsyncResetResource"]


class ResetResource(SyncAPIResource):
    """First-party sign-in and encrypted messaging setup for Beeper Desktop."""

    @cached_property
    def with_raw_response(self) -> ResetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return ResetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return ResetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        recovery_code: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResetCreateResponse:
        """
        Create a new recovery key when the user cannot use the existing one.

        Args:
          recovery_code: Existing recovery key, if the user has it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/app/e2ee/recovery-code/reset",
            body=maybe_transform({"recovery_code": recovery_code}, reset_create_params.ResetCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetCreateResponse,
        )

    def confirm(
        self,
        *,
        recovery_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResetConfirmResponse:
        """
        Confirm that the new recovery key should be used for this account.

        Args:
          recovery_code: New recovery key returned by the reset step.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/app/e2ee/recovery-code/reset/confirm",
            body=maybe_transform({"recovery_code": recovery_code}, reset_confirm_params.ResetConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetConfirmResponse,
        )


class AsyncResetResource(AsyncAPIResource):
    """First-party sign-in and encrypted messaging setup for Beeper Desktop."""

    @cached_property
    def with_raw_response(self) -> AsyncResetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncResetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        recovery_code: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResetCreateResponse:
        """
        Create a new recovery key when the user cannot use the existing one.

        Args:
          recovery_code: Existing recovery key, if the user has it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/app/e2ee/recovery-code/reset",
            body=await async_maybe_transform({"recovery_code": recovery_code}, reset_create_params.ResetCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetCreateResponse,
        )

    async def confirm(
        self,
        *,
        recovery_code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResetConfirmResponse:
        """
        Confirm that the new recovery key should be used for this account.

        Args:
          recovery_code: New recovery key returned by the reset step.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/app/e2ee/recovery-code/reset/confirm",
            body=await async_maybe_transform({"recovery_code": recovery_code}, reset_confirm_params.ResetConfirmParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResetConfirmResponse,
        )


class ResetResourceWithRawResponse:
    def __init__(self, reset: ResetResource) -> None:
        self._reset = reset

        self.create = to_raw_response_wrapper(
            reset.create,
        )
        self.confirm = to_raw_response_wrapper(
            reset.confirm,
        )


class AsyncResetResourceWithRawResponse:
    def __init__(self, reset: AsyncResetResource) -> None:
        self._reset = reset

        self.create = async_to_raw_response_wrapper(
            reset.create,
        )
        self.confirm = async_to_raw_response_wrapper(
            reset.confirm,
        )


class ResetResourceWithStreamingResponse:
    def __init__(self, reset: ResetResource) -> None:
        self._reset = reset

        self.create = to_streamed_response_wrapper(
            reset.create,
        )
        self.confirm = to_streamed_response_wrapper(
            reset.confirm,
        )


class AsyncResetResourceWithStreamingResponse:
    def __init__(self, reset: AsyncResetResource) -> None:
        self._reset = reset

        self.create = async_to_streamed_response_wrapper(
            reset.create,
        )
        self.confirm = async_to_streamed_response_wrapper(
            reset.confirm,
        )
