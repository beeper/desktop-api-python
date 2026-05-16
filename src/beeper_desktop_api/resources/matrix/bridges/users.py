# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.matrix.bridges import user_search_params, user_resolve_params
from ....types.matrix.bridges.user_search_response import UserSearchResponse
from ....types.matrix.bridges.user_resolve_response import UserResolveResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    """Matrix-compatible APIs for accounts and connected network bridges."""

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def resolve(
        self,
        identifier: str,
        *,
        bridge_id: str,
        login_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserResolveResponse:
        """
        Resolve an identifier to a user on the remote network.

        Args:
          login_id: An optional explicit login ID to do the action through.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/resolve_identifier/{identifier}",
                bridge_id=bridge_id,
                identifier=identifier,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"login_id": login_id}, user_resolve_params.UserResolveParams),
            ),
            cast_to=UserResolveResponse,
        )

    def search(
        self,
        bridge_id: str,
        *,
        login_id: str | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserSearchResponse:
        """
        Search for users on the remote network

        Args:
          login_id: An optional explicit login ID to do the action through.

          query: The search query to send to the remote network

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return self._post(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/search_users",
                bridge_id=bridge_id,
            ),
            body=maybe_transform({"query": query}, user_search_params.UserSearchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"login_id": login_id}, user_search_params.UserSearchParams),
            ),
            cast_to=UserSearchResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    """Matrix-compatible APIs for accounts and connected network bridges."""

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def resolve(
        self,
        identifier: str,
        *,
        bridge_id: str,
        login_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserResolveResponse:
        """
        Resolve an identifier to a user on the remote network.

        Args:
          login_id: An optional explicit login ID to do the action through.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/resolve_identifier/{identifier}",
                bridge_id=bridge_id,
                identifier=identifier,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"login_id": login_id}, user_resolve_params.UserResolveParams),
            ),
            cast_to=UserResolveResponse,
        )

    async def search(
        self,
        bridge_id: str,
        *,
        login_id: str | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserSearchResponse:
        """
        Search for users on the remote network

        Args:
          login_id: An optional explicit login ID to do the action through.

          query: The search query to send to the remote network

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bridge_id:
            raise ValueError(f"Expected a non-empty value for `bridge_id` but received {bridge_id!r}")
        return await self._post(
            path_template(
                "/_matrix/client/unstable/com.beeper.bridge/{bridge_id}/_matrix/provision/v3/search_users",
                bridge_id=bridge_id,
            ),
            body=await async_maybe_transform({"query": query}, user_search_params.UserSearchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"login_id": login_id}, user_search_params.UserSearchParams),
            ),
            cast_to=UserSearchResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.resolve = to_raw_response_wrapper(
            users.resolve,
        )
        self.search = to_raw_response_wrapper(
            users.search,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.resolve = async_to_raw_response_wrapper(
            users.resolve,
        )
        self.search = async_to_raw_response_wrapper(
            users.search,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.resolve = to_streamed_response_wrapper(
            users.resolve,
        )
        self.search = to_streamed_response_wrapper(
            users.search,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.resolve = async_to_streamed_response_wrapper(
            users.resolve,
        )
        self.search = async_to_streamed_response_wrapper(
            users.search,
        )
