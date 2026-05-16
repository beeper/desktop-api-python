# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, cast

import httpx

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
from ....types.matrix.bridges import auth_start_login_params, auth_submit_cookies_params, auth_submit_user_input_params
from ....types.matrix.bridges.auth_whoami_response import AuthWhoamiResponse
from ....types.matrix.bridges.auth_list_flows_response import AuthListFlowsResponse
from ....types.matrix.bridges.auth_list_logins_response import AuthListLoginsResponse
from ....types.matrix.bridges.auth_start_login_response import AuthStartLoginResponse
from ....types.matrix.bridges.auth_wait_for_step_response import AuthWaitForStepResponse
from ....types.matrix.bridges.auth_submit_cookies_response import AuthSubmitCookiesResponse
from ....types.matrix.bridges.auth_submit_user_input_response import AuthSubmitUserInputResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    """Matrix-compatible APIs for accounts and connected network bridges."""

    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def list_flows(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthListFlowsResponse:
        """
        Get the available login flows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/flows",
                bridge_id=bridge_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthListFlowsResponse,
        )

    def list_logins(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthListLoginsResponse:
        """
        Get the login IDs of the current user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/logins",
                bridge_id=bridge_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthListLoginsResponse,
        )

    def logout(
        self,
        login_id: str,
        *,
        bridge_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Log out of an existing login.

        Args:
          login_id: The unique ID of a login.

        Defined by the network connector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_id:
            raise ValueError(f"Expected a non-empty value for `login_id` but received {login_id!r}")
        return self._post(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/logout/{login_id}",
                bridge_id=bridge_id,
                login_id=login_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def start_login(
        self,
        flow_id: str,
        *,
        bridge_id: str,
        login_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthStartLoginResponse:
        """
        This endpoint starts a new login process, which is used to log into the bridge.

        The basic flow of the entire login, including calling this endpoint, is:

        1. Call `GET /v3/login/flows` to get the list of available flows. If there's
           more than one flow, ask the user to pick which one they want to use.
        2. Call this endpoint with the chosen flow ID to start the login. The first
           login step will be returned.
        3. Render the information provided in the step.
        4. Call the `/login/step/...` endpoint corresponding to the step type:
           - For `user_input` and `cookies`, acquire the requested fields before calling
             the endpoint.
           - For `display_and_wait`, call the endpoint immediately (as there's nothing
             to acquire on the client side).
        5. Handle the data returned by the login step endpoint:
           - If an error is returned, the login has failed and must be restarted (from
             either step 1 or step 2) if the user wants to try again.
           - If step type `complete` is returned, the login finished successfully.
           - Otherwise, go to step 3 with the new data.

        Args:
          login_id: An existing login ID to re-login as. If this is specified and the user logs into
              a different account, the provided ID will be logged out.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return cast(
            AuthStartLoginResponse,
            self._post(
                path_template(
                    "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/start/{flow_id}",
                    bridge_id=bridge_id,
                    flow_id=flow_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"login_id": login_id}, auth_start_login_params.AuthStartLoginParams),
                ),
                cast_to=cast(
                    Any, AuthStartLoginResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def submit_cookies(
        self,
        step_id: str,
        *,
        bridge_id: str,
        login_process_id: str,
        body: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSubmitCookiesResponse:
        """
        Submit extracted cookies in a login process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_process_id:
            raise ValueError(f"Expected a non-empty value for `login_process_id` but received {login_process_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return cast(
            AuthSubmitCookiesResponse,
            self._post(
                path_template(
                    "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/step/{login_process_id}/{step_id}/cookies",
                    bridge_id=bridge_id,
                    login_process_id=login_process_id,
                    step_id=step_id,
                ),
                body=maybe_transform(body, auth_submit_cookies_params.AuthSubmitCookiesParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AuthSubmitCookiesResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def submit_user_input(
        self,
        step_id: str,
        *,
        bridge_id: str,
        login_process_id: str,
        body: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSubmitUserInputResponse:
        """
        Submit user input in a login process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_process_id:
            raise ValueError(f"Expected a non-empty value for `login_process_id` but received {login_process_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return cast(
            AuthSubmitUserInputResponse,
            self._post(
                path_template(
                    "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/step/{login_process_id}/{step_id}/user_input",
                    bridge_id=bridge_id,
                    login_process_id=login_process_id,
                    step_id=step_id,
                ),
                body=maybe_transform(body, auth_submit_user_input_params.AuthSubmitUserInputParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AuthSubmitUserInputResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def wait_for_step(
        self,
        step_id: str,
        *,
        bridge_id: str,
        login_process_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthWaitForStepResponse:
        """
        Wait for the next step after displaying data to the user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_process_id:
            raise ValueError(f"Expected a non-empty value for `login_process_id` but received {login_process_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return cast(
            AuthWaitForStepResponse,
            self._post(
                path_template(
                    "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/step/{login_process_id}/{step_id}/display_and_wait",
                    bridge_id=bridge_id,
                    login_process_id=login_process_id,
                    step_id=step_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AuthWaitForStepResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def whoami(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthWhoamiResponse:
        """
        Get all info that is useful for presenting this bridge in a manager interface.

        - Server details: remote network details, available login flows, homeserver
          name, bridge bot user ID, command prefix
        - User details: management room ID, list of logins with current state and info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/whoami",
                bridge_id=bridge_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthWhoamiResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    """Matrix-compatible APIs for accounts and connected network bridges."""

    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def list_flows(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthListFlowsResponse:
        """
        Get the available login flows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return await self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/flows",
                bridge_id=bridge_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthListFlowsResponse,
        )

    async def list_logins(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthListLoginsResponse:
        """
        Get the login IDs of the current user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return await self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/logins",
                bridge_id=bridge_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthListLoginsResponse,
        )

    async def logout(
        self,
        login_id: str,
        *,
        bridge_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Log out of an existing login.

        Args:
          login_id: The unique ID of a login.

        Defined by the network connector.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_id:
            raise ValueError(f"Expected a non-empty value for `login_id` but received {login_id!r}")
        return await self._post(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/logout/{login_id}",
                bridge_id=bridge_id,
                login_id=login_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def start_login(
        self,
        flow_id: str,
        *,
        bridge_id: str,
        login_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthStartLoginResponse:
        """
        This endpoint starts a new login process, which is used to log into the bridge.

        The basic flow of the entire login, including calling this endpoint, is:

        1. Call `GET /v3/login/flows` to get the list of available flows. If there's
           more than one flow, ask the user to pick which one they want to use.
        2. Call this endpoint with the chosen flow ID to start the login. The first
           login step will be returned.
        3. Render the information provided in the step.
        4. Call the `/login/step/...` endpoint corresponding to the step type:
           - For `user_input` and `cookies`, acquire the requested fields before calling
             the endpoint.
           - For `display_and_wait`, call the endpoint immediately (as there's nothing
             to acquire on the client side).
        5. Handle the data returned by the login step endpoint:
           - If an error is returned, the login has failed and must be restarted (from
             either step 1 or step 2) if the user wants to try again.
           - If step type `complete` is returned, the login finished successfully.
           - Otherwise, go to step 3 with the new data.

        Args:
          login_id: An existing login ID to re-login as. If this is specified and the user logs into
              a different account, the provided ID will be logged out.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not flow_id:
            raise ValueError(f"Expected a non-empty value for `flow_id` but received {flow_id!r}")
        return cast(
            AuthStartLoginResponse,
            await self._post(
                path_template(
                    "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/start/{flow_id}",
                    bridge_id=bridge_id,
                    flow_id=flow_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"login_id": login_id}, auth_start_login_params.AuthStartLoginParams
                    ),
                ),
                cast_to=cast(
                    Any, AuthStartLoginResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def submit_cookies(
        self,
        step_id: str,
        *,
        bridge_id: str,
        login_process_id: str,
        body: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSubmitCookiesResponse:
        """
        Submit extracted cookies in a login process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_process_id:
            raise ValueError(f"Expected a non-empty value for `login_process_id` but received {login_process_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return cast(
            AuthSubmitCookiesResponse,
            await self._post(
                path_template(
                    "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/step/{login_process_id}/{step_id}/cookies",
                    bridge_id=bridge_id,
                    login_process_id=login_process_id,
                    step_id=step_id,
                ),
                body=await async_maybe_transform(body, auth_submit_cookies_params.AuthSubmitCookiesParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AuthSubmitCookiesResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def submit_user_input(
        self,
        step_id: str,
        *,
        bridge_id: str,
        login_process_id: str,
        body: Dict[str, str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSubmitUserInputResponse:
        """
        Submit user input in a login process.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_process_id:
            raise ValueError(f"Expected a non-empty value for `login_process_id` but received {login_process_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return cast(
            AuthSubmitUserInputResponse,
            await self._post(
                path_template(
                    "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/step/{login_process_id}/{step_id}/user_input",
                    bridge_id=bridge_id,
                    login_process_id=login_process_id,
                    step_id=step_id,
                ),
                body=await async_maybe_transform(body, auth_submit_user_input_params.AuthSubmitUserInputParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AuthSubmitUserInputResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def wait_for_step(
        self,
        step_id: str,
        *,
        bridge_id: str,
        login_process_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthWaitForStepResponse:
        """
        Wait for the next step after displaying data to the user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_process_id:
            raise ValueError(f"Expected a non-empty value for `login_process_id` but received {login_process_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return cast(
            AuthWaitForStepResponse,
            await self._post(
                path_template(
                    "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/login/step/{login_process_id}/{step_id}/display_and_wait",
                    bridge_id=bridge_id,
                    login_process_id=login_process_id,
                    step_id=step_id,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AuthWaitForStepResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def whoami(
        self,
        bridge_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthWhoamiResponse:
        """
        Get all info that is useful for presenting this bridge in a manager interface.

        - Server details: remote network details, available login flows, homeserver
          name, bridge bot user ID, command prefix
        - User details: management room ID, list of logins with current state and info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return await self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/whoami",
                bridge_id=bridge_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthWhoamiResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.list_flows = to_raw_response_wrapper(
            auth.list_flows,
        )
        self.list_logins = to_raw_response_wrapper(
            auth.list_logins,
        )
        self.logout = to_raw_response_wrapper(
            auth.logout,
        )
        self.start_login = to_raw_response_wrapper(
            auth.start_login,
        )
        self.submit_cookies = to_raw_response_wrapper(
            auth.submit_cookies,
        )
        self.submit_user_input = to_raw_response_wrapper(
            auth.submit_user_input,
        )
        self.wait_for_step = to_raw_response_wrapper(
            auth.wait_for_step,
        )
        self.whoami = to_raw_response_wrapper(
            auth.whoami,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.list_flows = async_to_raw_response_wrapper(
            auth.list_flows,
        )
        self.list_logins = async_to_raw_response_wrapper(
            auth.list_logins,
        )
        self.logout = async_to_raw_response_wrapper(
            auth.logout,
        )
        self.start_login = async_to_raw_response_wrapper(
            auth.start_login,
        )
        self.submit_cookies = async_to_raw_response_wrapper(
            auth.submit_cookies,
        )
        self.submit_user_input = async_to_raw_response_wrapper(
            auth.submit_user_input,
        )
        self.wait_for_step = async_to_raw_response_wrapper(
            auth.wait_for_step,
        )
        self.whoami = async_to_raw_response_wrapper(
            auth.whoami,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.list_flows = to_streamed_response_wrapper(
            auth.list_flows,
        )
        self.list_logins = to_streamed_response_wrapper(
            auth.list_logins,
        )
        self.logout = to_streamed_response_wrapper(
            auth.logout,
        )
        self.start_login = to_streamed_response_wrapper(
            auth.start_login,
        )
        self.submit_cookies = to_streamed_response_wrapper(
            auth.submit_cookies,
        )
        self.submit_user_input = to_streamed_response_wrapper(
            auth.submit_user_input,
        )
        self.wait_for_step = to_streamed_response_wrapper(
            auth.wait_for_step,
        )
        self.whoami = to_streamed_response_wrapper(
            auth.whoami,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.list_flows = async_to_streamed_response_wrapper(
            auth.list_flows,
        )
        self.list_logins = async_to_streamed_response_wrapper(
            auth.list_logins,
        )
        self.logout = async_to_streamed_response_wrapper(
            auth.logout,
        )
        self.start_login = async_to_streamed_response_wrapper(
            auth.start_login,
        )
        self.submit_cookies = async_to_streamed_response_wrapper(
            auth.submit_cookies,
        )
        self.submit_user_input = async_to_streamed_response_wrapper(
            auth.submit_user_input,
        )
        self.wait_for_step = async_to_streamed_response_wrapper(
            auth.wait_for_step,
        )
        self.whoami = async_to_streamed_response_wrapper(
            auth.whoami,
        )
