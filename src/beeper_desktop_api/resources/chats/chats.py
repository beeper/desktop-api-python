# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    chat_list_params,
    chat_start_params,
    chat_create_params,
    chat_search_params,
    chat_update_params,
    chat_archive_params,
    chat_retrieve_params,
    chat_mark_read_params,
    chat_mark_unread_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from .messages.messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...types.chat_list_response import ChatListResponse
from ...types.chat_start_response import ChatStartResponse
from ...types.chat_create_response import ChatCreateResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    """Manage chats"""

    @cached_property
    def reminders(self) -> RemindersResource:
        """Manage reminders for chats"""
        return RemindersResource(self._client)

    @cached_property
    def messages(self) -> MessagesResource:
        """Manage chat messages"""
        return MessagesResource(self._client)

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
        """Create a direct or group chat from participant IDs.

        Returns the created chat.

        Args:
          account_id: Account to create or start the chat on.

          participant_ids: User IDs to include in the new chat.

          type: 'single' requires exactly one participantID; 'group' supports multiple
              participants and optional title.

          message_text: Optional first message content if the platform requires it to create the chat.

          title: Optional title for group chats; ignored for single chats on most networks.

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
        Retrieve chat details, including metadata, participants, and the latest message.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          max_participant_count: Maximum number of participants to return. Use -1 for all; otherwise 0-500.
              Defaults to 100. List and search endpoints return up to 20 participants per
              chat.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            path_template("/v1/chats/{chat_id}", chat_id=chat_id),
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

    def update(
        self,
        chat_id: str,
        *,
        description: Optional[str] | Omit = omit,
        draft: Optional[chat_update_params.Draft] | Omit = omit,
        img_url: Optional[str] | Omit = omit,
        is_archived: bool | Omit = omit,
        is_low_priority: bool | Omit = omit,
        is_muted: bool | Omit = omit,
        is_pinned: bool | Omit = omit,
        message_expiry_seconds: Optional[int] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """Update supported chat fields.

        Non-empty drafts are accepted only when the
        current draft is empty. Send draft=null to clear the draft before setting new
        draft text or attachments.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          description: Group chat description/topic. Support depends on the chat account and chat
              permissions.

          draft: Draft object to set or clear. Non-empty drafts are only accepted when the
              current draft is empty. Send draft=null to clear text and attachments together
              before setting a new draft.

          img_url: Local filesystem path to a group chat avatar image. Support depends on the chat
              account and chat permissions.

          is_archived: Archive or unarchive the chat.

          is_low_priority: Mark or unmark the chat as low priority when supported by the account.

          is_muted: Mute or unmute the chat.

          is_pinned: Pin or unpin the chat when supported by the account.

          message_expiry_seconds: Disappearing-message timer in seconds, or null to clear when supported.

          title: Custom chat title. Support depends on the chat account and chat permissions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._patch(
            path_template("/v1/chats/{chat_id}", chat_id=chat_id),
            body=maybe_transform(
                {
                    "description": description,
                    "draft": draft,
                    "img_url": img_url,
                    "is_archived": is_archived,
                    "is_low_priority": is_low_priority,
                    "is_muted": is_muted,
                    "is_pinned": is_pinned,
                    "message_expiry_seconds": message_expiry_seconds,
                    "title": title,
                },
                chat_update_params.ChatUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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

        Set archived=true to move it to Archive, or
        archived=false to move it back to the inbox.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

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
            path_template("/v1/chats/{chat_id}/archive", chat_id=chat_id),
            body=maybe_transform({"archived": archived}, chat_archive_params.ChatArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def mark_read(
        self,
        chat_id: str,
        *,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """
        Mark a chat as read, optionally through a specific message ID.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          message_id: Optional message ID to mark read through.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v1/chats/{chat_id}/read", chat_id=chat_id),
            body=maybe_transform({"message_id": message_id}, chat_mark_read_params.ChatMarkReadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
        )

    def mark_unread(
        self,
        chat_id: str,
        *,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """
        Mark a chat as unread, optionally from a specific message ID.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          message_id: Optional message ID to mark unread from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v1/chats/{chat_id}/unread", chat_id=chat_id),
            body=maybe_transform({"message_id": message_id}, chat_mark_unread_params.ChatMarkUnreadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
        )

    def notify_anyway(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """
        Send a notification despite the recipient focus state when the network supports
        it. Currently intended for iMessage on macOS; unsupported networks return an
        error.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v1/chats/{chat_id}/notify-anyway", chat_id=chat_id),
            body={},
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
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
        Search chats by title, network, or participant names.

        Args:
          account_ids: Limit results to specific chat accounts.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          inbox: Filter by inbox type: "primary" (non-archived, non-low-priority),
              "low-priority", or "archive". If not specified, shows all chats.

          include_muted: Include chats marked as Muted by the user, which are usually less important.
              Default: true. Set to false if the user wants a more refined search.

          last_activity_after: Only include chats with last activity after this ISO 8601 datetime.

          last_activity_before: Only include chats with last activity before this ISO 8601 datetime.

          limit: Set the maximum number of chats to retrieve. Valid range: 1-200, default is 50

          query: Literal chat search. Use words the user typed, such as "dinner". When multiple
              words are provided, all must match. Case-insensitive.

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

    def start(
        self,
        *,
        account_id: str,
        user: chat_start_params.User,
        allow_invite: bool | Omit = omit,
        message_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatStartResponse:
        """Resolve a user/contact and open a direct chat.

        Reuses and returns an existing
        direct chat when one is found. Available in Beeper v4.2.808+.

        Args:
          account_id: Account to create or start the chat on.

          user: Contact-like user payload used to resolve the best identifier.

          allow_invite: Whether invite-based DM creation is allowed when required by the platform.

          message_text: Optional first message content if the platform requires it to create the chat.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chats/start",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "user": user,
                    "allow_invite": allow_invite,
                    "message_text": message_text,
                },
                chat_start_params.ChatStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatStartResponse,
        )


class AsyncChatsResource(AsyncAPIResource):
    """Manage chats"""

    @cached_property
    def reminders(self) -> AsyncRemindersResource:
        """Manage reminders for chats"""
        return AsyncRemindersResource(self._client)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Manage chat messages"""
        return AsyncMessagesResource(self._client)

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
        """Create a direct or group chat from participant IDs.

        Returns the created chat.

        Args:
          account_id: Account to create or start the chat on.

          participant_ids: User IDs to include in the new chat.

          type: 'single' requires exactly one participantID; 'group' supports multiple
              participants and optional title.

          message_text: Optional first message content if the platform requires it to create the chat.

          title: Optional title for group chats; ignored for single chats on most networks.

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
        Retrieve chat details, including metadata, participants, and the latest message.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          max_participant_count: Maximum number of participants to return. Use -1 for all; otherwise 0-500.
              Defaults to 100. List and search endpoints return up to 20 participants per
              chat.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            path_template("/v1/chats/{chat_id}", chat_id=chat_id),
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

    async def update(
        self,
        chat_id: str,
        *,
        description: Optional[str] | Omit = omit,
        draft: Optional[chat_update_params.Draft] | Omit = omit,
        img_url: Optional[str] | Omit = omit,
        is_archived: bool | Omit = omit,
        is_low_priority: bool | Omit = omit,
        is_muted: bool | Omit = omit,
        is_pinned: bool | Omit = omit,
        message_expiry_seconds: Optional[int] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """Update supported chat fields.

        Non-empty drafts are accepted only when the
        current draft is empty. Send draft=null to clear the draft before setting new
        draft text or attachments.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          description: Group chat description/topic. Support depends on the chat account and chat
              permissions.

          draft: Draft object to set or clear. Non-empty drafts are only accepted when the
              current draft is empty. Send draft=null to clear text and attachments together
              before setting a new draft.

          img_url: Local filesystem path to a group chat avatar image. Support depends on the chat
              account and chat permissions.

          is_archived: Archive or unarchive the chat.

          is_low_priority: Mark or unmark the chat as low priority when supported by the account.

          is_muted: Mute or unmute the chat.

          is_pinned: Pin or unpin the chat when supported by the account.

          message_expiry_seconds: Disappearing-message timer in seconds, or null to clear when supported.

          title: Custom chat title. Support depends on the chat account and chat permissions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._patch(
            path_template("/v1/chats/{chat_id}", chat_id=chat_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "draft": draft,
                    "img_url": img_url,
                    "is_archived": is_archived,
                    "is_low_priority": is_low_priority,
                    "is_muted": is_muted,
                    "is_pinned": is_pinned,
                    "message_expiry_seconds": message_expiry_seconds,
                    "title": title,
                },
                chat_update_params.ChatUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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

        Set archived=true to move it to Archive, or
        archived=false to move it back to the inbox.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

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
            path_template("/v1/chats/{chat_id}/archive", chat_id=chat_id),
            body=await async_maybe_transform({"archived": archived}, chat_archive_params.ChatArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def mark_read(
        self,
        chat_id: str,
        *,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """
        Mark a chat as read, optionally through a specific message ID.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          message_id: Optional message ID to mark read through.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v1/chats/{chat_id}/read", chat_id=chat_id),
            body=await async_maybe_transform({"message_id": message_id}, chat_mark_read_params.ChatMarkReadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
        )

    async def mark_unread(
        self,
        chat_id: str,
        *,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """
        Mark a chat as unread, optionally from a specific message ID.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          message_id: Optional message ID to mark unread from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v1/chats/{chat_id}/unread", chat_id=chat_id),
            body=await async_maybe_transform({"message_id": message_id}, chat_mark_unread_params.ChatMarkUnreadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
        )

    async def notify_anyway(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Chat:
        """
        Send a notification despite the recipient focus state when the network supports
        it. Currently intended for iMessage on macOS; unsupported networks return an
        error.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this installation when
              available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v1/chats/{chat_id}/notify-anyway", chat_id=chat_id),
            body={},
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
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
        Search chats by title, network, or participant names.

        Args:
          account_ids: Limit results to specific chat accounts.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          inbox: Filter by inbox type: "primary" (non-archived, non-low-priority),
              "low-priority", or "archive". If not specified, shows all chats.

          include_muted: Include chats marked as Muted by the user, which are usually less important.
              Default: true. Set to false if the user wants a more refined search.

          last_activity_after: Only include chats with last activity after this ISO 8601 datetime.

          last_activity_before: Only include chats with last activity before this ISO 8601 datetime.

          limit: Set the maximum number of chats to retrieve. Valid range: 1-200, default is 50

          query: Literal chat search. Use words the user typed, such as "dinner". When multiple
              words are provided, all must match. Case-insensitive.

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

    async def start(
        self,
        *,
        account_id: str,
        user: chat_start_params.User,
        allow_invite: bool | Omit = omit,
        message_text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatStartResponse:
        """Resolve a user/contact and open a direct chat.

        Reuses and returns an existing
        direct chat when one is found. Available in Beeper v4.2.808+.

        Args:
          account_id: Account to create or start the chat on.

          user: Contact-like user payload used to resolve the best identifier.

          allow_invite: Whether invite-based DM creation is allowed when required by the platform.

          message_text: Optional first message content if the platform requires it to create the chat.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chats/start",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "user": user,
                    "allow_invite": allow_invite,
                    "message_text": message_text,
                },
                chat_start_params.ChatStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatStartResponse,
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
        self.update = to_raw_response_wrapper(
            chats.update,
        )
        self.list = to_raw_response_wrapper(
            chats.list,
        )
        self.archive = to_raw_response_wrapper(
            chats.archive,
        )
        self.mark_read = to_raw_response_wrapper(
            chats.mark_read,
        )
        self.mark_unread = to_raw_response_wrapper(
            chats.mark_unread,
        )
        self.notify_anyway = to_raw_response_wrapper(
            chats.notify_anyway,
        )
        self.search = to_raw_response_wrapper(
            chats.search,
        )
        self.start = to_raw_response_wrapper(
            chats.start,
        )

    @cached_property
    def reminders(self) -> RemindersResourceWithRawResponse:
        """Manage reminders for chats"""
        return RemindersResourceWithRawResponse(self._chats.reminders)

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        """Manage chat messages"""
        return MessagesResourceWithRawResponse(self._chats.messages)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_raw_response_wrapper(
            chats.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            chats.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            chats.update,
        )
        self.list = async_to_raw_response_wrapper(
            chats.list,
        )
        self.archive = async_to_raw_response_wrapper(
            chats.archive,
        )
        self.mark_read = async_to_raw_response_wrapper(
            chats.mark_read,
        )
        self.mark_unread = async_to_raw_response_wrapper(
            chats.mark_unread,
        )
        self.notify_anyway = async_to_raw_response_wrapper(
            chats.notify_anyway,
        )
        self.search = async_to_raw_response_wrapper(
            chats.search,
        )
        self.start = async_to_raw_response_wrapper(
            chats.start,
        )

    @cached_property
    def reminders(self) -> AsyncRemindersResourceWithRawResponse:
        """Manage reminders for chats"""
        return AsyncRemindersResourceWithRawResponse(self._chats.reminders)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        """Manage chat messages"""
        return AsyncMessagesResourceWithRawResponse(self._chats.messages)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.create = to_streamed_response_wrapper(
            chats.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            chats.update,
        )
        self.list = to_streamed_response_wrapper(
            chats.list,
        )
        self.archive = to_streamed_response_wrapper(
            chats.archive,
        )
        self.mark_read = to_streamed_response_wrapper(
            chats.mark_read,
        )
        self.mark_unread = to_streamed_response_wrapper(
            chats.mark_unread,
        )
        self.notify_anyway = to_streamed_response_wrapper(
            chats.notify_anyway,
        )
        self.search = to_streamed_response_wrapper(
            chats.search,
        )
        self.start = to_streamed_response_wrapper(
            chats.start,
        )

    @cached_property
    def reminders(self) -> RemindersResourceWithStreamingResponse:
        """Manage reminders for chats"""
        return RemindersResourceWithStreamingResponse(self._chats.reminders)

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        """Manage chat messages"""
        return MessagesResourceWithStreamingResponse(self._chats.messages)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.create = async_to_streamed_response_wrapper(
            chats.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            chats.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            chats.update,
        )
        self.list = async_to_streamed_response_wrapper(
            chats.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            chats.archive,
        )
        self.mark_read = async_to_streamed_response_wrapper(
            chats.mark_read,
        )
        self.mark_unread = async_to_streamed_response_wrapper(
            chats.mark_unread,
        )
        self.notify_anyway = async_to_streamed_response_wrapper(
            chats.notify_anyway,
        )
        self.search = async_to_streamed_response_wrapper(
            chats.search,
        )
        self.start = async_to_streamed_response_wrapper(
            chats.start,
        )

    @cached_property
    def reminders(self) -> AsyncRemindersResourceWithStreamingResponse:
        """Manage reminders for chats"""
        return AsyncRemindersResourceWithStreamingResponse(self._chats.reminders)

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        """Manage chat messages"""
        return AsyncMessagesResourceWithStreamingResponse(self._chats.messages)
