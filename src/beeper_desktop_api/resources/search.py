# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import search_chats_params, search_contacts_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorSearch, AsyncCursorSearch
from ..types.chat import Chat
from .._base_client import AsyncPaginator, make_request_options
from ..types.search_contacts_response import SearchContactsResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def chats(
        self,
        *,
        account_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        inbox: Literal["primary", "low-priority", "archive"] | Omit = omit,
        include_muted: Optional[bool] | Omit = omit,
        last_activity_after: Union[str, datetime] | Omit = omit,
        last_activity_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        scope: Literal["titles", "participants"] | Omit = omit,
        type: Literal["single", "group", "any"] | Omit = omit,
        unread_only: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorSearch[Chat]:
        """
        Search chats by title/network or participants using Beeper Desktop's renderer
        algorithm.

        Args:
          account_ids: Provide an array of account IDs to filter chats from specific messaging accounts
              only

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          inbox: Filter by inbox type: "primary" (non-archived, non-low-priority),
              "low-priority", or "archive". If not specified, shows all chats.

          include_muted: Include chats marked as Muted by the user, which are usually less important.
              Default: true. Set to false if the user wants a more refined search.

          last_activity_after: Provide an ISO datetime string to only retrieve chats with last activity after
              this time

          last_activity_before: Provide an ISO datetime string to only retrieve chats with last activity before
              this time

          limit: Set the maximum number of chats to retrieve. Valid range: 1-200, default is 50

          query: Literal token search (non-semantic). Use single words users type (e.g.,
              "dinner"). When multiple words provided, ALL must match. Case-insensitive.

          scope: Search scope: 'titles' matches title + network; 'participants' matches
              participant names.

          type: Specify the type of chats to retrieve: use "single" for direct messages, "group"
              for group chats, or "any" to get all types

          unread_only: Set to true to only retrieve chats that have unread messages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/search/chats",
            page=SyncCursorSearch[Chat],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "cursor": cursor,
                        "direction": direction,
                        "inbox": inbox,
                        "include_muted": include_muted,
                        "last_activity_after": last_activity_after,
                        "last_activity_before": last_activity_before,
                        "limit": limit,
                        "query": query,
                        "scope": scope,
                        "type": type,
                        "unread_only": unread_only,
                    },
                    search_chats_params.SearchChatsParams,
                ),
            ),
            model=Chat,
        )

    def contacts(
        self,
        account_id: str,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchContactsResponse:
        """
        Search contacts across on a specific account using the network's search API.
        Only use for creating new chats.

        Args:
          account_id: Account ID this resource belongs to.

          query: Text to search users by. Network-specific behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/v1/search/contacts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, search_contacts_params.SearchContactsParams),
            ),
            cast_to=SearchContactsResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    def chats(
        self,
        *,
        account_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        inbox: Literal["primary", "low-priority", "archive"] | Omit = omit,
        include_muted: Optional[bool] | Omit = omit,
        last_activity_after: Union[str, datetime] | Omit = omit,
        last_activity_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        scope: Literal["titles", "participants"] | Omit = omit,
        type: Literal["single", "group", "any"] | Omit = omit,
        unread_only: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Chat, AsyncCursorSearch[Chat]]:
        """
        Search chats by title/network or participants using Beeper Desktop's renderer
        algorithm.

        Args:
          account_ids: Provide an array of account IDs to filter chats from specific messaging accounts
              only

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          inbox: Filter by inbox type: "primary" (non-archived, non-low-priority),
              "low-priority", or "archive". If not specified, shows all chats.

          include_muted: Include chats marked as Muted by the user, which are usually less important.
              Default: true. Set to false if the user wants a more refined search.

          last_activity_after: Provide an ISO datetime string to only retrieve chats with last activity after
              this time

          last_activity_before: Provide an ISO datetime string to only retrieve chats with last activity before
              this time

          limit: Set the maximum number of chats to retrieve. Valid range: 1-200, default is 50

          query: Literal token search (non-semantic). Use single words users type (e.g.,
              "dinner"). When multiple words provided, ALL must match. Case-insensitive.

          scope: Search scope: 'titles' matches title + network; 'participants' matches
              participant names.

          type: Specify the type of chats to retrieve: use "single" for direct messages, "group"
              for group chats, or "any" to get all types

          unread_only: Set to true to only retrieve chats that have unread messages

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/search/chats",
            page=AsyncCursorSearch[Chat],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "cursor": cursor,
                        "direction": direction,
                        "inbox": inbox,
                        "include_muted": include_muted,
                        "last_activity_after": last_activity_after,
                        "last_activity_before": last_activity_before,
                        "limit": limit,
                        "query": query,
                        "scope": scope,
                        "type": type,
                        "unread_only": unread_only,
                    },
                    search_chats_params.SearchChatsParams,
                ),
            ),
            model=Chat,
        )

    async def contacts(
        self,
        account_id: str,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchContactsResponse:
        """
        Search contacts across on a specific account using the network's search API.
        Only use for creating new chats.

        Args:
          account_id: Account ID this resource belongs to.

          query: Text to search users by. Network-specific behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/v1/search/contacts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, search_contacts_params.SearchContactsParams),
            ),
            cast_to=SearchContactsResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.chats = to_raw_response_wrapper(
            search.chats,
        )
        self.contacts = to_raw_response_wrapper(
            search.contacts,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.chats = async_to_raw_response_wrapper(
            search.chats,
        )
        self.contacts = async_to_raw_response_wrapper(
            search.contacts,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.chats = to_streamed_response_wrapper(
            search.chats,
        )
        self.contacts = to_streamed_response_wrapper(
            search.contacts,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.chats = async_to_streamed_response_wrapper(
            search.chats,
        )
        self.contacts = async_to_streamed_response_wrapper(
            search.contacts,
        )
