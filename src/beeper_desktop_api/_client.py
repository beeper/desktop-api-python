# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_focus_params, client_search_params
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    omit,
    not_given,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import assets, messages
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, BeeperDesktopError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.chats import chats
from .resources.accounts import accounts
from .types.focus_response import FocusResponse
from .types.search_response import SearchResponse

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "BeeperDesktop",
    "AsyncBeeperDesktop",
    "Client",
    "AsyncClient",
]


class BeeperDesktop(SyncAPIClient):
    accounts: accounts.AccountsResource
    chats: chats.ChatsResource
    messages: messages.MessagesResource
    assets: assets.AssetsResource
    with_raw_response: BeeperDesktopWithRawResponse
    with_streaming_response: BeeperDesktopWithStreamedResponse

    # client options
    access_token: str

    def __init__(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous BeeperDesktop client instance.

        This automatically infers the `access_token` argument from the `BEEPER_ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("BEEPER_ACCESS_TOKEN")
        if access_token is None:
            raise BeeperDesktopError(
                "The access_token client option must be set either by passing access_token to the client or by setting the BEEPER_ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("BEEPER_DESKTOP_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:23373"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AccountsResource(self)
        self.chats = chats.ChatsResource(self)
        self.messages = messages.MessagesResource(self)
        self.assets = assets.AssetsResource(self)
        self.with_raw_response = BeeperDesktopWithRawResponse(self)
        self.with_streaming_response = BeeperDesktopWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def focus(
        self,
        *,
        chat_id: str | Omit = omit,
        draft_attachment_path: str | Omit = omit,
        draft_text: str | Omit = omit,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FocusResponse:
        """
        Focus Beeper Desktop and optionally navigate to a specific chat, message, or
        pre-fill draft text and attachment.

        Args:
          chat_id: Optional Beeper chat ID (or local chat ID) to focus after opening the app. If
              omitted, only opens/focuses the app.

          draft_attachment_path: Optional draft attachment path to populate in the message input field.

          draft_text: Optional draft text to populate in the message input field.

          message_id: Optional message ID. Jumps to that message in the chat when opening.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/focus",
            body=maybe_transform(
                {
                    "chat_id": chat_id,
                    "draft_attachment_path": draft_attachment_path,
                    "draft_text": draft_text,
                    "message_id": message_id,
                },
                client_focus_params.ClientFocusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FocusResponse,
        )

    def search(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Returns matching chats, participant name matches in groups, and the first page
        of messages in one call. Paginate messages via search-messages. Paginate chats
        via search-chats. Uses the same sorting as the chat search in the app.

        Args:
          query: User-typed search text. Literal word matching (NOT semantic).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get(
            "/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, client_search_params.ClientSearchParams),
            ),
            cast_to=SearchResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBeeperDesktop(AsyncAPIClient):
    accounts: accounts.AsyncAccountsResource
    chats: chats.AsyncChatsResource
    messages: messages.AsyncMessagesResource
    assets: assets.AsyncAssetsResource
    with_raw_response: AsyncBeeperDesktopWithRawResponse
    with_streaming_response: AsyncBeeperDesktopWithStreamedResponse

    # client options
    access_token: str

    def __init__(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBeeperDesktop client instance.

        This automatically infers the `access_token` argument from the `BEEPER_ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("BEEPER_ACCESS_TOKEN")
        if access_token is None:
            raise BeeperDesktopError(
                "The access_token client option must be set either by passing access_token to the client or by setting the BEEPER_ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("BEEPER_DESKTOP_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:23373"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.accounts = accounts.AsyncAccountsResource(self)
        self.chats = chats.AsyncChatsResource(self)
        self.messages = messages.AsyncMessagesResource(self)
        self.assets = assets.AsyncAssetsResource(self)
        self.with_raw_response = AsyncBeeperDesktopWithRawResponse(self)
        self.with_streaming_response = AsyncBeeperDesktopWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def focus(
        self,
        *,
        chat_id: str | Omit = omit,
        draft_attachment_path: str | Omit = omit,
        draft_text: str | Omit = omit,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FocusResponse:
        """
        Focus Beeper Desktop and optionally navigate to a specific chat, message, or
        pre-fill draft text and attachment.

        Args:
          chat_id: Optional Beeper chat ID (or local chat ID) to focus after opening the app. If
              omitted, only opens/focuses the app.

          draft_attachment_path: Optional draft attachment path to populate in the message input field.

          draft_text: Optional draft text to populate in the message input field.

          message_id: Optional message ID. Jumps to that message in the chat when opening.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/focus",
            body=await async_maybe_transform(
                {
                    "chat_id": chat_id,
                    "draft_attachment_path": draft_attachment_path,
                    "draft_text": draft_text,
                    "message_id": message_id,
                },
                client_focus_params.ClientFocusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FocusResponse,
        )

    async def search(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResponse:
        """
        Returns matching chats, participant name matches in groups, and the first page
        of messages in one call. Paginate messages via search-messages. Paginate chats
        via search-chats. Uses the same sorting as the chat search in the app.

        Args:
          query: User-typed search text. Literal word matching (NOT semantic).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.get(
            "/v1/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, client_search_params.ClientSearchParams),
            ),
            cast_to=SearchResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BeeperDesktopWithRawResponse:
    def __init__(self, client: BeeperDesktop) -> None:
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.chats = chats.ChatsResourceWithRawResponse(client.chats)
        self.messages = messages.MessagesResourceWithRawResponse(client.messages)
        self.assets = assets.AssetsResourceWithRawResponse(client.assets)

        self.focus = to_raw_response_wrapper(
            client.focus,
        )
        self.search = to_raw_response_wrapper(
            client.search,
        )


class AsyncBeeperDesktopWithRawResponse:
    def __init__(self, client: AsyncBeeperDesktop) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.chats = chats.AsyncChatsResourceWithRawResponse(client.chats)
        self.messages = messages.AsyncMessagesResourceWithRawResponse(client.messages)
        self.assets = assets.AsyncAssetsResourceWithRawResponse(client.assets)

        self.focus = async_to_raw_response_wrapper(
            client.focus,
        )
        self.search = async_to_raw_response_wrapper(
            client.search,
        )


class BeeperDesktopWithStreamedResponse:
    def __init__(self, client: BeeperDesktop) -> None:
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.chats = chats.ChatsResourceWithStreamingResponse(client.chats)
        self.messages = messages.MessagesResourceWithStreamingResponse(client.messages)
        self.assets = assets.AssetsResourceWithStreamingResponse(client.assets)

        self.focus = to_streamed_response_wrapper(
            client.focus,
        )
        self.search = to_streamed_response_wrapper(
            client.search,
        )


class AsyncBeeperDesktopWithStreamedResponse:
    def __init__(self, client: AsyncBeeperDesktop) -> None:
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.chats = chats.AsyncChatsResourceWithStreamingResponse(client.chats)
        self.messages = messages.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.assets = assets.AsyncAssetsResourceWithStreamingResponse(client.assets)

        self.focus = async_to_streamed_response_wrapper(
            client.focus,
        )
        self.search = async_to_streamed_response_wrapper(
            client.search,
        )


Client = BeeperDesktop

AsyncClient = AsyncBeeperDesktop
