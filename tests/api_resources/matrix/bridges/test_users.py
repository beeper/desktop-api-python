# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.matrix.bridges import (
    UserSearchResponse,
    UserResolveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_resolve(self, client: BeeperDesktop) -> None:
        user = client.matrix.bridges.users.resolve(
            identifier="identifier",
            bridge_id="bridgeID",
        )
        assert_matches_type(UserResolveResponse, user, path=["response"])

    @parametrize
    def test_method_resolve_with_all_params(self, client: BeeperDesktop) -> None:
        user = client.matrix.bridges.users.resolve(
            identifier="identifier",
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        assert_matches_type(UserResolveResponse, user, path=["response"])

    @parametrize
    def test_raw_response_resolve(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.users.with_raw_response.resolve(
            identifier="identifier",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserResolveResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_resolve(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.users.with_streaming_response.resolve(
            identifier="identifier",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserResolveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resolve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.users.with_raw_response.resolve(
                identifier="identifier",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.matrix.bridges.users.with_raw_response.resolve(
                identifier="",
                bridge_id="bridgeID",
            )

    @parametrize
    def test_method_search(self, client: BeeperDesktop) -> None:
        user = client.matrix.bridges.users.search(
            bridge_id="bridgeID",
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: BeeperDesktop) -> None:
        user = client.matrix.bridges.users.search(
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            query="query",
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.users.with_raw_response.search(
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.users.with_streaming_response.search(
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserSearchResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.users.with_raw_response.search(
                bridge_id="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_resolve(self, async_client: AsyncBeeperDesktop) -> None:
        user = await async_client.matrix.bridges.users.resolve(
            identifier="identifier",
            bridge_id="bridgeID",
        )
        assert_matches_type(UserResolveResponse, user, path=["response"])

    @parametrize
    async def test_method_resolve_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        user = await async_client.matrix.bridges.users.resolve(
            identifier="identifier",
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        assert_matches_type(UserResolveResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.users.with_raw_response.resolve(
            identifier="identifier",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserResolveResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.users.with_streaming_response.resolve(
            identifier="identifier",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserResolveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resolve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.users.with_raw_response.resolve(
                identifier="identifier",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.matrix.bridges.users.with_raw_response.resolve(
                identifier="",
                bridge_id="bridgeID",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncBeeperDesktop) -> None:
        user = await async_client.matrix.bridges.users.search(
            bridge_id="bridgeID",
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        user = await async_client.matrix.bridges.users.search(
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            query="query",
        )
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.users.with_raw_response.search(
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserSearchResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.users.with_streaming_response.search(
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserSearchResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.users.with_raw_response.search(
                bridge_id="",
            )
