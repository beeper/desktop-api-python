# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from pydantic import Field as FieldInfo

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncCursorSearch",
    "AsyncCursorSearch",
    "SyncCursorNoLimit",
    "AsyncCursorNoLimit",
    "SyncCursorSortKey",
    "AsyncCursorSortKey",
]

_T = TypeVar("_T")


@runtime_checkable
class CursorSortKeyItem(Protocol):
    sort_key: Optional[str]


class SyncCursorSearch(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
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


class AsyncCursorSearch(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
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


class SyncCursorNoLimit(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
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


class AsyncCursorNoLimit(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
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


class SyncCursorSortKey(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

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
        items = self.items
        if not items:
            return None

        item = cast(Any, items[-1])
        if not isinstance(item, CursorSortKeyItem) or item.sort_key is None:
            # TODO emit warning log
            return None

        return PageInfo(params={"cursor": item.sort_key})


class AsyncCursorSortKey(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

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
        items = self.items
        if not items:
            return None

        item = cast(Any, items[-1])
        if not isinstance(item, CursorSortKeyItem) or item.sort_key is None:
            # TODO emit warning log
            return None

        return PageInfo(params={"cursor": item.sort_key})
