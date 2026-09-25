# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import LoginSession
from beeper_desktop_api.types.bridges import LoginSessionCancelResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoginSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BeeperDesktop) -> None:
        login_session = client.bridges.login_sessions.create(
            bridge_id="local-whatsapp",
        )
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: BeeperDesktop) -> None:
        login_session = client.bridges.login_sessions.create(
            bridge_id="local-whatsapp",
            account_id="x",
            flow_id="x",
            login_id="x",
        )
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: BeeperDesktop) -> None:
        response = client.bridges.login_sessions.with_raw_response.create(
            bridge_id="local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login_session = response.parse()
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: BeeperDesktop) -> None:
        with client.bridges.login_sessions.with_streaming_response.create(
            bridge_id="local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login_session = response.parse()
            assert_matches_type(LoginSession, login_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.login_sessions.with_raw_response.create(
                bridge_id="",
            )

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        login_session = client.bridges.login_sessions.retrieve(
            login_session_id="123",
            bridge_id="local-whatsapp",
        )
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.bridges.login_sessions.with_raw_response.retrieve(
            login_session_id="123",
            bridge_id="local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login_session = response.parse()
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.bridges.login_sessions.with_streaming_response.retrieve(
            login_session_id="123",
            bridge_id="local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login_session = response.parse()
            assert_matches_type(LoginSession, login_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.login_sessions.with_raw_response.retrieve(
                login_session_id="123",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_session_id` but received ''"):
            client.bridges.login_sessions.with_raw_response.retrieve(
                login_session_id="",
                bridge_id="local-whatsapp",
            )

    @parametrize
    def test_method_cancel(self, client: BeeperDesktop) -> None:
        login_session = client.bridges.login_sessions.cancel(
            login_session_id="123",
            bridge_id="local-whatsapp",
        )
        assert_matches_type(LoginSessionCancelResponse, login_session, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: BeeperDesktop) -> None:
        response = client.bridges.login_sessions.with_raw_response.cancel(
            login_session_id="123",
            bridge_id="local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login_session = response.parse()
        assert_matches_type(LoginSessionCancelResponse, login_session, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: BeeperDesktop) -> None:
        with client.bridges.login_sessions.with_streaming_response.cancel(
            login_session_id="123",
            bridge_id="local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login_session = response.parse()
            assert_matches_type(LoginSessionCancelResponse, login_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.login_sessions.with_raw_response.cancel(
                login_session_id="123",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_session_id` but received ''"):
            client.bridges.login_sessions.with_raw_response.cancel(
                login_session_id="",
                bridge_id="local-whatsapp",
            )


class TestAsyncLoginSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBeeperDesktop) -> None:
        login_session = await async_client.bridges.login_sessions.create(
            bridge_id="local-whatsapp",
        )
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        login_session = await async_client.bridges.login_sessions.create(
            bridge_id="local-whatsapp",
            account_id="x",
            flow_id="x",
            login_id="x",
        )
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.login_sessions.with_raw_response.create(
            bridge_id="local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login_session = await response.parse()
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.login_sessions.with_streaming_response.create(
            bridge_id="local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login_session = await response.parse()
            assert_matches_type(LoginSession, login_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.login_sessions.with_raw_response.create(
                bridge_id="",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        login_session = await async_client.bridges.login_sessions.retrieve(
            login_session_id="123",
            bridge_id="local-whatsapp",
        )
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.login_sessions.with_raw_response.retrieve(
            login_session_id="123",
            bridge_id="local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login_session = await response.parse()
        assert_matches_type(LoginSession, login_session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.login_sessions.with_streaming_response.retrieve(
            login_session_id="123",
            bridge_id="local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login_session = await response.parse()
            assert_matches_type(LoginSession, login_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.login_sessions.with_raw_response.retrieve(
                login_session_id="123",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_session_id` but received ''"):
            await async_client.bridges.login_sessions.with_raw_response.retrieve(
                login_session_id="",
                bridge_id="local-whatsapp",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncBeeperDesktop) -> None:
        login_session = await async_client.bridges.login_sessions.cancel(
            login_session_id="123",
            bridge_id="local-whatsapp",
        )
        assert_matches_type(LoginSessionCancelResponse, login_session, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.login_sessions.with_raw_response.cancel(
            login_session_id="123",
            bridge_id="local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login_session = await response.parse()
        assert_matches_type(LoginSessionCancelResponse, login_session, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.login_sessions.with_streaming_response.cancel(
            login_session_id="123",
            bridge_id="local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login_session = await response.parse()
            assert_matches_type(LoginSessionCancelResponse, login_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.login_sessions.with_raw_response.cancel(
                login_session_id="123",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_session_id` but received ''"):
            await async_client.bridges.login_sessions.with_raw_response.cancel(
                login_session_id="",
                bridge_id="local-whatsapp",
            )
