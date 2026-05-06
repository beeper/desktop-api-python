# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    message_list_params,
    message_send_params,
    message_delete_params,
    message_search_params,
    message_update_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorSearch, AsyncCursorSearch, SyncCursorNoLimit, AsyncCursorNoLimit
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.message import Message
from ..types.message_send_response import MessageSendResponse
from ..types.message_update_response import MessageUpdateResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    """Manage messages in chats"""

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Retrieve a message by final message ID, pendingMessageID, or Matrix event ID.
        Chat ID may be a Beeper chat ID or local chat ID.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          message_id: Message ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template("/v1/chats/{chat_id}/messages/{message_id}", chat_id=chat_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def update(
        self,
        message_id: str,
        *,
        chat_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """Edit the text content of an existing message.

        Messages with attachments cannot
        be edited.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          message_id: Message ID.

          text: New text content for the message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._put(
            path_template("/v1/chats/{chat_id}/messages/{message_id}", chat_id=chat_id, message_id=message_id),
            body=maybe_transform({"text": text}, message_update_params.MessageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateResponse,
        )

    def list(
        self,
        chat_id: str,
        *,
        cursor: str | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorNoLimit[Message]:
        """List all messages in a chat with cursor-based pagination.

        Sorted by timestamp.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get_api_list(
            path_template("/v1/chats/{chat_id}/messages", chat_id=chat_id),
            page=SyncCursorNoLimit[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    def delete(
        self,
        message_id: str,
        *,
        chat_id: str,
        for_everyone: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a message by final message ID.

        Pending message IDs are not accepted
        because messages cannot be deleted while sending.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          message_id: Message ID.

          for_everyone: True to request deletion for everyone when the network supports it; false to
              delete only for the authenticated user when supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/chats/{chat_id}/messages/{message_id}", chat_id=chat_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"for_everyone": for_everyone}, message_delete_params.MessageDeleteParams),
            ),
            cast_to=NoneType,
        )

    def search(
        self,
        *,
        account_ids: SequenceNotStr[str] | Omit = omit,
        chat_ids: SequenceNotStr[str] | Omit = omit,
        chat_type: Literal["group", "single"] | Omit = omit,
        cursor: str | Omit = omit,
        date_after: Union[str, datetime] | Omit = omit,
        date_before: Union[str, datetime] | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        exclude_low_priority: Optional[bool] | Omit = omit,
        include_muted: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        media_types: List[Literal["any", "video", "image", "link", "file"]] | Omit = omit,
        query: str | Omit = omit,
        sender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorSearch[Message]:
        """
        Search messages across chats.

        Args:
          account_ids: Limit search to specific account IDs.

          chat_ids: Limit search to specific chat IDs.

          chat_type: Filter by chat type: 'group' for group chats, 'single' for 1:1 chats.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          date_after: Only include messages with timestamp strictly after this ISO 8601 datetime
              (e.g., '2024-07-01T00:00:00Z' or '2024-07-01T00:00:00+02:00').

          date_before: Only include messages with timestamp strictly before this ISO 8601 datetime
              (e.g., '2024-07-31T23:59:59Z' or '2024-07-31T23:59:59+02:00').

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          exclude_low_priority: Exclude messages marked Low Priority by the user. Default: true. Set to false to
              include all.

          include_muted: Include messages in chats marked as Muted by the user, which are usually less
              important. Default: true. Set to false if the user wants a more refined search.

          limit: Maximum number of messages to return.

          media_types: Filter messages by media types. Use ['any'] for any media type, or specify exact
              types like ['video', 'image']. Omit for no media filtering.

          query: Literal word search (non-semantic). Finds messages containing these EXACT words
              in any order. Use single words users actually type, not concepts or phrases.
              Example: use "dinner" not "dinner plans", use "sick" not "health issues". If
              omitted, returns results filtered only by other parameters.

          sender: Filter by sender: 'me' (messages sent by the authenticated user), 'others'
              (messages sent by others), or a specific user ID string (user.id).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/messages/search",
            page=SyncCursorSearch[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "chat_ids": chat_ids,
                        "chat_type": chat_type,
                        "cursor": cursor,
                        "date_after": date_after,
                        "date_before": date_before,
                        "direction": direction,
                        "exclude_low_priority": exclude_low_priority,
                        "include_muted": include_muted,
                        "limit": limit,
                        "media_types": media_types,
                        "query": query,
                        "sender": sender,
                    },
                    message_search_params.MessageSearchParams,
                ),
            ),
            model=Message,
        )

    def send(
        self,
        chat_id: str,
        *,
        attachment: message_send_params.Attachment | Omit = omit,
        reply_to_message_id: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Send a text message to a specific chat.

        Supports replying to existing messages.
        Returns a pending message ID.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          attachment: Single attachment to send with the message

          reply_to_message_id: Provide a message ID to send this as a reply to an existing message

          text: Draft text. Plain text and Markdown are converted to Matrix HTML with the same
              rules used by send and edit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/v1/chats/{chat_id}/messages", chat_id=chat_id),
            body=maybe_transform(
                {
                    "attachment": attachment,
                    "reply_to_message_id": reply_to_message_id,
                    "text": text,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    """Manage messages in chats"""

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_id: str,
        *,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Message:
        """
        Retrieve a message by final message ID, pendingMessageID, or Matrix event ID.
        Chat ID may be a Beeper chat ID or local chat ID.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          message_id: Message ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template("/v1/chats/{chat_id}/messages/{message_id}", chat_id=chat_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def update(
        self,
        message_id: str,
        *,
        chat_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUpdateResponse:
        """Edit the text content of an existing message.

        Messages with attachments cannot
        be edited.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          message_id: Message ID.

          text: New text content for the message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._put(
            path_template("/v1/chats/{chat_id}/messages/{message_id}", chat_id=chat_id, message_id=message_id),
            body=await async_maybe_transform({"text": text}, message_update_params.MessageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUpdateResponse,
        )

    def list(
        self,
        chat_id: str,
        *,
        cursor: str | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncCursorNoLimit[Message]]:
        """List all messages in a chat with cursor-based pagination.

        Sorted by timestamp.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get_api_list(
            path_template("/v1/chats/{chat_id}/messages", chat_id=chat_id),
            page=AsyncCursorNoLimit[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    async def delete(
        self,
        message_id: str,
        *,
        chat_id: str,
        for_everyone: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a message by final message ID.

        Pending message IDs are not accepted
        because messages cannot be deleted while sending.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          message_id: Message ID.

          for_everyone: True to request deletion for everyone when the network supports it; false to
              delete only for the authenticated user when supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/chats/{chat_id}/messages/{message_id}", chat_id=chat_id, message_id=message_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"for_everyone": for_everyone}, message_delete_params.MessageDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    def search(
        self,
        *,
        account_ids: SequenceNotStr[str] | Omit = omit,
        chat_ids: SequenceNotStr[str] | Omit = omit,
        chat_type: Literal["group", "single"] | Omit = omit,
        cursor: str | Omit = omit,
        date_after: Union[str, datetime] | Omit = omit,
        date_before: Union[str, datetime] | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        exclude_low_priority: Optional[bool] | Omit = omit,
        include_muted: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        media_types: List[Literal["any", "video", "image", "link", "file"]] | Omit = omit,
        query: str | Omit = omit,
        sender: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncCursorSearch[Message]]:
        """
        Search messages across chats.

        Args:
          account_ids: Limit search to specific account IDs.

          chat_ids: Limit search to specific chat IDs.

          chat_type: Filter by chat type: 'group' for group chats, 'single' for 1:1 chats.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          date_after: Only include messages with timestamp strictly after this ISO 8601 datetime
              (e.g., '2024-07-01T00:00:00Z' or '2024-07-01T00:00:00+02:00').

          date_before: Only include messages with timestamp strictly before this ISO 8601 datetime
              (e.g., '2024-07-31T23:59:59Z' or '2024-07-31T23:59:59+02:00').

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          exclude_low_priority: Exclude messages marked Low Priority by the user. Default: true. Set to false to
              include all.

          include_muted: Include messages in chats marked as Muted by the user, which are usually less
              important. Default: true. Set to false if the user wants a more refined search.

          limit: Maximum number of messages to return.

          media_types: Filter messages by media types. Use ['any'] for any media type, or specify exact
              types like ['video', 'image']. Omit for no media filtering.

          query: Literal word search (non-semantic). Finds messages containing these EXACT words
              in any order. Use single words users actually type, not concepts or phrases.
              Example: use "dinner" not "dinner plans", use "sick" not "health issues". If
              omitted, returns results filtered only by other parameters.

          sender: Filter by sender: 'me' (messages sent by the authenticated user), 'others'
              (messages sent by others), or a specific user ID string (user.id).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/messages/search",
            page=AsyncCursorSearch[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "chat_ids": chat_ids,
                        "chat_type": chat_type,
                        "cursor": cursor,
                        "date_after": date_after,
                        "date_before": date_before,
                        "direction": direction,
                        "exclude_low_priority": exclude_low_priority,
                        "include_muted": include_muted,
                        "limit": limit,
                        "media_types": media_types,
                        "query": query,
                        "sender": sender,
                    },
                    message_search_params.MessageSearchParams,
                ),
            ),
            model=Message,
        )

    async def send(
        self,
        chat_id: str,
        *,
        attachment: message_send_params.Attachment | Omit = omit,
        reply_to_message_id: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Send a text message to a specific chat.

        Supports replying to existing messages.
        Returns a pending message ID.

        Args:
          chat_id: Chat ID. Input routes also accept the local chat ID from this Beeper Desktop
              installation when available.

          attachment: Single attachment to send with the message

          reply_to_message_id: Provide a message ID to send this as a reply to an existing message

          text: Draft text. Plain text and Markdown are converted to Matrix HTML with the same
              rules used by send and edit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/v1/chats/{chat_id}/messages", chat_id=chat_id),
            body=await async_maybe_transform(
                {
                    "attachment": attachment,
                    "reply_to_message_id": reply_to_message_id,
                    "text": text,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            messages.update,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.delete = to_raw_response_wrapper(
            messages.delete,
        )
        self.search = to_raw_response_wrapper(
            messages.search,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            messages.update,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            messages.delete,
        )
        self.search = async_to_raw_response_wrapper(
            messages.search,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            messages.update,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.delete = to_streamed_response_wrapper(
            messages.delete,
        )
        self.search = to_streamed_response_wrapper(
            messages.search,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            messages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            messages.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            messages.search,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
