# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.matrix.bridges import CapabilityRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCapabilities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        capability = client.matrix.bridges.capabilities.retrieve(
            "bridgeID",
        )
        assert_matches_type(CapabilityRetrieveResponse, capability, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.capabilities.with_raw_response.retrieve(
            "bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = response.parse()
        assert_matches_type(CapabilityRetrieveResponse, capability, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.capabilities.with_streaming_response.retrieve(
            "bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = response.parse()
            assert_matches_type(CapabilityRetrieveResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.capabilities.with_raw_response.retrieve(
                "",
            )


class TestAsyncCapabilities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        capability = await async_client.matrix.bridges.capabilities.retrieve(
            "bridgeID",
        )
        assert_matches_type(CapabilityRetrieveResponse, capability, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.capabilities.with_raw_response.retrieve(
            "bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = await response.parse()
        assert_matches_type(CapabilityRetrieveResponse, capability, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.capabilities.with_streaming_response.retrieve(
            "bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = await response.parse()
            assert_matches_type(CapabilityRetrieveResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.capabilities.with_raw_response.retrieve(
                "",
            )
