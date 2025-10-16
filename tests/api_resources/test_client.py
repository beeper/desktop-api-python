# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import FocusResponse, SearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_focus(self, client: BeeperDesktop) -> None:
        client_ = client.focus()
        assert_matches_type(FocusResponse, client_, path=["response"])

    @parametrize
    def test_method_focus_with_all_params(self, client: BeeperDesktop) -> None:
        client_ = client.focus(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            draft_attachment_path="draftAttachmentPath",
            draft_text="draftText",
            message_id="messageID",
        )
        assert_matches_type(FocusResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_focus(self, client: BeeperDesktop) -> None:
        response = client.with_raw_response.focus()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(FocusResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_focus(self, client: BeeperDesktop) -> None:
        with client.with_streaming_response.focus() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(FocusResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: BeeperDesktop) -> None:
        client_ = client.search(
            query="x",
        )
        assert_matches_type(SearchResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: BeeperDesktop) -> None:
        response = client.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(SearchResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: BeeperDesktop) -> None:
        with client.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(SearchResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_focus(self, async_client: AsyncBeeperDesktop) -> None:
        client = await async_client.focus()
        assert_matches_type(FocusResponse, client, path=["response"])

    @parametrize
    async def test_method_focus_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        client = await async_client.focus(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            draft_attachment_path="draftAttachmentPath",
            draft_text="draftText",
            message_id="messageID",
        )
        assert_matches_type(FocusResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_focus(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.with_raw_response.focus()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(FocusResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_focus(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.with_streaming_response.focus() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(FocusResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncBeeperDesktop) -> None:
        client = await async_client.search(
            query="x",
        )
        assert_matches_type(SearchResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(SearchResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(SearchResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
