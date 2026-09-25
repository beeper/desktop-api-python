# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import LoginSession

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_submit(self, client: BeeperDesktop) -> None:
        step = client.bridges.login_sessions.steps.submit(
            step_id="x",
            bridge_id="local-whatsapp",
            login_session_id="123",
            type="user_input",
        )
        assert_matches_type(LoginSession, step, path=["response"])

    @parametrize
    def test_method_submit_with_all_params(self, client: BeeperDesktop) -> None:
        step = client.bridges.login_sessions.steps.submit(
            step_id="x",
            bridge_id="local-whatsapp",
            login_session_id="123",
            type="user_input",
            fields={"foo": "string"},
            last_url="lastURL",
            source="api",
        )
        assert_matches_type(LoginSession, step, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: BeeperDesktop) -> None:
        response = client.bridges.login_sessions.steps.with_raw_response.submit(
            step_id="x",
            bridge_id="local-whatsapp",
            login_session_id="123",
            type="user_input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(LoginSession, step, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: BeeperDesktop) -> None:
        with client.bridges.login_sessions.steps.with_streaming_response.submit(
            step_id="x",
            bridge_id="local-whatsapp",
            login_session_id="123",
            type="user_input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(LoginSession, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.login_sessions.steps.with_raw_response.submit(
                step_id="x",
                bridge_id="",
                login_session_id="123",
                type="user_input",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_session_id` but received ''"):
            client.bridges.login_sessions.steps.with_raw_response.submit(
                step_id="x",
                bridge_id="local-whatsapp",
                login_session_id="",
                type="user_input",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.bridges.login_sessions.steps.with_raw_response.submit(
                step_id="",
                bridge_id="local-whatsapp",
                login_session_id="123",
                type="user_input",
            )


class TestAsyncSteps:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_submit(self, async_client: AsyncBeeperDesktop) -> None:
        step = await async_client.bridges.login_sessions.steps.submit(
            step_id="x",
            bridge_id="local-whatsapp",
            login_session_id="123",
            type="user_input",
        )
        assert_matches_type(LoginSession, step, path=["response"])

    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        step = await async_client.bridges.login_sessions.steps.submit(
            step_id="x",
            bridge_id="local-whatsapp",
            login_session_id="123",
            type="user_input",
            fields={"foo": "string"},
            last_url="lastURL",
            source="api",
        )
        assert_matches_type(LoginSession, step, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.login_sessions.steps.with_raw_response.submit(
            step_id="x",
            bridge_id="local-whatsapp",
            login_session_id="123",
            type="user_input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(LoginSession, step, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.login_sessions.steps.with_streaming_response.submit(
            step_id="x",
            bridge_id="local-whatsapp",
            login_session_id="123",
            type="user_input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(LoginSession, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.login_sessions.steps.with_raw_response.submit(
                step_id="x",
                bridge_id="",
                login_session_id="123",
                type="user_input",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_session_id` but received ''"):
            await async_client.bridges.login_sessions.steps.with_raw_response.submit(
                step_id="x",
                bridge_id="local-whatsapp",
                login_session_id="",
                type="user_input",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.bridges.login_sessions.steps.with_raw_response.submit(
                step_id="",
                bridge_id="local-whatsapp",
                login_session_id="123",
                type="user_input",
            )
