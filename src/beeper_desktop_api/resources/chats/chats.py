# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import chat_list_params, chat_create_params, chat_search_params, chat_archive_params, chat_retrieve_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .reminders import (
    RemindersResource,
    AsyncRemindersResource,
    RemindersResourceWithRawResponse,
    AsyncRemindersResourceWithRawResponse,
    RemindersResourceWithStreamingResponse,
    AsyncRemindersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorSearch, AsyncCursorSearch, SyncCursorNoLimit, AsyncCursorNoLimit
from ...types.chat import Chat
from ..._base_client import AsyncPaginator, make_request_options
from ...types.chat_list_response import ChatListResponse
from ...types.chat_create_response import ChatCreateResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    """Manage chats"""

    @cached_property
    def reminders(self) -> RemindersResource:
        """Manage reminders for chats"""
        return RemindersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return ChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return ChatsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        participant_ids: SequenceNotStr[str],
        type: Literal["single", "group"],
        message_text: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateResponse:
        """
        Create a single or group chat on a specific account using participant IDs and
        optional title.

        Args:
          account_id: Account to create the chat on.

          participant_ids: User IDs to include in the new chat.

          type: Chat type to create: 'single' requires exactly one participantID; 'group'
              supports multiple participants and optional title.

          message_text: Optional first message content if the platform requires it to create the chat.

          title: Optional title for group chats; ignored for single chats on most platforms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chats",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "participant_ids": participant_ids,
                    "type": type,
                    "message_text": message_text,
                    "title": title,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateResponse,
        )

    def retrieve(
        self,
        chat_id: str,
        *,
        max_participant_count: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """
        Retrieve chat details including metadata, participants, and latest message

        Args:
          chat_id: Unique identifier of the chat.

          max_participant_count: Maximum number of participants to return. Use -1 for all; otherwise 0–500.
              Defaults to all (-1).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            f"/v1/chats/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"max_participant_count": max_participant_count}, chat_retrieve_params.ChatRetrieveParams
                ),
            ),
            cast_to=Chat,
        )

    def list(
        self,
        *,
        account_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorNoLimit[ChatListResponse]:
        """List all chats sorted by last activity (most recent first).

        Combines all
        accounts into a single paginated list.

        Args:
          account_ids: Limit to specific account IDs. If omitted, fetches from all accounts.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/chats",
            page=SyncCursorNoLimit[ChatListResponse],
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
                    },
                    chat_list_params.ChatListParams,
                ),
            ),
            model=ChatListResponse,
        )

    def archive(
        self,
        chat_id: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive or unarchive a chat.

        Set archived=true to move to archive,
        archived=false to move back to inbox

        Args:
          chat_id: Unique identifier of the chat.

          archived: True to archive, false to unarchive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/chats/{chat_id}/archive",
            body=maybe_transform({"archived": archived}, chat_archive_params.ChatArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def search(
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
            "/v1/chats/search",
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
                    chat_search_params.ChatSearchParams,
                ),
            ),
            model=Chat,
        )


class AsyncChatsResource(AsyncAPIResource):
    """Manage chats"""

    @cached_property
    def reminders(self) -> AsyncRemindersResource:
        """Manage reminders for chats"""
        return AsyncRemindersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncChatsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        participant_ids: SequenceNotStr[str],
        type: Literal["single", "group"],
        message_text: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateResponse:
        """
        Create a single or group chat on a specific account using participant IDs and
        optional title.

        Args:
          account_id: Account to create the chat on.

          participant_ids: User IDs to include in the new chat.

          type: Chat type to create: 'single' requires exactly one participantID; 'group'
              supports multiple participants and optional title.

          message_text: Optional first message content if the platform requires it to create the chat.

          title: Optional title for group chats; ignored for single chats on most platforms.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chats",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "participant_ids": participant_ids,
                    "type": type,
                    "message_text": message_text,
                    "title": title,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateResponse,
        )

    async def retrieve(
        self,
        chat_id: str,
        *,
        max_participant_count: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """
        Retrieve chat details including metadata, participants, and latest message

        Args:
          chat_id: Unique identifier of the chat.

          max_participant_count: Maximum number of participants to return. Use -1 for all; otherwise 0–500.
              Defaults to all (-1).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            f"/v1/chats/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"max_participant_count": max_participant_count}, chat_retrieve_params.ChatRetrieveParams
                ),
            ),
            cast_to=Chat,
        )

    def list(
        self,
        *,
        account_ids: SequenceNotStr[str] | Omit = omit,
        cursor: str | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ChatListResponse, AsyncCursorNoLimit[ChatListResponse]]:
        """List all chats sorted by last activity (most recent first).

        Combines all
        accounts into a single paginated list.

        Args:
          account_ids: Limit to specific account IDs. If omitted, fetches from all accounts.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/chats",
            page=AsyncCursorNoLimit[ChatListResponse],
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
                    },
                    chat_list_params.ChatListParams,
                ),
            ),
            model=ChatListResponse,
        )

    async def archive(
        self,
        chat_id: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive or unarchive a chat.

        Set archived=true to move to archive,
        archived=false to move back to inbox

        Args:
          chat_id: Unique identifier of the chat.

          archived: True to archive, false to unarchive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/chats/{chat_id}/archive",
            body=await async_maybe_transform({"archived": archived}, chat_archive_params.ChatArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def search(
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
            "/v1/chats/search",
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
                    chat_search_params.ChatSearchParams,
                ),
            ),
            model=Chat,
        )


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_raw_response_wrapper(
            chats.create,
        )
        self.retrieve = to_raw_response_wrapper(
            chats.retrieve,
        )
        self.list = to_raw_response_wrapper(
            chats.list,
        )
        self.archive = to_raw_response_wrapper(
            chats.archive,
        )
        self.search = to_raw_response_wrapper(
            chats.search,
        )

    @cached_property
    def reminders(self) -> RemindersResourceWithRawResponse:
        """Manage reminders for chats"""
        return RemindersResourceWithRawResponse(self._chats.reminders)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_raw_response_wrapper(
            chats.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            chats.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            chats.list,
        )
        self.archive = async_to_raw_response_wrapper(
            chats.archive,
        )
        self.search = async_to_raw_response_wrapper(
            chats.search,
        )

    @cached_property
    def reminders(self) -> AsyncRemindersResourceWithRawResponse:
        """Manage reminders for chats"""
        return AsyncRemindersResourceWithRawResponse(self._chats.reminders)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_streamed_response_wrapper(
            chats.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            chats.list,
        )
        self.archive = to_streamed_response_wrapper(
            chats.archive,
        )
        self.search = to_streamed_response_wrapper(
            chats.search,
        )

    @cached_property
    def reminders(self) -> RemindersResourceWithStreamingResponse:
        """Manage reminders for chats"""
        return RemindersResourceWithStreamingResponse(self._chats.reminders)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_streamed_response_wrapper(
            chats.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            chats.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            chats.archive,
        )
        self.search = async_to_streamed_response_wrapper(
            chats.search,
        )

    @cached_property
    def reminders(self) -> AsyncRemindersResourceWithStreamingResponse:
        """Manage reminders for chats"""
        return AsyncRemindersResourceWithStreamingResponse(self._chats.reminders)
