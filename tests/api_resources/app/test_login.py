# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.app import (
    LoginStartResponse,
    LoginRegisterResponse,
    LoginResponseResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_email(self, client: BeeperDesktop) -> None:
        login = client.app.login.email(
            email="dev@stainless.com",
            request="request",
        )
        assert_matches_type(object, login, path=["response"])

    @parametrize
    def test_raw_response_email(self, client: BeeperDesktop) -> None:
        response = client.app.login.with_raw_response.email(
            email="dev@stainless.com",
            request="request",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(object, login, path=["response"])

    @parametrize
    def test_streaming_response_email(self, client: BeeperDesktop) -> None:
        with client.app.login.with_streaming_response.email(
            email="dev@stainless.com",
            request="request",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(object, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: BeeperDesktop) -> None:
        login = client.app.login.register(
            accept_terms=True,
            lead_token="leadToken",
            request="request",
            username="x",
        )
        assert_matches_type(LoginRegisterResponse, login, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: BeeperDesktop) -> None:
        response = client.app.login.with_raw_response.register(
            accept_terms=True,
            lead_token="leadToken",
            request="request",
            username="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(LoginRegisterResponse, login, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: BeeperDesktop) -> None:
        with client.app.login.with_streaming_response.register(
            accept_terms=True,
            lead_token="leadToken",
            request="request",
            username="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(LoginRegisterResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_response(self, client: BeeperDesktop) -> None:
        login = client.app.login.response(
            request="request",
            response="response",
        )
        assert_matches_type(LoginResponseResponse, login, path=["response"])

    @parametrize
    def test_raw_response_response(self, client: BeeperDesktop) -> None:
        response = client.app.login.with_raw_response.response(
            request="request",
            response="response",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(LoginResponseResponse, login, path=["response"])

    @parametrize
    def test_streaming_response_response(self, client: BeeperDesktop) -> None:
        with client.app.login.with_streaming_response.response(
            request="request",
            response="response",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(LoginResponseResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: BeeperDesktop) -> None:
        login = client.app.login.start()
        assert_matches_type(LoginStartResponse, login, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: BeeperDesktop) -> None:
        response = client.app.login.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(LoginStartResponse, login, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: BeeperDesktop) -> None:
        with client.app.login.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(LoginStartResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLogin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_email(self, async_client: AsyncBeeperDesktop) -> None:
        login = await async_client.app.login.email(
            email="dev@stainless.com",
            request="request",
        )
        assert_matches_type(object, login, path=["response"])

    @parametrize
    async def test_raw_response_email(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.login.with_raw_response.email(
            email="dev@stainless.com",
            request="request",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(object, login, path=["response"])

    @parametrize
    async def test_streaming_response_email(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.login.with_streaming_response.email(
            email="dev@stainless.com",
            request="request",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(object, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncBeeperDesktop) -> None:
        login = await async_client.app.login.register(
            accept_terms=True,
            lead_token="leadToken",
            request="request",
            username="x",
        )
        assert_matches_type(LoginRegisterResponse, login, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.login.with_raw_response.register(
            accept_terms=True,
            lead_token="leadToken",
            request="request",
            username="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(LoginRegisterResponse, login, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.login.with_streaming_response.register(
            accept_terms=True,
            lead_token="leadToken",
            request="request",
            username="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(LoginRegisterResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_response(self, async_client: AsyncBeeperDesktop) -> None:
        login = await async_client.app.login.response(
            request="request",
            response="response",
        )
        assert_matches_type(LoginResponseResponse, login, path=["response"])

    @parametrize
    async def test_raw_response_response(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.login.with_raw_response.response(
            request="request",
            response="response",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(LoginResponseResponse, login, path=["response"])

    @parametrize
    async def test_streaming_response_response(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.login.with_streaming_response.response(
            request="request",
            response="response",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(LoginResponseResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncBeeperDesktop) -> None:
        login = await async_client.app.login.start()
        assert_matches_type(LoginStartResponse, login, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.app.login.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(LoginStartResponse, login, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.app.login.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(LoginStartResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True
