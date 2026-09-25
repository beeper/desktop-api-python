# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.app import setup_email_params, setup_register_params, setup_response_params
from ...._base_client import make_request_options
from .recovery_key.recovery_key import (
    RecoveryKeyResource,
    AsyncRecoveryKeyResource,
    RecoveryKeyResourceWithRawResponse,
    AsyncRecoveryKeyResourceWithRawResponse,
    RecoveryKeyResourceWithStreamingResponse,
    AsyncRecoveryKeyResourceWithStreamingResponse,
)
from .verifications.verifications import (
    VerificationsResource,
    AsyncVerificationsResource,
    VerificationsResourceWithRawResponse,
    AsyncVerificationsResourceWithRawResponse,
    VerificationsResourceWithStreamingResponse,
    AsyncVerificationsResourceWithStreamingResponse,
)
from ....types.app.setup_start_response import SetupStartResponse
from ....types.app.setup_register_response import SetupRegisterResponse
from ....types.app.setup_response_response import SetupResponseResponse
from ....types.app.setup_retrieve_response import SetupRetrieveResponse

__all__ = ["SetupResource", "AsyncSetupResource"]


class SetupResource(SyncAPIResource):
    """Complete first-party Beeper app setup"""

    @cached_property
    def recovery_key(self) -> RecoveryKeyResource:
        """Manage recovery-key setup for encrypted messages"""
        return RecoveryKeyResource(self._client)

    @cached_property
    def verifications(self) -> VerificationsResource:
        """Manage device verification transactions"""
        return VerificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SetupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return SetupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SetupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return SetupResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupRetrieveResponse:
        """
        Return the current Beeper Desktop or Beeper Server sign-in and encrypted
        messaging setup state. This endpoint is public before sign-in so apps can
        discover that sign-in is needed; after sign-in, pass a read token.
        """
        return self._get(
            "/v1/app/setup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupRetrieveResponse,
        )

    def email(
        self,
        *,
        email: str,
        setup_request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send a sign-in code to the user email address for app setup.

        Args:
          email: Email address to send the sign-in code to.

          setup_request_id: Setup request ID returned by the start step.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/app/setup/email",
            body=maybe_transform(
                {
                    "email": email,
                    "setup_request_id": setup_request_id,
                },
                setup_email_params.SetupEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    def register(
        self,
        *,
        accept_terms: Literal[True],
        lead_token: str,
        setup_request_id: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupRegisterResponse:
        """
        Create a Beeper account after the user chooses a username and accepts the Terms
        of Use.

        Args:
          accept_terms: Confirms that the user agreed to our
              [terms of use](https://www.beeper.com/terms-onboarding) and has read our
              [privacy policy](https://www.beeper.com/privacy).

          lead_token: Registration token returned by Beeper.

          setup_request_id: Setup request ID returned by the start step.

          username: Username selected by the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/app/setup/register",
            body=maybe_transform(
                {
                    "accept_terms": accept_terms,
                    "lead_token": lead_token,
                    "setup_request_id": setup_request_id,
                    "username": username,
                },
                setup_register_params.SetupRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SetupRegisterResponse,
        )

    def response(
        self,
        *,
        response: str,
        setup_request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupResponseResponse:
        """Finish setup sign-in with the code sent to the user email address.

        If the user
        needs a new account, the response includes account creation copy and username
        suggestions.

        Args:
          response: Sign-in code from the user email.

          setup_request_id: Setup request ID returned by the start step.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            SetupResponseResponse,
            self._post(
                "/v1/app/setup/response",
                body=maybe_transform(
                    {
                        "response": response,
                        "setup_request_id": setup_request_id,
                    },
                    setup_response_params.SetupResponseParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    security={},
                ),
                cast_to=cast(
                    Any, SetupResponseResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def start(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupStartResponse:
        """Start setting up Beeper Desktop or Beeper Server.

        The flow supports existing
        Beeper accounts and new account creation.
        """
        return self._post(
            "/v1/app/setup/start",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SetupStartResponse,
        )


class AsyncSetupResource(AsyncAPIResource):
    """Complete first-party Beeper app setup"""

    @cached_property
    def recovery_key(self) -> AsyncRecoveryKeyResource:
        """Manage recovery-key setup for encrypted messages"""
        return AsyncRecoveryKeyResource(self._client)

    @cached_property
    def verifications(self) -> AsyncVerificationsResource:
        """Manage device verification transactions"""
        return AsyncVerificationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSetupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSetupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSetupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncSetupResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupRetrieveResponse:
        """
        Return the current Beeper Desktop or Beeper Server sign-in and encrypted
        messaging setup state. This endpoint is public before sign-in so apps can
        discover that sign-in is needed; after sign-in, pass a read token.
        """
        return await self._get(
            "/v1/app/setup",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetupRetrieveResponse,
        )

    async def email(
        self,
        *,
        email: str,
        setup_request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Send a sign-in code to the user email address for app setup.

        Args:
          email: Email address to send the sign-in code to.

          setup_request_id: Setup request ID returned by the start step.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/app/setup/email",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "setup_request_id": setup_request_id,
                },
                setup_email_params.SetupEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )

    async def register(
        self,
        *,
        accept_terms: Literal[True],
        lead_token: str,
        setup_request_id: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupRegisterResponse:
        """
        Create a Beeper account after the user chooses a username and accepts the Terms
        of Use.

        Args:
          accept_terms: Confirms that the user agreed to our
              [terms of use](https://www.beeper.com/terms-onboarding) and has read our
              [privacy policy](https://www.beeper.com/privacy).

          lead_token: Registration token returned by Beeper.

          setup_request_id: Setup request ID returned by the start step.

          username: Username selected by the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/app/setup/register",
            body=await async_maybe_transform(
                {
                    "accept_terms": accept_terms,
                    "lead_token": lead_token,
                    "setup_request_id": setup_request_id,
                    "username": username,
                },
                setup_register_params.SetupRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SetupRegisterResponse,
        )

    async def response(
        self,
        *,
        response: str,
        setup_request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupResponseResponse:
        """Finish setup sign-in with the code sent to the user email address.

        If the user
        needs a new account, the response includes account creation copy and username
        suggestions.

        Args:
          response: Sign-in code from the user email.

          setup_request_id: Setup request ID returned by the start step.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            SetupResponseResponse,
            await self._post(
                "/v1/app/setup/response",
                body=await async_maybe_transform(
                    {
                        "response": response,
                        "setup_request_id": setup_request_id,
                    },
                    setup_response_params.SetupResponseParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    security={},
                ),
                cast_to=cast(
                    Any, SetupResponseResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def start(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupStartResponse:
        """Start setting up Beeper Desktop or Beeper Server.

        The flow supports existing
        Beeper accounts and new account creation.
        """
        return await self._post(
            "/v1/app/setup/start",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=SetupStartResponse,
        )


class SetupResourceWithRawResponse:
    def __init__(self, setup: SetupResource) -> None:
        self._setup = setup

        self.retrieve = to_raw_response_wrapper(
            setup.retrieve,
        )
        self.email = to_raw_response_wrapper(
            setup.email,
        )
        self.register = to_raw_response_wrapper(
            setup.register,
        )
        self.response = to_raw_response_wrapper(
            setup.response,
        )
        self.start = to_raw_response_wrapper(
            setup.start,
        )

    @cached_property
    def recovery_key(self) -> RecoveryKeyResourceWithRawResponse:
        """Manage recovery-key setup for encrypted messages"""
        return RecoveryKeyResourceWithRawResponse(self._setup.recovery_key)

    @cached_property
    def verifications(self) -> VerificationsResourceWithRawResponse:
        """Manage device verification transactions"""
        return VerificationsResourceWithRawResponse(self._setup.verifications)


class AsyncSetupResourceWithRawResponse:
    def __init__(self, setup: AsyncSetupResource) -> None:
        self._setup = setup

        self.retrieve = async_to_raw_response_wrapper(
            setup.retrieve,
        )
        self.email = async_to_raw_response_wrapper(
            setup.email,
        )
        self.register = async_to_raw_response_wrapper(
            setup.register,
        )
        self.response = async_to_raw_response_wrapper(
            setup.response,
        )
        self.start = async_to_raw_response_wrapper(
            setup.start,
        )

    @cached_property
    def recovery_key(self) -> AsyncRecoveryKeyResourceWithRawResponse:
        """Manage recovery-key setup for encrypted messages"""
        return AsyncRecoveryKeyResourceWithRawResponse(self._setup.recovery_key)

    @cached_property
    def verifications(self) -> AsyncVerificationsResourceWithRawResponse:
        """Manage device verification transactions"""
        return AsyncVerificationsResourceWithRawResponse(self._setup.verifications)


class SetupResourceWithStreamingResponse:
    def __init__(self, setup: SetupResource) -> None:
        self._setup = setup

        self.retrieve = to_streamed_response_wrapper(
            setup.retrieve,
        )
        self.email = to_streamed_response_wrapper(
            setup.email,
        )
        self.register = to_streamed_response_wrapper(
            setup.register,
        )
        self.response = to_streamed_response_wrapper(
            setup.response,
        )
        self.start = to_streamed_response_wrapper(
            setup.start,
        )

    @cached_property
    def recovery_key(self) -> RecoveryKeyResourceWithStreamingResponse:
        """Manage recovery-key setup for encrypted messages"""
        return RecoveryKeyResourceWithStreamingResponse(self._setup.recovery_key)

    @cached_property
    def verifications(self) -> VerificationsResourceWithStreamingResponse:
        """Manage device verification transactions"""
        return VerificationsResourceWithStreamingResponse(self._setup.verifications)


class AsyncSetupResourceWithStreamingResponse:
    def __init__(self, setup: AsyncSetupResource) -> None:
        self._setup = setup

        self.retrieve = async_to_streamed_response_wrapper(
            setup.retrieve,
        )
        self.email = async_to_streamed_response_wrapper(
            setup.email,
        )
        self.register = async_to_streamed_response_wrapper(
            setup.register,
        )
        self.response = async_to_streamed_response_wrapper(
            setup.response,
        )
        self.start = async_to_streamed_response_wrapper(
            setup.start,
        )

    @cached_property
    def recovery_key(self) -> AsyncRecoveryKeyResourceWithStreamingResponse:
        """Manage recovery-key setup for encrypted messages"""
        return AsyncRecoveryKeyResourceWithStreamingResponse(self._setup.recovery_key)

    @cached_property
    def verifications(self) -> AsyncVerificationsResourceWithStreamingResponse:
        """Manage device verification transactions"""
        return AsyncVerificationsResourceWithStreamingResponse(self._setup.verifications)
