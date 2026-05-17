# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.bridges import LoginFlowListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoginFlows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BeeperDesktop) -> None:
        login_flow = client.bridges.login_flows.list(
            "local-whatsapp",
        )
        assert_matches_type(LoginFlowListResponse, login_flow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BeeperDesktop) -> None:
        response = client.bridges.login_flows.with_raw_response.list(
            "local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login_flow = response.parse()
        assert_matches_type(LoginFlowListResponse, login_flow, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BeeperDesktop) -> None:
        with client.bridges.login_flows.with_streaming_response.list(
            "local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login_flow = response.parse()
            assert_matches_type(LoginFlowListResponse, login_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.login_flows.with_raw_response.list(
                "",
            )


class TestAsyncLoginFlows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBeeperDesktop) -> None:
        login_flow = await async_client.bridges.login_flows.list(
            "local-whatsapp",
        )
        assert_matches_type(LoginFlowListResponse, login_flow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.login_flows.with_raw_response.list(
            "local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login_flow = await response.parse()
        assert_matches_type(LoginFlowListResponse, login_flow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.login_flows.with_streaming_response.list(
            "local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login_flow = await response.parse()
            assert_matches_type(LoginFlowListResponse, login_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.login_flows.with_raw_response.list(
                "",
            )
