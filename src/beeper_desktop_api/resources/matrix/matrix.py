# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .rooms.rooms import (
    RoomsResource,
    AsyncRoomsResource,
    RoomsResourceWithRawResponse,
    AsyncRoomsResourceWithRawResponse,
    RoomsResourceWithStreamingResponse,
    AsyncRoomsResourceWithStreamingResponse,
)
from .users.users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .bridges.bridges import (
    BridgesResource,
    AsyncBridgesResource,
    BridgesResourceWithRawResponse,
    AsyncBridgesResourceWithRawResponse,
    BridgesResourceWithStreamingResponse,
    AsyncBridgesResourceWithStreamingResponse,
)

__all__ = ["MatrixResource", "AsyncMatrixResource"]


class MatrixResource(SyncAPIResource):
    """Matrix-compatible APIs for accounts, rooms, and connected network bridges."""

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def rooms(self) -> RoomsResource:
        return RoomsResource(self._client)

    @cached_property
    def bridges(self) -> BridgesResource:
        """Matrix-compatible APIs for connected network bridges."""
        return BridgesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MatrixResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return MatrixResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MatrixResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return MatrixResourceWithStreamingResponse(self)


class AsyncMatrixResource(AsyncAPIResource):
    """Matrix-compatible APIs for accounts, rooms, and connected network bridges."""

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def rooms(self) -> AsyncRoomsResource:
        return AsyncRoomsResource(self._client)

    @cached_property
    def bridges(self) -> AsyncBridgesResource:
        """Matrix-compatible APIs for connected network bridges."""
        return AsyncBridgesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMatrixResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMatrixResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMatrixResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncMatrixResourceWithStreamingResponse(self)


class MatrixResourceWithRawResponse:
    def __init__(self, matrix: MatrixResource) -> None:
        self._matrix = matrix

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._matrix.users)

    @cached_property
    def rooms(self) -> RoomsResourceWithRawResponse:
        return RoomsResourceWithRawResponse(self._matrix.rooms)

    @cached_property
    def bridges(self) -> BridgesResourceWithRawResponse:
        """Matrix-compatible APIs for connected network bridges."""
        return BridgesResourceWithRawResponse(self._matrix.bridges)


class AsyncMatrixResourceWithRawResponse:
    def __init__(self, matrix: AsyncMatrixResource) -> None:
        self._matrix = matrix

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._matrix.users)

    @cached_property
    def rooms(self) -> AsyncRoomsResourceWithRawResponse:
        return AsyncRoomsResourceWithRawResponse(self._matrix.rooms)

    @cached_property
    def bridges(self) -> AsyncBridgesResourceWithRawResponse:
        """Matrix-compatible APIs for connected network bridges."""
        return AsyncBridgesResourceWithRawResponse(self._matrix.bridges)


class MatrixResourceWithStreamingResponse:
    def __init__(self, matrix: MatrixResource) -> None:
        self._matrix = matrix

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._matrix.users)

    @cached_property
    def rooms(self) -> RoomsResourceWithStreamingResponse:
        return RoomsResourceWithStreamingResponse(self._matrix.rooms)

    @cached_property
    def bridges(self) -> BridgesResourceWithStreamingResponse:
        """Matrix-compatible APIs for connected network bridges."""
        return BridgesResourceWithStreamingResponse(self._matrix.bridges)


class AsyncMatrixResourceWithStreamingResponse:
    def __init__(self, matrix: AsyncMatrixResource) -> None:
        self._matrix = matrix

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._matrix.users)

    @cached_property
    def rooms(self) -> AsyncRoomsResourceWithStreamingResponse:
        return AsyncRoomsResourceWithStreamingResponse(self._matrix.rooms)

    @cached_property
    def bridges(self) -> AsyncBridgesResourceWithStreamingResponse:
        """Matrix-compatible APIs for connected network bridges."""
        return AsyncBridgesResourceWithStreamingResponse(self._matrix.bridges)
