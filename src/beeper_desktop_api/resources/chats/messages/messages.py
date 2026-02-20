# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .reactions import (
    ReactionsResource,
    AsyncReactionsResource,
    ReactionsResourceWithRawResponse,
    AsyncReactionsResourceWithRawResponse,
    ReactionsResourceWithStreamingResponse,
    AsyncReactionsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    """Manage chat messages"""

    @cached_property
    def reactions(self) -> ReactionsResource:
        """Manage message reactions"""
        return ReactionsResource(self._client)

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


class AsyncMessagesResource(AsyncAPIResource):
    """Manage chat messages"""

    @cached_property
    def reactions(self) -> AsyncReactionsResource:
        """Manage message reactions"""
        return AsyncReactionsResource(self._client)

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


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

    @cached_property
    def reactions(self) -> ReactionsResourceWithRawResponse:
        """Manage message reactions"""
        return ReactionsResourceWithRawResponse(self._messages.reactions)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithRawResponse:
        """Manage message reactions"""
        return AsyncReactionsResourceWithRawResponse(self._messages.reactions)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

    @cached_property
    def reactions(self) -> ReactionsResourceWithStreamingResponse:
        """Manage message reactions"""
        return ReactionsResourceWithStreamingResponse(self._messages.reactions)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithStreamingResponse:
        """Manage message reactions"""
        return AsyncReactionsResourceWithStreamingResponse(self._messages.reactions)
