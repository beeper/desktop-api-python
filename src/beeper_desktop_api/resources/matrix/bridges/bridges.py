# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .auth import (
    AuthResource,
    AsyncAuthResource,
    AuthResourceWithRawResponse,
    AsyncAuthResourceWithRawResponse,
    AuthResourceWithStreamingResponse,
    AsyncAuthResourceWithStreamingResponse,
)
from .rooms import (
    RoomsResource,
    AsyncRoomsResource,
    RoomsResourceWithRawResponse,
    AsyncRoomsResourceWithRawResponse,
    RoomsResourceWithStreamingResponse,
    AsyncRoomsResourceWithStreamingResponse,
)
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .contacts import (
    ContactsResource,
    AsyncContactsResource,
    ContactsResourceWithRawResponse,
    AsyncContactsResourceWithRawResponse,
    ContactsResourceWithStreamingResponse,
    AsyncContactsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .capabilities import (
    CapabilitiesResource,
    AsyncCapabilitiesResource,
    CapabilitiesResourceWithRawResponse,
    AsyncCapabilitiesResourceWithRawResponse,
    CapabilitiesResourceWithStreamingResponse,
    AsyncCapabilitiesResourceWithStreamingResponse,
)

__all__ = ["BridgesResource", "AsyncBridgesResource"]


class BridgesResource(SyncAPIResource):
    """Matrix-compatible APIs for connected network bridges."""

    @cached_property
    def auth(self) -> AuthResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AuthResource(self._client)

    @cached_property
    def contacts(self) -> ContactsResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return ContactsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return UsersResource(self._client)

    @cached_property
    def rooms(self) -> RoomsResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return RoomsResource(self._client)

    @cached_property
    def capabilities(self) -> CapabilitiesResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return CapabilitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BridgesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return BridgesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BridgesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return BridgesResourceWithStreamingResponse(self)


class AsyncBridgesResource(AsyncAPIResource):
    """Matrix-compatible APIs for connected network bridges."""

    @cached_property
    def auth(self) -> AsyncAuthResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncAuthResource(self._client)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncContactsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncUsersResource(self._client)

    @cached_property
    def rooms(self) -> AsyncRoomsResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncRoomsResource(self._client)

    @cached_property
    def capabilities(self) -> AsyncCapabilitiesResource:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncCapabilitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBridgesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBridgesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBridgesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncBridgesResourceWithStreamingResponse(self)


class BridgesResourceWithRawResponse:
    def __init__(self, bridges: BridgesResource) -> None:
        self._bridges = bridges

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AuthResourceWithRawResponse(self._bridges.auth)

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return ContactsResourceWithRawResponse(self._bridges.contacts)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return UsersResourceWithRawResponse(self._bridges.users)

    @cached_property
    def rooms(self) -> RoomsResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return RoomsResourceWithRawResponse(self._bridges.rooms)

    @cached_property
    def capabilities(self) -> CapabilitiesResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return CapabilitiesResourceWithRawResponse(self._bridges.capabilities)


class AsyncBridgesResourceWithRawResponse:
    def __init__(self, bridges: AsyncBridgesResource) -> None:
        self._bridges = bridges

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncAuthResourceWithRawResponse(self._bridges.auth)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncContactsResourceWithRawResponse(self._bridges.contacts)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncUsersResourceWithRawResponse(self._bridges.users)

    @cached_property
    def rooms(self) -> AsyncRoomsResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncRoomsResourceWithRawResponse(self._bridges.rooms)

    @cached_property
    def capabilities(self) -> AsyncCapabilitiesResourceWithRawResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncCapabilitiesResourceWithRawResponse(self._bridges.capabilities)


class BridgesResourceWithStreamingResponse:
    def __init__(self, bridges: BridgesResource) -> None:
        self._bridges = bridges

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AuthResourceWithStreamingResponse(self._bridges.auth)

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return ContactsResourceWithStreamingResponse(self._bridges.contacts)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return UsersResourceWithStreamingResponse(self._bridges.users)

    @cached_property
    def rooms(self) -> RoomsResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return RoomsResourceWithStreamingResponse(self._bridges.rooms)

    @cached_property
    def capabilities(self) -> CapabilitiesResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return CapabilitiesResourceWithStreamingResponse(self._bridges.capabilities)


class AsyncBridgesResourceWithStreamingResponse:
    def __init__(self, bridges: AsyncBridgesResource) -> None:
        self._bridges = bridges

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncAuthResourceWithStreamingResponse(self._bridges.auth)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncContactsResourceWithStreamingResponse(self._bridges.contacts)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncUsersResourceWithStreamingResponse(self._bridges.users)

    @cached_property
    def rooms(self) -> AsyncRoomsResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncRoomsResourceWithStreamingResponse(self._bridges.rooms)

    @cached_property
    def capabilities(self) -> AsyncCapabilitiesResourceWithStreamingResponse:
        """Matrix-compatible APIs for accounts and connected network bridges."""
        return AsyncCapabilitiesResourceWithStreamingResponse(self._bridges.capabilities)
