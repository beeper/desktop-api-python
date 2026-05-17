# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.app.login.verification import RecoveryKeyVerifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecoveryKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_verify(self, client: BeeperDesktop) -> None:
        recovery_key = client.app.login.verification.recovery_key.verify(
            recovery_key="x",
        )
        assert_matches_type(RecoveryKeyVerifyResponse, recovery_key, path=["response"])

    @parametrize
    def test_raw_response_verify(self, client: BeeperDesktop) -> None:
        response = client.app.login.verification.recovery_key.with_raw_response.verify(
            recovery_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recovery_key = response.parse()
        assert_matches_type(RecoveryKeyVerifyResponse, recovery_key, path=["response"])

    @parametrize
    def test_streaming_response_verify(self, client: BeeperDesktop) -> None:
        with client.app.login.verification.recovery_key.with_streaming_response.verify(
            recovery_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recovery_key = response.parse()
            assert_matches_type(RecoveryKeyVerifyResponse, recovery_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRecoveryKey:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_verify(self, async_client: AsyncBeeperDesktop) -> None:
        recovery_key = await async_client.app.login.verification.recovery_key.verify(
            recovery_key="x",
        )
        assert_matches_type(RecoveryKeyVerifyResponse, recovery_key, path=["response"])

    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.login.verification.recovery_key.with_raw_response.verify(
            recovery_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recovery_key = await response.parse()
        assert_matches_type(RecoveryKeyVerifyResponse, recovery_key, path=["response"])

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.login.verification.recovery_key.with_streaming_response.verify(
            recovery_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recovery_key = await response.parse()
            assert_matches_type(RecoveryKeyVerifyResponse, recovery_key, path=["response"])

        assert cast(Any, response.is_closed) is True
