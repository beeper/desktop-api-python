# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.app.verifications import QrScanResponse, QrConfirmScannedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQr:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_confirm_scanned(self, client: BeeperDesktop) -> None:
        qr = client.app.verifications.qr.confirm_scanned(
            "x",
        )
        assert_matches_type(QrConfirmScannedResponse, qr, path=["response"])

    @parametrize
    def test_raw_response_confirm_scanned(self, client: BeeperDesktop) -> None:
        response = client.app.verifications.qr.with_raw_response.confirm_scanned(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr = response.parse()
        assert_matches_type(QrConfirmScannedResponse, qr, path=["response"])

    @parametrize
    def test_streaming_response_confirm_scanned(self, client: BeeperDesktop) -> None:
        with client.app.verifications.qr.with_streaming_response.confirm_scanned(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr = response.parse()
            assert_matches_type(QrConfirmScannedResponse, qr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_confirm_scanned(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            client.app.verifications.qr.with_raw_response.confirm_scanned(
                "",
            )

    @parametrize
    def test_method_scan(self, client: BeeperDesktop) -> None:
        qr = client.app.verifications.qr.scan(
            data="x",
        )
        assert_matches_type(QrScanResponse, qr, path=["response"])

    @parametrize
    def test_raw_response_scan(self, client: BeeperDesktop) -> None:
        response = client.app.verifications.qr.with_raw_response.scan(
            data="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr = response.parse()
        assert_matches_type(QrScanResponse, qr, path=["response"])

    @parametrize
    def test_streaming_response_scan(self, client: BeeperDesktop) -> None:
        with client.app.verifications.qr.with_streaming_response.scan(
            data="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr = response.parse()
            assert_matches_type(QrScanResponse, qr, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQr:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_confirm_scanned(self, async_client: AsyncBeeperDesktop) -> None:
        qr = await async_client.app.verifications.qr.confirm_scanned(
            "x",
        )
        assert_matches_type(QrConfirmScannedResponse, qr, path=["response"])

    @parametrize
    async def test_raw_response_confirm_scanned(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.verifications.qr.with_raw_response.confirm_scanned(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr = await response.parse()
        assert_matches_type(QrConfirmScannedResponse, qr, path=["response"])

    @parametrize
    async def test_streaming_response_confirm_scanned(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.verifications.qr.with_streaming_response.confirm_scanned(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr = await response.parse()
            assert_matches_type(QrConfirmScannedResponse, qr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_confirm_scanned(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            await async_client.app.verifications.qr.with_raw_response.confirm_scanned(
                "",
            )

    @parametrize
    async def test_method_scan(self, async_client: AsyncBeeperDesktop) -> None:
        qr = await async_client.app.verifications.qr.scan(
            data="x",
        )
        assert_matches_type(QrScanResponse, qr, path=["response"])

    @parametrize
    async def test_raw_response_scan(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.verifications.qr.with_raw_response.scan(
            data="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr = await response.parse()
        assert_matches_type(QrScanResponse, qr, path=["response"])

    @parametrize
    async def test_streaming_response_scan(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.verifications.qr.with_streaming_response.scan(
            data="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr = await response.parse()
            assert_matches_type(QrScanResponse, qr, path=["response"])

        assert cast(Any, response.is_closed) is True
