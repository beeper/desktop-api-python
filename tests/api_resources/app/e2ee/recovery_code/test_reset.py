# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.app.e2ee.recovery_code import (
    ResetCreateResponse,
    ResetConfirmResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReset:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BeeperDesktop) -> None:
        reset = client.app.e2ee.recovery_code.reset.create()
        assert_matches_type(ResetCreateResponse, reset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: BeeperDesktop) -> None:
        reset = client.app.e2ee.recovery_code.reset.create(
            recovery_code="recoveryCode",
        )
        assert_matches_type(ResetCreateResponse, reset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: BeeperDesktop) -> None:
        response = client.app.e2ee.recovery_code.reset.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset = response.parse()
        assert_matches_type(ResetCreateResponse, reset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: BeeperDesktop) -> None:
        with client.app.e2ee.recovery_code.reset.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset = response.parse()
            assert_matches_type(ResetCreateResponse, reset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_confirm(self, client: BeeperDesktop) -> None:
        reset = client.app.e2ee.recovery_code.reset.confirm(
            recovery_code="x",
        )
        assert_matches_type(ResetConfirmResponse, reset, path=["response"])

    @parametrize
    def test_raw_response_confirm(self, client: BeeperDesktop) -> None:
        response = client.app.e2ee.recovery_code.reset.with_raw_response.confirm(
            recovery_code="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset = response.parse()
        assert_matches_type(ResetConfirmResponse, reset, path=["response"])

    @parametrize
    def test_streaming_response_confirm(self, client: BeeperDesktop) -> None:
        with client.app.e2ee.recovery_code.reset.with_streaming_response.confirm(
            recovery_code="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset = response.parse()
            assert_matches_type(ResetConfirmResponse, reset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReset:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBeeperDesktop) -> None:
        reset = await async_client.app.e2ee.recovery_code.reset.create()
        assert_matches_type(ResetCreateResponse, reset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        reset = await async_client.app.e2ee.recovery_code.reset.create(
            recovery_code="recoveryCode",
        )
        assert_matches_type(ResetCreateResponse, reset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.e2ee.recovery_code.reset.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset = await response.parse()
        assert_matches_type(ResetCreateResponse, reset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.e2ee.recovery_code.reset.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset = await response.parse()
            assert_matches_type(ResetCreateResponse, reset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_confirm(self, async_client: AsyncBeeperDesktop) -> None:
        reset = await async_client.app.e2ee.recovery_code.reset.confirm(
            recovery_code="x",
        )
        assert_matches_type(ResetConfirmResponse, reset, path=["response"])

    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.e2ee.recovery_code.reset.with_raw_response.confirm(
            recovery_code="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reset = await response.parse()
        assert_matches_type(ResetConfirmResponse, reset, path=["response"])

    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.e2ee.recovery_code.reset.with_streaming_response.confirm(
            recovery_code="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reset = await response.parse()
            assert_matches_type(ResetConfirmResponse, reset, path=["response"])

        assert cast(Any, response.is_closed) is True
