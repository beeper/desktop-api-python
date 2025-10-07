# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import UserInfo

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToken:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_info(self, client: BeeperDesktop) -> None:
        token = client.token.info()
        assert_matches_type(UserInfo, token, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: BeeperDesktop) -> None:
        response = client.token.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(UserInfo, token, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: BeeperDesktop) -> None:
        with client.token.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(UserInfo, token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncToken:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_info(self, async_client: AsyncBeeperDesktop) -> None:
        token = await async_client.token.info()
        assert_matches_type(UserInfo, token, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.token.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(UserInfo, token, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.token.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(UserInfo, token, path=["response"])

        assert cast(Any, response.is_closed) is True
