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
from ....types.chats.messages import reaction_add_params, reaction_delete_params
from ....types.chats.messages.reaction_add_response import ReactionAddResponse
from ....types.chats.messages.reaction_delete_response import ReactionDeleteResponse

__all__ = ["ReactionsResource", "AsyncReactionsResource"]


class ReactionsResource(SyncAPIResource):
    """Manage message reactions"""

    @cached_property
    def with_raw_response(self) -> ReactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return ReactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return ReactionsResourceWithStreamingResponse(self)

    def delete(
        self,
        message_id: str,
        *,
        chat_id: str,
        reaction_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReactionDeleteResponse:
        """
        Remove the authenticated user's reaction from an existing message.

        Args:
          chat_id: Unique identifier of the chat.

          reaction_key: Reaction key to remove

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            path_template(
                "/v1/chats/{chat_id}/messages/{message_id}/reactions", chat_id=chat_id, message_id=message_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"reaction_key": reaction_key}, reaction_delete_params.ReactionDeleteParams),
            ),
            cast_to=ReactionDeleteResponse,
        )

    def add(
        self,
        message_id: str,
        *,
        chat_id: str,
        reaction_key: str,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReactionAddResponse:
        """
        Add a reaction to an existing message.

        Args:
          chat_id: Unique identifier of the chat.

          reaction_key: Reaction key to add (emoji, shortcode, or custom emoji key)

          transaction_id: Optional transaction ID for deduplication and local echo tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template(
                "/v1/chats/{chat_id}/messages/{message_id}/reactions", chat_id=chat_id, message_id=message_id
            ),
            body=maybe_transform(
                {
                    "reaction_key": reaction_key,
                    "transaction_id": transaction_id,
                },
                reaction_add_params.ReactionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReactionAddResponse,
        )


class AsyncReactionsResource(AsyncAPIResource):
    """Manage message reactions"""

    @cached_property
    def with_raw_response(self) -> AsyncReactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncReactionsResourceWithStreamingResponse(self)

    async def delete(
        self,
        message_id: str,
        *,
        chat_id: str,
        reaction_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReactionDeleteResponse:
        """
        Remove the authenticated user's reaction from an existing message.

        Args:
          chat_id: Unique identifier of the chat.

          reaction_key: Reaction key to remove

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            path_template(
                "/v1/chats/{chat_id}/messages/{message_id}/reactions", chat_id=chat_id, message_id=message_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"reaction_key": reaction_key}, reaction_delete_params.ReactionDeleteParams
                ),
            ),
            cast_to=ReactionDeleteResponse,
        )

    async def add(
        self,
        message_id: str,
        *,
        chat_id: str,
        reaction_key: str,
        transaction_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReactionAddResponse:
        """
        Add a reaction to an existing message.

        Args:
          chat_id: Unique identifier of the chat.

          reaction_key: Reaction key to add (emoji, shortcode, or custom emoji key)

          transaction_id: Optional transaction ID for deduplication and local echo tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template(
                "/v1/chats/{chat_id}/messages/{message_id}/reactions", chat_id=chat_id, message_id=message_id
            ),
            body=await async_maybe_transform(
                {
                    "reaction_key": reaction_key,
                    "transaction_id": transaction_id,
                },
                reaction_add_params.ReactionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReactionAddResponse,
        )


class ReactionsResourceWithRawResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.delete = to_raw_response_wrapper(
            reactions.delete,
        )
        self.add = to_raw_response_wrapper(
            reactions.add,
        )


class AsyncReactionsResourceWithRawResponse:
    def __init__(self, reactions: AsyncReactionsResource) -> None:
        self._reactions = reactions

        self.delete = async_to_raw_response_wrapper(
            reactions.delete,
        )
        self.add = async_to_raw_response_wrapper(
            reactions.add,
        )


class ReactionsResourceWithStreamingResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.delete = to_streamed_response_wrapper(
            reactions.delete,
        )
        self.add = to_streamed_response_wrapper(
            reactions.add,
        )


class AsyncReactionsResourceWithStreamingResponse:
    def __init__(self, reactions: AsyncReactionsResource) -> None:
        self._reactions = reactions

        self.delete = async_to_streamed_response_wrapper(
            reactions.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            reactions.add,
        )
