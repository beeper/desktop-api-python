# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorSearch, AsyncCursorSearch
from ..._base_client import AsyncPaginator, make_request_options
from ...types.accounts import contact_list_params, contact_search_params
from ...types.shared.user import User
from ...types.accounts.contact_search_response import ContactSearchResponse

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    """Manage contacts on a specific account"""

    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return ContactsResourceWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
        cursor: str | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorSearch[User]:
        """
        List merged contacts for a specific account with cursor-based pagination.

        Args:
          account_id: Account ID this resource belongs to.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          limit: Maximum contacts to return per page.

          query: Optional search query for blended contact lookup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/v1/accounts/{account_id}/contacts/list",
            page=SyncCursorSearch[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                        "query": query,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            model=User,
        )

    def search(
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
    ) -> ContactSearchResponse:
        """
        Search contacts on a specific account using merged account contacts, network
        search, and exact identifier lookup.

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
            f"/v1/accounts/{account_id}/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, contact_search_params.ContactSearchParams),
            ),
            cast_to=ContactSearchResponse,
        )


class AsyncContactsResource(AsyncAPIResource):
    """Manage contacts on a specific account"""

    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncContactsResourceWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
        cursor: str | Omit = omit,
        direction: Literal["after", "before"] | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[User, AsyncCursorSearch[User]]:
        """
        List merged contacts for a specific account with cursor-based pagination.

        Args:
          account_id: Account ID this resource belongs to.

          cursor: Opaque pagination cursor; do not inspect. Use together with 'direction'.

          direction: Pagination direction used with 'cursor': 'before' fetches older results, 'after'
              fetches newer results. Defaults to 'before' when only 'cursor' is provided.

          limit: Maximum contacts to return per page.

          query: Optional search query for blended contact lookup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/v1/accounts/{account_id}/contacts/list",
            page=AsyncCursorSearch[User],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "limit": limit,
                        "query": query,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            model=User,
        )

    async def search(
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
    ) -> ContactSearchResponse:
        """
        Search contacts on a specific account using merged account contacts, network
        search, and exact identifier lookup.

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
            f"/v1/accounts/{account_id}/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, contact_search_params.ContactSearchParams),
            ),
            cast_to=ContactSearchResponse,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.search = to_raw_response_wrapper(
            contacts.search,
        )


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.search = async_to_raw_response_wrapper(
            contacts.search,
        )


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.search = to_streamed_response_wrapper(
            contacts.search,
        )


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.search = async_to_streamed_response_wrapper(
            contacts.search,
        )
