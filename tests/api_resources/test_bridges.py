# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import BridgeListResponse, BridgeRetrieveResponse, ProvisioningCapabilities

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBridges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        bridge = client.bridges.retrieve(
            "local-whatsapp",
        )
        assert_matches_type(BridgeRetrieveResponse, bridge, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.bridges.with_raw_response.retrieve(
            "local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bridge = response.parse()
        assert_matches_type(BridgeRetrieveResponse, bridge, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.bridges.with_streaming_response.retrieve(
            "local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bridge = response.parse()
            assert_matches_type(BridgeRetrieveResponse, bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: BeeperDesktop) -> None:
        bridge = client.bridges.list()
        assert_matches_type(BridgeListResponse, bridge, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BeeperDesktop) -> None:
        response = client.bridges.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bridge = response.parse()
        assert_matches_type(BridgeListResponse, bridge, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BeeperDesktop) -> None:
        with client.bridges.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bridge = response.parse()
            assert_matches_type(BridgeListResponse, bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_capabilities(self, client: BeeperDesktop) -> None:
        bridge = client.bridges.retrieve_capabilities(
            "local-whatsapp",
        )
        assert_matches_type(ProvisioningCapabilities, bridge, path=["response"])

    @parametrize
    def test_raw_response_retrieve_capabilities(self, client: BeeperDesktop) -> None:
        response = client.bridges.with_raw_response.retrieve_capabilities(
            "local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bridge = response.parse()
        assert_matches_type(ProvisioningCapabilities, bridge, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_capabilities(self, client: BeeperDesktop) -> None:
        with client.bridges.with_streaming_response.retrieve_capabilities(
            "local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bridge = response.parse()
            assert_matches_type(ProvisioningCapabilities, bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_capabilities(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.with_raw_response.retrieve_capabilities(
                "",
            )


class TestAsyncBridges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        bridge = await async_client.bridges.retrieve(
            "local-whatsapp",
        )
        assert_matches_type(BridgeRetrieveResponse, bridge, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.with_raw_response.retrieve(
            "local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bridge = await response.parse()
        assert_matches_type(BridgeRetrieveResponse, bridge, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.with_streaming_response.retrieve(
            "local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bridge = await response.parse()
            assert_matches_type(BridgeRetrieveResponse, bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBeeperDesktop) -> None:
        bridge = await async_client.bridges.list()
        assert_matches_type(BridgeListResponse, bridge, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bridge = await response.parse()
        assert_matches_type(BridgeListResponse, bridge, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bridge = await response.parse()
            assert_matches_type(BridgeListResponse, bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_capabilities(self, async_client: AsyncBeeperDesktop) -> None:
        bridge = await async_client.bridges.retrieve_capabilities(
            "local-whatsapp",
        )
        assert_matches_type(ProvisioningCapabilities, bridge, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_capabilities(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.with_raw_response.retrieve_capabilities(
            "local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bridge = await response.parse()
        assert_matches_type(ProvisioningCapabilities, bridge, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_capabilities(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.with_streaming_response.retrieve_capabilities(
            "local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bridge = await response.parse()
            assert_matches_type(ProvisioningCapabilities, bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_capabilities(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.with_raw_response.retrieve_capabilities(
                "",
            )
