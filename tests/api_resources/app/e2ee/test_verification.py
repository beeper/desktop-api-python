# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.app.e2ee import (
    VerificationAcceptResponse,
    VerificationCancelResponse,
    VerificationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BeeperDesktop) -> None:
        verification = client.app.e2ee.verification.create()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: BeeperDesktop) -> None:
        verification = client.app.e2ee.verification.create(
            user_id="userID",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: BeeperDesktop) -> None:
        response = client.app.e2ee.verification.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: BeeperDesktop) -> None:
        with client.app.e2ee.verification.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_accept(self, client: BeeperDesktop) -> None:
        verification = client.app.e2ee.verification.accept(
            "x",
        )
        assert_matches_type(VerificationAcceptResponse, verification, path=["response"])

    @parametrize
    def test_raw_response_accept(self, client: BeeperDesktop) -> None:
        response = client.app.e2ee.verification.with_raw_response.accept(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationAcceptResponse, verification, path=["response"])

    @parametrize
    def test_streaming_response_accept(self, client: BeeperDesktop) -> None:
        with client.app.e2ee.verification.with_streaming_response.accept(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationAcceptResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_accept(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            client.app.e2ee.verification.with_raw_response.accept(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: BeeperDesktop) -> None:
        verification = client.app.e2ee.verification.cancel(
            verification_id="x",
        )
        assert_matches_type(VerificationCancelResponse, verification, path=["response"])

    @parametrize
    def test_method_cancel_with_all_params(self, client: BeeperDesktop) -> None:
        verification = client.app.e2ee.verification.cancel(
            verification_id="x",
            code="code",
            reason="reason",
        )
        assert_matches_type(VerificationCancelResponse, verification, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: BeeperDesktop) -> None:
        response = client.app.e2ee.verification.with_raw_response.cancel(
            verification_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationCancelResponse, verification, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: BeeperDesktop) -> None:
        with client.app.e2ee.verification.with_streaming_response.cancel(
            verification_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationCancelResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            client.app.e2ee.verification.with_raw_response.cancel(
                verification_id="",
            )


class TestAsyncVerification:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBeeperDesktop) -> None:
        verification = await async_client.app.e2ee.verification.create()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        verification = await async_client.app.e2ee.verification.create(
            user_id="userID",
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.e2ee.verification.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.e2ee.verification.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_accept(self, async_client: AsyncBeeperDesktop) -> None:
        verification = await async_client.app.e2ee.verification.accept(
            "x",
        )
        assert_matches_type(VerificationAcceptResponse, verification, path=["response"])

    @parametrize
    async def test_raw_response_accept(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.e2ee.verification.with_raw_response.accept(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationAcceptResponse, verification, path=["response"])

    @parametrize
    async def test_streaming_response_accept(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.e2ee.verification.with_streaming_response.accept(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationAcceptResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_accept(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            await async_client.app.e2ee.verification.with_raw_response.accept(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncBeeperDesktop) -> None:
        verification = await async_client.app.e2ee.verification.cancel(
            verification_id="x",
        )
        assert_matches_type(VerificationCancelResponse, verification, path=["response"])

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        verification = await async_client.app.e2ee.verification.cancel(
            verification_id="x",
            code="code",
            reason="reason",
        )
        assert_matches_type(VerificationCancelResponse, verification, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.e2ee.verification.with_raw_response.cancel(
            verification_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationCancelResponse, verification, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.e2ee.verification.with_streaming_response.cancel(
            verification_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationCancelResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `verification_id` but received ''"):
            await async_client.app.e2ee.verification.with_raw_response.cancel(
                verification_id="",
            )
