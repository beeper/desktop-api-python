# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.app import (
    SetupStartResponse,
    SetupRegisterResponse,
    SetupResponseResponse,
    SetupRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSetup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        setup = client.app.setup.retrieve()
        assert_matches_type(SetupRetrieveResponse, setup, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.app.setup.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = response.parse()
        assert_matches_type(SetupRetrieveResponse, setup, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.app.setup.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = response.parse()
            assert_matches_type(SetupRetrieveResponse, setup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_email(self, client: BeeperDesktop) -> None:
        setup = client.app.setup.email(
            email="dev@stainless.com",
            setup_request_id="setupRequestID",
        )
        assert setup is None

    @parametrize
    def test_raw_response_email(self, client: BeeperDesktop) -> None:
        response = client.app.setup.with_raw_response.email(
            email="dev@stainless.com",
            setup_request_id="setupRequestID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = response.parse()
        assert setup is None

    @parametrize
    def test_streaming_response_email(self, client: BeeperDesktop) -> None:
        with client.app.setup.with_streaming_response.email(
            email="dev@stainless.com",
            setup_request_id="setupRequestID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = response.parse()
            assert setup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: BeeperDesktop) -> None:
        setup = client.app.setup.register(
            accept_terms=True,
            lead_token="leadToken",
            setup_request_id="setupRequestID",
            username="x",
        )
        assert_matches_type(SetupRegisterResponse, setup, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: BeeperDesktop) -> None:
        response = client.app.setup.with_raw_response.register(
            accept_terms=True,
            lead_token="leadToken",
            setup_request_id="setupRequestID",
            username="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = response.parse()
        assert_matches_type(SetupRegisterResponse, setup, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: BeeperDesktop) -> None:
        with client.app.setup.with_streaming_response.register(
            accept_terms=True,
            lead_token="leadToken",
            setup_request_id="setupRequestID",
            username="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = response.parse()
            assert_matches_type(SetupRegisterResponse, setup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_response(self, client: BeeperDesktop) -> None:
        setup = client.app.setup.response(
            response="response",
            setup_request_id="setupRequestID",
        )
        assert_matches_type(SetupResponseResponse, setup, path=["response"])

    @parametrize
    def test_raw_response_response(self, client: BeeperDesktop) -> None:
        response = client.app.setup.with_raw_response.response(
            response="response",
            setup_request_id="setupRequestID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = response.parse()
        assert_matches_type(SetupResponseResponse, setup, path=["response"])

    @parametrize
    def test_streaming_response_response(self, client: BeeperDesktop) -> None:
        with client.app.setup.with_streaming_response.response(
            response="response",
            setup_request_id="setupRequestID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = response.parse()
            assert_matches_type(SetupResponseResponse, setup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: BeeperDesktop) -> None:
        setup = client.app.setup.start()
        assert_matches_type(SetupStartResponse, setup, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: BeeperDesktop) -> None:
        response = client.app.setup.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = response.parse()
        assert_matches_type(SetupStartResponse, setup, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: BeeperDesktop) -> None:
        with client.app.setup.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = response.parse()
            assert_matches_type(SetupStartResponse, setup, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSetup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        setup = await async_client.app.setup.retrieve()
        assert_matches_type(SetupRetrieveResponse, setup, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.setup.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = await response.parse()
        assert_matches_type(SetupRetrieveResponse, setup, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.setup.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = await response.parse()
            assert_matches_type(SetupRetrieveResponse, setup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_email(self, async_client: AsyncBeeperDesktop) -> None:
        setup = await async_client.app.setup.email(
            email="dev@stainless.com",
            setup_request_id="setupRequestID",
        )
        assert setup is None

    @parametrize
    async def test_raw_response_email(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.setup.with_raw_response.email(
            email="dev@stainless.com",
            setup_request_id="setupRequestID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = await response.parse()
        assert setup is None

    @parametrize
    async def test_streaming_response_email(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.setup.with_streaming_response.email(
            email="dev@stainless.com",
            setup_request_id="setupRequestID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = await response.parse()
            assert setup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncBeeperDesktop) -> None:
        setup = await async_client.app.setup.register(
            accept_terms=True,
            lead_token="leadToken",
            setup_request_id="setupRequestID",
            username="x",
        )
        assert_matches_type(SetupRegisterResponse, setup, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.setup.with_raw_response.register(
            accept_terms=True,
            lead_token="leadToken",
            setup_request_id="setupRequestID",
            username="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = await response.parse()
        assert_matches_type(SetupRegisterResponse, setup, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.setup.with_streaming_response.register(
            accept_terms=True,
            lead_token="leadToken",
            setup_request_id="setupRequestID",
            username="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = await response.parse()
            assert_matches_type(SetupRegisterResponse, setup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_response(self, async_client: AsyncBeeperDesktop) -> None:
        setup = await async_client.app.setup.response(
            response="response",
            setup_request_id="setupRequestID",
        )
        assert_matches_type(SetupResponseResponse, setup, path=["response"])

    @parametrize
    async def test_raw_response_response(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.setup.with_raw_response.response(
            response="response",
            setup_request_id="setupRequestID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = await response.parse()
        assert_matches_type(SetupResponseResponse, setup, path=["response"])

    @parametrize
    async def test_streaming_response_response(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.setup.with_streaming_response.response(
            response="response",
            setup_request_id="setupRequestID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = await response.parse()
            assert_matches_type(SetupResponseResponse, setup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncBeeperDesktop) -> None:
        setup = await async_client.app.setup.start()
        assert_matches_type(SetupStartResponse, setup, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.setup.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setup = await response.parse()
        assert_matches_type(SetupStartResponse, setup, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.setup.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setup = await response.parse()
            assert_matches_type(SetupStartResponse, setup, path=["response"])

        assert cast(Any, response.is_closed) is True
