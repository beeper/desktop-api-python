# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chats import reminder_create_params
from ..._base_client import make_request_options

__all__ = ["RemindersResource", "AsyncRemindersResource"]


class RemindersResource(SyncAPIResource):
    """Manage reminders for chats"""

    @cached_property
    def with_raw_response(self) -> RemindersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return RemindersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RemindersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return RemindersResourceWithStreamingResponse(self)

    def create(
        self,
        chat_id: str,
        *,
        reminder: reminder_create_params.Reminder,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set a reminder for a chat at a specific time

        Args:
          chat_id: Unique identifier of the chat.

          reminder: Reminder configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/chats/{chat_id}/reminders",
            body=maybe_transform({"reminder": reminder}, reminder_create_params.ReminderCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Clear an existing reminder from a chat

        Args:
          chat_id: Unique identifier of the chat.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/chats/{chat_id}/reminders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRemindersResource(AsyncAPIResource):
    """Manage reminders for chats"""

    @cached_property
    def with_raw_response(self) -> AsyncRemindersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRemindersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRemindersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncRemindersResourceWithStreamingResponse(self)

    async def create(
        self,
        chat_id: str,
        *,
        reminder: reminder_create_params.Reminder,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set a reminder for a chat at a specific time

        Args:
          chat_id: Unique identifier of the chat.

          reminder: Reminder configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/chats/{chat_id}/reminders",
            body=await async_maybe_transform({"reminder": reminder}, reminder_create_params.ReminderCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Clear an existing reminder from a chat

        Args:
          chat_id: Unique identifier of the chat.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/chats/{chat_id}/reminders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RemindersResourceWithRawResponse:
    def __init__(self, reminders: RemindersResource) -> None:
        self._reminders = reminders

        self.create = to_raw_response_wrapper(
            reminders.create,
        )
        self.delete = to_raw_response_wrapper(
            reminders.delete,
        )


class AsyncRemindersResourceWithRawResponse:
    def __init__(self, reminders: AsyncRemindersResource) -> None:
        self._reminders = reminders

        self.create = async_to_raw_response_wrapper(
            reminders.create,
        )
        self.delete = async_to_raw_response_wrapper(
            reminders.delete,
        )


class RemindersResourceWithStreamingResponse:
    def __init__(self, reminders: RemindersResource) -> None:
        self._reminders = reminders

        self.create = to_streamed_response_wrapper(
            reminders.create,
        )
        self.delete = to_streamed_response_wrapper(
            reminders.delete,
        )


class AsyncRemindersResourceWithStreamingResponse:
    def __init__(self, reminders: AsyncRemindersResource) -> None:
        self._reminders = reminders

        self.create = async_to_streamed_response_wrapper(
            reminders.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            reminders.delete,
        )
