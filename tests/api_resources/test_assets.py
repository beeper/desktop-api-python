# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import AssetDownloadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_download(self, client: BeeperDesktop) -> None:
        asset = client.assets.download(
            url="mxc://example.org/Q4x9CqGz1pB3Oa6XgJ",
        )
        assert_matches_type(AssetDownloadResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_download(self, client: BeeperDesktop) -> None:
        response = client.assets.with_raw_response.download(
            url="mxc://example.org/Q4x9CqGz1pB3Oa6XgJ",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetDownloadResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_download(self, client: BeeperDesktop) -> None:
        with client.assets.with_streaming_response.download(
            url="mxc://example.org/Q4x9CqGz1pB3Oa6XgJ",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetDownloadResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_download(self, async_client: AsyncBeeperDesktop) -> None:
        asset = await async_client.assets.download(
            url="mxc://example.org/Q4x9CqGz1pB3Oa6XgJ",
        )
        assert_matches_type(AssetDownloadResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.assets.with_raw_response.download(
            url="mxc://example.org/Q4x9CqGz1pB3Oa6XgJ",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetDownloadResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.assets.with_streaming_response.download(
            url="mxc://example.org/Q4x9CqGz1pB3Oa6XgJ",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetDownloadResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True
