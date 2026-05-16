# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.app.e2ee.verification import SaStartResponse, SaConfirmResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_confirm(self, client: BeeperDesktop) -> None:
        sa = client.app.e2ee.verification.sas.confirm(
            "x",
        )
        assert_matches_type(SaConfirmResponse, sa, path=["response"])

    @parametrize
    def test_raw_response_confirm(self, client: BeeperDesktop) -> None:
        response = client.app.e2ee.verification.sas.with_raw_response.confirm(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sa = response.parse()
        assert_matches_type(SaConfirmResponse, sa, path=["response"])

    @parametrize
    def test_streaming_response_confirm(self, client: BeeperDesktop) -> None:
        with client.app.e2ee.verification.sas.with_streaming_response.confirm(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sa = response.parse()
            assert_matches_type(SaConfirmResponse, sa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_confirm(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            client.app.e2ee.verification.sas.with_raw_response.confirm(
                "",
            )

    @parametrize
    def test_method_start(self, client: BeeperDesktop) -> None:
        sa = client.app.e2ee.verification.sas.start(
            "x",
        )
        assert_matches_type(SaStartResponse, sa, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: BeeperDesktop) -> None:
        response = client.app.e2ee.verification.sas.with_raw_response.start(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sa = response.parse()
        assert_matches_type(SaStartResponse, sa, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: BeeperDesktop) -> None:
        with client.app.e2ee.verification.sas.with_streaming_response.start(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sa = response.parse()
            assert_matches_type(SaStartResponse, sa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_start(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            client.app.e2ee.verification.sas.with_raw_response.start(
                "",
            )


class TestAsyncSas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_confirm(self, async_client: AsyncBeeperDesktop) -> None:
        sa = await async_client.app.e2ee.verification.sas.confirm(
            "x",
        )
        assert_matches_type(SaConfirmResponse, sa, path=["response"])

    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.e2ee.verification.sas.with_raw_response.confirm(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sa = await response.parse()
        assert_matches_type(SaConfirmResponse, sa, path=["response"])

    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.e2ee.verification.sas.with_streaming_response.confirm(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sa = await response.parse()
            assert_matches_type(SaConfirmResponse, sa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_confirm(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            await async_client.app.e2ee.verification.sas.with_raw_response.confirm(
                "",
            )

    @parametrize
    async def test_method_start(self, async_client: AsyncBeeperDesktop) -> None:
        sa = await async_client.app.e2ee.verification.sas.start(
            "x",
        )
        assert_matches_type(SaStartResponse, sa, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.e2ee.verification.sas.with_raw_response.start(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sa = await response.parse()
        assert_matches_type(SaStartResponse, sa, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.e2ee.verification.sas.with_streaming_response.start(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sa = await response.parse()
            assert_matches_type(SaStartResponse, sa, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_start(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            await async_client.app.e2ee.verification.sas.with_raw_response.start(
                "",
            )
