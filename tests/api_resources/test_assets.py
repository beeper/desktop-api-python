# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import (
    AssetUploadResponse,
    AssetDownloadResponse,
    AssetUploadBase64Response,
)
from beeper_desktop_api._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_serve(self, client: BeeperDesktop, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/serve").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        asset = client.assets.serve(
            url="x",
        )
        assert asset.is_closed
        assert asset.json() == {"foo": "bar"}
        assert cast(Any, asset.is_closed) is True
        assert isinstance(asset, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_serve(self, client: BeeperDesktop, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/serve").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        asset = client.assets.with_raw_response.serve(
            url="x",
        )

        assert asset.is_closed is True
        assert asset.http_request.headers.get("X-Stainless-Lang") == "python"
        assert asset.json() == {"foo": "bar"}
        assert isinstance(asset, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_serve(self, client: BeeperDesktop, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/serve").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.assets.with_streaming_response.serve(
            url="x",
        ) as asset:
            assert not asset.is_closed
            assert asset.http_request.headers.get("X-Stainless-Lang") == "python"

            assert asset.json() == {"foo": "bar"}
            assert cast(Any, asset.is_closed) is True
            assert isinstance(asset, StreamedBinaryAPIResponse)

        assert cast(Any, asset.is_closed) is True

    @parametrize
    def test_method_upload(self, client: BeeperDesktop) -> None:
        asset = client.assets.upload(
            file=b"Example data",
        )
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    def test_method_upload_with_all_params(self, client: BeeperDesktop) -> None:
        asset = client.assets.upload(
            file=b"Example data",
            file_name="fileName",
            mime_type="mimeType",
        )
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: BeeperDesktop) -> None:
        response = client.assets.with_raw_response.upload(
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: BeeperDesktop) -> None:
        with client.assets.with_streaming_response.upload(
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetUploadResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_base64(self, client: BeeperDesktop) -> None:
        asset = client.assets.upload_base64(
            content="x",
        )
        assert_matches_type(AssetUploadBase64Response, asset, path=["response"])

    @parametrize
    def test_method_upload_base64_with_all_params(self, client: BeeperDesktop) -> None:
        asset = client.assets.upload_base64(
            content="x",
            file_name="fileName",
            mime_type="mimeType",
        )
        assert_matches_type(AssetUploadBase64Response, asset, path=["response"])

    @parametrize
    def test_raw_response_upload_base64(self, client: BeeperDesktop) -> None:
        response = client.assets.with_raw_response.upload_base64(
            content="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetUploadBase64Response, asset, path=["response"])

    @parametrize
    def test_streaming_response_upload_base64(self, client: BeeperDesktop) -> None:
        with client.assets.with_streaming_response.upload_base64(
            content="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetUploadBase64Response, asset, path=["response"])

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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_serve(self, async_client: AsyncBeeperDesktop, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/serve").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        asset = await async_client.assets.serve(
            url="x",
        )
        assert asset.is_closed
        assert await asset.json() == {"foo": "bar"}
        assert cast(Any, asset.is_closed) is True
        assert isinstance(asset, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_serve(self, async_client: AsyncBeeperDesktop, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/serve").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        asset = await async_client.assets.with_raw_response.serve(
            url="x",
        )

        assert asset.is_closed is True
        assert asset.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await asset.json() == {"foo": "bar"}
        assert isinstance(asset, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_serve(self, async_client: AsyncBeeperDesktop, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/assets/serve").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.assets.with_streaming_response.serve(
            url="x",
        ) as asset:
            assert not asset.is_closed
            assert asset.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await asset.json() == {"foo": "bar"}
            assert cast(Any, asset.is_closed) is True
            assert isinstance(asset, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, asset.is_closed) is True

    @parametrize
    async def test_method_upload(self, async_client: AsyncBeeperDesktop) -> None:
        asset = await async_client.assets.upload(
            file=b"Example data",
        )
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        asset = await async_client.assets.upload(
            file=b"Example data",
            file_name="fileName",
            mime_type="mimeType",
        )
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.assets.with_raw_response.upload(
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetUploadResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.assets.with_streaming_response.upload(
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetUploadResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_base64(self, async_client: AsyncBeeperDesktop) -> None:
        asset = await async_client.assets.upload_base64(
            content="x",
        )
        assert_matches_type(AssetUploadBase64Response, asset, path=["response"])

    @parametrize
    async def test_method_upload_base64_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        asset = await async_client.assets.upload_base64(
            content="x",
            file_name="fileName",
            mime_type="mimeType",
        )
        assert_matches_type(AssetUploadBase64Response, asset, path=["response"])

    @parametrize
    async def test_raw_response_upload_base64(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.assets.with_raw_response.upload_base64(
            content="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetUploadBase64Response, asset, path=["response"])

    @parametrize
    async def test_streaming_response_upload_base64(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.assets.with_streaming_response.upload_base64(
            content="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetUploadBase64Response, asset, path=["response"])

        assert cast(Any, response.is_closed) is True
