# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

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
from ....types.login_session import LoginSession
from ....types.bridges.login_sessions import step_submit_params

__all__ = ["StepsResource", "AsyncStepsResource"]


class StepsResource(SyncAPIResource):
    """
    Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
    """

    @cached_property
    def with_raw_response(self) -> StepsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return StepsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StepsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return StepsResourceWithStreamingResponse(self)

    def submit(
        self,
        step_id: str,
        *,
        bridge_id: str,
        login_session_id: str,
        type: Literal["user_input", "cookies", "display_and_wait"],
        fields: Dict[str, str] | Omit = omit,
        last_url: str | Omit = omit,
        source: Literal["api", "webview", "browser_extension"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginSession:
        """
        Submit input for the current step of a bridge login session.

        Args:
          bridge_id: Bridge ID.

          login_session_id: Temporary bridge login session ID.

          step_id: Current bridge login session step ID.

          fields: Field values keyed by the field IDs from the current step.

          last_url: Last browser URL reached during a cookies step, if available.

          source: How the step was completed. Omit unless the client needs to distinguish an
              embedded webview or browser extension.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_session_id:
            raise ValueError(f"Expected a non-empty value for `login_session_id` but received {login_session_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._post(
            path_template(
                "/v1/bridges/{bridge_id}/login-sessions/{login_session_id}/steps/{step_id}",
                bridge_id=bridge_id,
                login_session_id=login_session_id,
                step_id=step_id,
            ),
            body=maybe_transform(
                {
                    "type": type,
                    "fields": fields,
                    "last_url": last_url,
                    "source": source,
                },
                step_submit_params.StepSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginSession,
        )


class AsyncStepsResource(AsyncAPIResource):
    """
    Available bridges, bridge logins, login sessions for connect and reconnect flows, and advanced network capabilities.
    """

    @cached_property
    def with_raw_response(self) -> AsyncStepsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStepsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStepsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncStepsResourceWithStreamingResponse(self)

    async def submit(
        self,
        step_id: str,
        *,
        bridge_id: str,
        login_session_id: str,
        type: Literal["user_input", "cookies", "display_and_wait"],
        fields: Dict[str, str] | Omit = omit,
        last_url: str | Omit = omit,
        source: Literal["api", "webview", "browser_extension"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoginSession:
        """
        Submit input for the current step of a bridge login session.

        Args:
          bridge_id: Bridge ID.

          login_session_id: Temporary bridge login session ID.

          step_id: Current bridge login session step ID.

          fields: Field values keyed by the field IDs from the current step.

          last_url: Last browser URL reached during a cookies step, if available.

          source: How the step was completed. Omit unless the client needs to distinguish an
              embedded webview or browser extension.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not login_session_id:
            raise ValueError(f"Expected a non-empty value for `login_session_id` but received {login_session_id!r}")
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._post(
            path_template(
                "/v1/bridges/{bridge_id}/login-sessions/{login_session_id}/steps/{step_id}",
                bridge_id=bridge_id,
                login_session_id=login_session_id,
                step_id=step_id,
            ),
            body=await async_maybe_transform(
                {
                    "type": type,
                    "fields": fields,
                    "last_url": last_url,
                    "source": source,
                },
                step_submit_params.StepSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoginSession,
        )


class StepsResourceWithRawResponse:
    def __init__(self, steps: StepsResource) -> None:
        self._steps = steps

        self.submit = to_raw_response_wrapper(
            steps.submit,
        )


class AsyncStepsResourceWithRawResponse:
    def __init__(self, steps: AsyncStepsResource) -> None:
        self._steps = steps

        self.submit = async_to_raw_response_wrapper(
            steps.submit,
        )


class StepsResourceWithStreamingResponse:
    def __init__(self, steps: StepsResource) -> None:
        self._steps = steps

        self.submit = to_streamed_response_wrapper(
            steps.submit,
        )


class AsyncStepsResourceWithStreamingResponse:
    def __init__(self, steps: AsyncStepsResource) -> None:
        self._steps = steps

        self.submit = async_to_streamed_response_wrapper(
            steps.submit,
        )
