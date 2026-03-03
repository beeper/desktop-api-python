# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, BeeperDesktopError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.focus_response import FocusResponse
from .types.search_response import SearchResponse

if TYPE_CHECKING:
    from .resources import info, chats, assets, accounts, messages
    from .resources.info import InfoResource, AsyncInfoResource
    from .resources.assets import AssetsResource, AsyncAssetsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.chats.chats import ChatsResource, AsyncChatsResource
    from .resources.accounts.accounts import AccountsResource, AsyncAccountsResource

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

    @cached_property
    def accounts(self) -> AccountsResource:
        """Manage connected chat accounts"""
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def chats(self) -> ChatsResource:
        """Manage chats"""
        from .resources.chats import ChatsResource

        return ChatsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        """Manage messages in chats"""
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def assets(self) -> AssetsResource:
        """Manage assets in Beeper Desktop, like message attachments"""
        from .resources.assets import AssetsResource

        return AssetsResource(self)

    @cached_property
    def info(self) -> InfoResource:
        """Control the Beeper Desktop application"""
        from .resources.info import InfoResource

        return InfoResource(self)

    @cached_property
    def with_raw_response(self) -> BeeperDesktopWithRawResponse:
        return BeeperDesktopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BeeperDesktopWithStreamedResponse:
        return BeeperDesktopWithStreamedResponse(self)

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
        via search-chats.

        Args:
          query: User-typed search text. Literal word matching (non-semantic).

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

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Manage connected chat accounts"""
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def chats(self) -> AsyncChatsResource:
        """Manage chats"""
        from .resources.chats import AsyncChatsResource

        return AsyncChatsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Manage messages in chats"""
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def assets(self) -> AsyncAssetsResource:
        """Manage assets in Beeper Desktop, like message attachments"""
        from .resources.assets import AsyncAssetsResource

        return AsyncAssetsResource(self)

    @cached_property
    def info(self) -> AsyncInfoResource:
        """Control the Beeper Desktop application"""
        from .resources.info import AsyncInfoResource

        return AsyncInfoResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncBeeperDesktopWithRawResponse:
        return AsyncBeeperDesktopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBeeperDesktopWithStreamedResponse:
        return AsyncBeeperDesktopWithStreamedResponse(self)

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
        via search-chats.

        Args:
          query: User-typed search text. Literal word matching (non-semantic).

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
    _client: BeeperDesktop

    def __init__(self, client: BeeperDesktop) -> None:
        self._client = client

        self.focus = to_raw_response_wrapper(
            client.focus,
        )
        self.search = to_raw_response_wrapper(
            client.search,
        )

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        """Manage connected chat accounts"""
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithRawResponse:
        """Manage chats"""
        from .resources.chats import ChatsResourceWithRawResponse

        return ChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        """Manage messages in chats"""
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def assets(self) -> assets.AssetsResourceWithRawResponse:
        """Manage assets in Beeper Desktop, like message attachments"""
        from .resources.assets import AssetsResourceWithRawResponse

        return AssetsResourceWithRawResponse(self._client.assets)

    @cached_property
    def info(self) -> info.InfoResourceWithRawResponse:
        """Control the Beeper Desktop application"""
        from .resources.info import InfoResourceWithRawResponse

        return InfoResourceWithRawResponse(self._client.info)


class AsyncBeeperDesktopWithRawResponse:
    _client: AsyncBeeperDesktop

    def __init__(self, client: AsyncBeeperDesktop) -> None:
        self._client = client

        self.focus = async_to_raw_response_wrapper(
            client.focus,
        )
        self.search = async_to_raw_response_wrapper(
            client.search,
        )

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        """Manage connected chat accounts"""
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithRawResponse:
        """Manage chats"""
        from .resources.chats import AsyncChatsResourceWithRawResponse

        return AsyncChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        """Manage messages in chats"""
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def assets(self) -> assets.AsyncAssetsResourceWithRawResponse:
        """Manage assets in Beeper Desktop, like message attachments"""
        from .resources.assets import AsyncAssetsResourceWithRawResponse

        return AsyncAssetsResourceWithRawResponse(self._client.assets)

    @cached_property
    def info(self) -> info.AsyncInfoResourceWithRawResponse:
        """Control the Beeper Desktop application"""
        from .resources.info import AsyncInfoResourceWithRawResponse

        return AsyncInfoResourceWithRawResponse(self._client.info)


class BeeperDesktopWithStreamedResponse:
    _client: BeeperDesktop

    def __init__(self, client: BeeperDesktop) -> None:
        self._client = client

        self.focus = to_streamed_response_wrapper(
            client.focus,
        )
        self.search = to_streamed_response_wrapper(
            client.search,
        )

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        """Manage connected chat accounts"""
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithStreamingResponse:
        """Manage chats"""
        from .resources.chats import ChatsResourceWithStreamingResponse

        return ChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        """Manage messages in chats"""
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def assets(self) -> assets.AssetsResourceWithStreamingResponse:
        """Manage assets in Beeper Desktop, like message attachments"""
        from .resources.assets import AssetsResourceWithStreamingResponse

        return AssetsResourceWithStreamingResponse(self._client.assets)

    @cached_property
    def info(self) -> info.InfoResourceWithStreamingResponse:
        """Control the Beeper Desktop application"""
        from .resources.info import InfoResourceWithStreamingResponse

        return InfoResourceWithStreamingResponse(self._client.info)


class AsyncBeeperDesktopWithStreamedResponse:
    _client: AsyncBeeperDesktop

    def __init__(self, client: AsyncBeeperDesktop) -> None:
        self._client = client

        self.focus = async_to_streamed_response_wrapper(
            client.focus,
        )
        self.search = async_to_streamed_response_wrapper(
            client.search,
        )

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        """Manage connected chat accounts"""
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithStreamingResponse:
        """Manage chats"""
        from .resources.chats import AsyncChatsResourceWithStreamingResponse

        return AsyncChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        """Manage messages in chats"""
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def assets(self) -> assets.AsyncAssetsResourceWithStreamingResponse:
        """Manage assets in Beeper Desktop, like message attachments"""
        from .resources.assets import AsyncAssetsResourceWithStreamingResponse

        return AsyncAssetsResourceWithStreamingResponse(self._client.assets)

    @cached_property
    def info(self) -> info.AsyncInfoResourceWithStreamingResponse:
        """Control the Beeper Desktop application"""
        from .resources.info import AsyncInfoResourceWithStreamingResponse

        return AsyncInfoResourceWithStreamingResponse(self._client.info)


Client = BeeperDesktop

AsyncClient = AsyncBeeperDesktop
