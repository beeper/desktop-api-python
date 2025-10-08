# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import Chat, SearchContactsResponse
from beeper_desktop_api._utils import parse_datetime
from beeper_desktop_api.pagination import SyncCursorSearch, AsyncCursorSearch

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_chats(self, client: BeeperDesktop) -> None:
        search = client.search.chats()
        assert_matches_type(SyncCursorSearch[Chat], search, path=["response"])

    @parametrize
    def test_method_chats_with_all_params(self, client: BeeperDesktop) -> None:
        search = client.search.chats(
            account_ids=[
                "local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
                "local-telegram_ba_QFrb5lrLPhO3OT5MFBeTWv0x4BI",
            ],
            cursor="1725489123456|c29tZUltc2dQYWdl",
            direction="before",
            inbox="primary",
            include_muted=True,
            last_activity_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_activity_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            query="x",
            scope="titles",
            type="single",
            unread_only=True,
        )
        assert_matches_type(SyncCursorSearch[Chat], search, path=["response"])

    @parametrize
    def test_raw_response_chats(self, client: BeeperDesktop) -> None:
        response = client.search.with_raw_response.chats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SyncCursorSearch[Chat], search, path=["response"])

    @parametrize
    def test_streaming_response_chats(self, client: BeeperDesktop) -> None:
        with client.search.with_streaming_response.chats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SyncCursorSearch[Chat], search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_contacts(self, client: BeeperDesktop) -> None:
        search = client.search.contacts(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        )
        assert_matches_type(SearchContactsResponse, search, path=["response"])

    @parametrize
    def test_raw_response_contacts(self, client: BeeperDesktop) -> None:
        response = client.search.with_raw_response.contacts(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchContactsResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_contacts(self, client: BeeperDesktop) -> None:
        with client.search.with_streaming_response.contacts(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchContactsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_contacts(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.search.with_raw_response.contacts(
                account_id="",
                query="x",
            )


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_chats(self, async_client: AsyncBeeperDesktop) -> None:
        search = await async_client.search.chats()
        assert_matches_type(AsyncCursorSearch[Chat], search, path=["response"])

    @parametrize
    async def test_method_chats_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        search = await async_client.search.chats(
            account_ids=[
                "local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
                "local-telegram_ba_QFrb5lrLPhO3OT5MFBeTWv0x4BI",
            ],
            cursor="1725489123456|c29tZUltc2dQYWdl",
            direction="before",
            inbox="primary",
            include_muted=True,
            last_activity_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_activity_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            query="x",
            scope="titles",
            type="single",
            unread_only=True,
        )
        assert_matches_type(AsyncCursorSearch[Chat], search, path=["response"])

    @parametrize
    async def test_raw_response_chats(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.search.with_raw_response.chats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(AsyncCursorSearch[Chat], search, path=["response"])

    @parametrize
    async def test_streaming_response_chats(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.search.with_streaming_response.chats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(AsyncCursorSearch[Chat], search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_contacts(self, async_client: AsyncBeeperDesktop) -> None:
        search = await async_client.search.contacts(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        )
        assert_matches_type(SearchContactsResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_contacts(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.search.with_raw_response.contacts(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchContactsResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_contacts(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.search.with_streaming_response.contacts(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchContactsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_contacts(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.search.with_raw_response.contacts(
                account_id="",
                query="x",
            )
