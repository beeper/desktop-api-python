# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import ContactSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search(self, client: BeeperDesktop) -> None:
        contact = client.contacts.search(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        )
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: BeeperDesktop) -> None:
        response = client.contacts.with_raw_response.search(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: BeeperDesktop) -> None:
        with client.contacts.with_streaming_response.search(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactSearchResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_search(self, async_client: AsyncBeeperDesktop) -> None:
        contact = await async_client.contacts.search(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        )
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.contacts.with_raw_response.search(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactSearchResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.contacts.with_streaming_response.search(
            account_id="local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactSearchResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
