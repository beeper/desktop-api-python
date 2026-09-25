# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .steps import (
    StepsResource,
    AsyncStepsResource,
    StepsResourceWithRawResponse,
    AsyncStepsResourceWithRawResponse,
    StepsResourceWithStreamingResponse,
    AsyncStepsResourceWithStreamingResponse,
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
from ...._base_client import make_request_options
from ....types.bridges import login_session_create_params
from ....types.login_session import LoginSession
from ....types.bridges.login_session_cancel_response import LoginSessionCancelResponse

__all__ = ["LoginSessionsResource", "AsyncLoginSessionsResource"]


class LoginSessionsResource(SyncAPIResource):
    """
    Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
    """

    @cached_property
    def steps(self) -> StepsResource:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return StepsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LoginSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return LoginSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoginSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return LoginSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        bridge_id: str,
        *,
        account_id: str | Omit = omit,
        flow_id: str | Omit = omit,
        login_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginSession:
        """
        Start a temporary bridge login session to connect a new chat account or
        reconnect an existing bridge login. Omit loginID and accountID to connect a new
        account.

        Args:
          bridge_id: Bridge ID.

          account_id: Existing chat account ID to reconnect. Omit to connect a new account.

          flow_id: Optional flow ID returned by the list login flows endpoint. If omitted, Beeper
              chooses the default flow.

          login_id: Existing bridge login ID to reconnect. Omit to connect a new account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return self._post(
            path_template("/v1/bridges/{bridge_id}/login-sessions", bridge_id=bridge_id),
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "flow_id": flow_id,
                    "login_id": login_id,
                },
                login_session_create_params.LoginSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginSession,
        )

    def retrieve(
        self,
        login_session_id: str,
        *,
        bridge_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginSession:
        """
        Get the current state of a temporary bridge login session.

        Args:
          bridge_id: Bridge ID.

          login_session_id: Temporary bridge login session ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_session_id:
            raise ValueError(f"Expected a non-empty value for `login_session_id` but received {login_session_id!r}")
        return self._get(
            path_template(
                "/v1/bridges/{bridge_id}/login-sessions/{login_session_id}",
                bridge_id=bridge_id,
                login_session_id=login_session_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginSession,
        )

    def cancel(
        self,
        login_session_id: str,
        *,
        bridge_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginSessionCancelResponse:
        """
        Cancel a temporary bridge login session.

        Args:
          bridge_id: Bridge ID.

          login_session_id: Temporary bridge login session ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_session_id:
            raise ValueError(f"Expected a non-empty value for `login_session_id` but received {login_session_id!r}")
        return self._delete(
            path_template(
                "/v1/bridges/{bridge_id}/login-sessions/{login_session_id}",
                bridge_id=bridge_id,
                login_session_id=login_session_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginSessionCancelResponse,
        )


class AsyncLoginSessionsResource(AsyncAPIResource):
    """
    Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
    """

    @cached_property
    def steps(self) -> AsyncStepsResource:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return AsyncStepsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoginSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoginSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoginSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncLoginSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        bridge_id: str,
        *,
        account_id: str | Omit = omit,
        flow_id: str | Omit = omit,
        login_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginSession:
        """
        Start a temporary bridge login session to connect a new chat account or
        reconnect an existing bridge login. Omit loginID and accountID to connect a new
        account.

        Args:
          bridge_id: Bridge ID.

          account_id: Existing chat account ID to reconnect. Omit to connect a new account.

          flow_id: Optional flow ID returned by the list login flows endpoint. If omitted, Beeper
              chooses the default flow.

          login_id: Existing bridge login ID to reconnect. Omit to connect a new account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return await self._post(
            path_template("/v1/bridges/{bridge_id}/login-sessions", bridge_id=bridge_id),
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "flow_id": flow_id,
                    "login_id": login_id,
                },
                login_session_create_params.LoginSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginSession,
        )

    async def retrieve(
        self,
        login_session_id: str,
        *,
        bridge_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginSession:
        """
        Get the current state of a temporary bridge login session.

        Args:
          bridge_id: Bridge ID.

          login_session_id: Temporary bridge login session ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_session_id:
            raise ValueError(f"Expected a non-empty value for `login_session_id` but received {login_session_id!r}")
        return await self._get(
            path_template(
                "/v1/bridges/{bridge_id}/login-sessions/{login_session_id}",
                bridge_id=bridge_id,
                login_session_id=login_session_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginSession,
        )

    async def cancel(
        self,
        login_session_id: str,
        *,
        bridge_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginSessionCancelResponse:
        """
        Cancel a temporary bridge login session.

        Args:
          bridge_id: Bridge ID.

          login_session_id: Temporary bridge login session ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_session_id:
            raise ValueError(f"Expected a non-empty value for `login_session_id` but received {login_session_id!r}")
        return await self._delete(
            path_template(
                "/v1/bridges/{bridge_id}/login-sessions/{login_session_id}",
                bridge_id=bridge_id,
                login_session_id=login_session_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginSessionCancelResponse,
        )


class LoginSessionsResourceWithRawResponse:
    def __init__(self, login_sessions: LoginSessionsResource) -> None:
        self._login_sessions = login_sessions

        self.create = to_raw_response_wrapper(
            login_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            login_sessions.retrieve,
        )
        self.cancel = to_raw_response_wrapper(
            login_sessions.cancel,
        )

    @cached_property
    def steps(self) -> StepsResourceWithRawResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return StepsResourceWithRawResponse(self._login_sessions.steps)


class AsyncLoginSessionsResourceWithRawResponse:
    def __init__(self, login_sessions: AsyncLoginSessionsResource) -> None:
        self._login_sessions = login_sessions

        self.create = async_to_raw_response_wrapper(
            login_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            login_sessions.retrieve,
        )
        self.cancel = async_to_raw_response_wrapper(
            login_sessions.cancel,
        )

    @cached_property
    def steps(self) -> AsyncStepsResourceWithRawResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return AsyncStepsResourceWithRawResponse(self._login_sessions.steps)


class LoginSessionsResourceWithStreamingResponse:
    def __init__(self, login_sessions: LoginSessionsResource) -> None:
        self._login_sessions = login_sessions

        self.create = to_streamed_response_wrapper(
            login_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            login_sessions.retrieve,
        )
        self.cancel = to_streamed_response_wrapper(
            login_sessions.cancel,
        )

    @cached_property
    def steps(self) -> StepsResourceWithStreamingResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return StepsResourceWithStreamingResponse(self._login_sessions.steps)


class AsyncLoginSessionsResourceWithStreamingResponse:
    def __init__(self, login_sessions: AsyncLoginSessionsResource) -> None:
        self._login_sessions = login_sessions

        self.create = async_to_streamed_response_wrapper(
            login_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            login_sessions.retrieve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            login_sessions.cancel,
        )

    @cached_property
    def steps(self) -> AsyncStepsResourceWithStreamingResponse:
        """
        Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
        """
        return AsyncStepsResourceWithStreamingResponse(self._login_sessions.steps)
