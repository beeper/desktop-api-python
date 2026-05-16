# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import AppStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_status(self, client: BeeperDesktop) -> None:
        app = client.app.status()
        assert_matches_type(AppStatusResponse, app, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: BeeperDesktop) -> None:
        response = client.app.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppStatusResponse, app, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: BeeperDesktop) -> None:
        with client.app.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppStatusResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncApp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_status(self, async_client: AsyncBeeperDesktop) -> None:
        app = await async_client.app.status()
        assert_matches_type(AppStatusResponse, app, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppStatusResponse, app, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppStatusResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True
