# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.app.e2ee import (
    RecoveryCodeVerifyResponse,
    RecoveryCodeMarkBackedUpResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecoveryCode:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_mark_backed_up(self, client: BeeperDesktop) -> None:
        recovery_code = client.app.e2ee.recovery_code.mark_backed_up()
        assert_matches_type(RecoveryCodeMarkBackedUpResponse, recovery_code, path=["response"])

    @parametrize
    def test_raw_response_mark_backed_up(self, client: BeeperDesktop) -> None:
        response = client.app.e2ee.recovery_code.with_raw_response.mark_backed_up()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recovery_code = response.parse()
        assert_matches_type(RecoveryCodeMarkBackedUpResponse, recovery_code, path=["response"])

    @parametrize
    def test_streaming_response_mark_backed_up(self, client: BeeperDesktop) -> None:
        with client.app.e2ee.recovery_code.with_streaming_response.mark_backed_up() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recovery_code = response.parse()
            assert_matches_type(RecoveryCodeMarkBackedUpResponse, recovery_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_verify(self, client: BeeperDesktop) -> None:
        recovery_code = client.app.e2ee.recovery_code.verify(
            recovery_code="x",
        )
        assert_matches_type(RecoveryCodeVerifyResponse, recovery_code, path=["response"])

    @parametrize
    def test_raw_response_verify(self, client: BeeperDesktop) -> None:
        response = client.app.e2ee.recovery_code.with_raw_response.verify(
            recovery_code="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recovery_code = response.parse()
        assert_matches_type(RecoveryCodeVerifyResponse, recovery_code, path=["response"])

    @parametrize
    def test_streaming_response_verify(self, client: BeeperDesktop) -> None:
        with client.app.e2ee.recovery_code.with_streaming_response.verify(
            recovery_code="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recovery_code = response.parse()
            assert_matches_type(RecoveryCodeVerifyResponse, recovery_code, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRecoveryCode:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_mark_backed_up(self, async_client: AsyncBeeperDesktop) -> None:
        recovery_code = await async_client.app.e2ee.recovery_code.mark_backed_up()
        assert_matches_type(RecoveryCodeMarkBackedUpResponse, recovery_code, path=["response"])

    @parametrize
    async def test_raw_response_mark_backed_up(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.e2ee.recovery_code.with_raw_response.mark_backed_up()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recovery_code = await response.parse()
        assert_matches_type(RecoveryCodeMarkBackedUpResponse, recovery_code, path=["response"])

    @parametrize
    async def test_streaming_response_mark_backed_up(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.e2ee.recovery_code.with_streaming_response.mark_backed_up() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recovery_code = await response.parse()
            assert_matches_type(RecoveryCodeMarkBackedUpResponse, recovery_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_verify(self, async_client: AsyncBeeperDesktop) -> None:
        recovery_code = await async_client.app.e2ee.recovery_code.verify(
            recovery_code="x",
        )
        assert_matches_type(RecoveryCodeVerifyResponse, recovery_code, path=["response"])

    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.e2ee.recovery_code.with_raw_response.verify(
            recovery_code="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recovery_code = await response.parse()
        assert_matches_type(RecoveryCodeVerifyResponse, recovery_code, path=["response"])

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.e2ee.recovery_code.with_streaming_response.verify(
            recovery_code="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recovery_code = await response.parse()
            assert_matches_type(RecoveryCodeVerifyResponse, recovery_code, path=["response"])

        assert cast(Any, response.is_closed) is True
