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
from ....types.app import login_email_params, login_register_params, login_response_params
from ...._base_client import make_request_options
from .verification.verification import (
    VerificationResource,
    AsyncVerificationResource,
    VerificationResourceWithRawResponse,
    AsyncVerificationResourceWithRawResponse,
    VerificationResourceWithStreamingResponse,
    AsyncVerificationResourceWithStreamingResponse,
)
from ....types.app.login_start_response import LoginStartResponse
from ....types.app.login_register_response import LoginRegisterResponse
from ....types.app.login_response_response import LoginResponseResponse

__all__ = ["LoginResource", "AsyncLoginResource"]


class LoginResource(SyncAPIResource):
    """Complete first-party Beeper app login"""

    @cached_property
    def verification(self) -> VerificationResource:
        return VerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> LoginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return LoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return LoginResourceWithStreamingResponse(self)

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
                login_email_params.LoginEmailParams,
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
    ) -> LoginRegisterResponse:
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
                login_register_params.LoginRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=LoginRegisterResponse,
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
    ) -> LoginResponseResponse:
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
            LoginResponseResponse,
            self._post(
                "/v1/app/setup/response",
                body=maybe_transform(
                    {
                        "response": response,
                        "setup_request_id": setup_request_id,
                    },
                    login_response_params.LoginResponseParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    security={},
                ),
                cast_to=cast(
                    Any, LoginResponseResponse
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
    ) -> LoginStartResponse:
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
            cast_to=LoginStartResponse,
        )


class AsyncLoginResource(AsyncAPIResource):
    """Complete first-party Beeper app login"""

    @cached_property
    def verification(self) -> AsyncVerificationResource:
        return AsyncVerificationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoginResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoginResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncLoginResourceWithStreamingResponse(self)

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
                login_email_params.LoginEmailParams,
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
    ) -> LoginRegisterResponse:
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
                login_register_params.LoginRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=LoginRegisterResponse,
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
    ) -> LoginResponseResponse:
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
            LoginResponseResponse,
            await self._post(
                "/v1/app/setup/response",
                body=await async_maybe_transform(
                    {
                        "response": response,
                        "setup_request_id": setup_request_id,
                    },
                    login_response_params.LoginResponseParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    security={},
                ),
                cast_to=cast(
                    Any, LoginResponseResponse
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
    ) -> LoginStartResponse:
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
            cast_to=LoginStartResponse,
        )


class LoginResourceWithRawResponse:
    def __init__(self, login: LoginResource) -> None:
        self._login = login

        self.email = to_raw_response_wrapper(
            login.email,
        )
        self.register = to_raw_response_wrapper(
            login.register,
        )
        self.response = to_raw_response_wrapper(
            login.response,
        )
        self.start = to_raw_response_wrapper(
            login.start,
        )

    @cached_property
    def verification(self) -> VerificationResourceWithRawResponse:
        return VerificationResourceWithRawResponse(self._login.verification)


class AsyncLoginResourceWithRawResponse:
    def __init__(self, login: AsyncLoginResource) -> None:
        self._login = login

        self.email = async_to_raw_response_wrapper(
            login.email,
        )
        self.register = async_to_raw_response_wrapper(
            login.register,
        )
        self.response = async_to_raw_response_wrapper(
            login.response,
        )
        self.start = async_to_raw_response_wrapper(
            login.start,
        )

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithRawResponse:
        return AsyncVerificationResourceWithRawResponse(self._login.verification)


class LoginResourceWithStreamingResponse:
    def __init__(self, login: LoginResource) -> None:
        self._login = login

        self.email = to_streamed_response_wrapper(
            login.email,
        )
        self.register = to_streamed_response_wrapper(
            login.register,
        )
        self.response = to_streamed_response_wrapper(
            login.response,
        )
        self.start = to_streamed_response_wrapper(
            login.start,
        )

    @cached_property
    def verification(self) -> VerificationResourceWithStreamingResponse:
        return VerificationResourceWithStreamingResponse(self._login.verification)


class AsyncLoginResourceWithStreamingResponse:
    def __init__(self, login: AsyncLoginResource) -> None:
        self._login = login

        self.email = async_to_streamed_response_wrapper(
            login.email,
        )
        self.register = async_to_streamed_response_wrapper(
            login.register,
        )
        self.response = async_to_streamed_response_wrapper(
            login.response,
        )
        self.start = async_to_streamed_response_wrapper(
            login.start,
        )

    @cached_property
    def verification(self) -> AsyncVerificationResourceWithStreamingResponse:
        return AsyncVerificationResourceWithStreamingResponse(self._login.verification)
