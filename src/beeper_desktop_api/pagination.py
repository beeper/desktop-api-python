# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from .types.chat import Chat
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncCursor", "AsyncCursor", "SyncCursorWithChats", "AsyncCursorWithChats"]

_T = TypeVar("_T")


class SyncCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    oldest_cursor: Optional[str] = FieldInfo(alias="oldestCursor", default=None)
    newest_cursor: Optional[str] = FieldInfo(alias="newestCursor", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        oldest_cursor = self.oldest_cursor
        if not oldest_cursor:
            return None

        return PageInfo(params={"cursor": oldest_cursor})


class AsyncCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    oldest_cursor: Optional[str] = FieldInfo(alias="oldestCursor", default=None)
    newest_cursor: Optional[str] = FieldInfo(alias="newestCursor", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        oldest_cursor = self.oldest_cursor
        if not oldest_cursor:
            return None

        return PageInfo(params={"cursor": oldest_cursor})


class SyncCursorWithChats(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    chats: Optional[Dict[str, Chat]] = None
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    oldest_cursor: Optional[str] = FieldInfo(alias="oldestCursor", default=None)
    newest_cursor: Optional[str] = FieldInfo(alias="newestCursor", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        oldest_cursor = self.oldest_cursor
        if not oldest_cursor:
            return None

        return PageInfo(params={"cursor": oldest_cursor})


class AsyncCursorWithChats(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    chats: Optional[Dict[str, Chat]] = None
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    oldest_cursor: Optional[str] = FieldInfo(alias="oldestCursor", default=None)
    newest_cursor: Optional[str] = FieldInfo(alias="newestCursor", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        oldest_cursor = self.oldest_cursor
        if not oldest_cursor:
            return None

        return PageInfo(params={"cursor": oldest_cursor})
