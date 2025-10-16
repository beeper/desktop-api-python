# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from .contacts import (
    ContactsResource,
    AsyncContactsResource,
    ContactsResourceWithRawResponse,
    AsyncContactsResourceWithRawResponse,
    ContactsResourceWithStreamingResponse,
    AsyncContactsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.account_list_response import AccountListResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    """Manage connected chat accounts"""

    @cached_property
    def contacts(self) -> ContactsResource:
        """Manage contacts on a specific account"""
        return ContactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountListResponse:
        """
        Lists chat accounts across networks (WhatsApp, Telegram, Twitter/X, etc.)
        actively connected to this Beeper Desktop instance
        """
        return self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    """Manage connected chat accounts"""

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        """Manage contacts on a specific account"""
        return AsyncContactsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountListResponse:
        """
        Lists chat accounts across networks (WhatsApp, Telegram, Twitter/X, etc.)
        actively connected to this Beeper Desktop instance
        """
        return await self._get(
            "/v1/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.list = to_raw_response_wrapper(
            accounts.list,
        )

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        """Manage contacts on a specific account"""
        return ContactsResourceWithRawResponse(self._accounts.contacts)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        """Manage contacts on a specific account"""
        return AsyncContactsResourceWithRawResponse(self._accounts.contacts)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.list = to_streamed_response_wrapper(
            accounts.list,
        )

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        """Manage contacts on a specific account"""
        return ContactsResourceWithStreamingResponse(self._accounts.contacts)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        """Manage contacts on a specific account"""
        return AsyncContactsResourceWithStreamingResponse(self._accounts.contacts)
