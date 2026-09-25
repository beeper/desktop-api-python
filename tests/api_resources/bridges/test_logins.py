# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import BridgeLogin
from beeper_desktop_api.types.bridges import LoginListResponse, LoginRemoveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        login = client.bridges.logins.retrieve(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
        )
        assert_matches_type(BridgeLogin, login, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.bridges.logins.with_raw_response.retrieve(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(BridgeLogin, login, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.bridges.logins.with_streaming_response.retrieve(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(BridgeLogin, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.logins.with_raw_response.retrieve(
                login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_id` but received ''"):
            client.bridges.logins.with_raw_response.retrieve(
                login_id="",
                bridge_id="local-whatsapp",
            )

    @parametrize
    def test_method_list(self, client: BeeperDesktop) -> None:
        login = client.bridges.logins.list(
            "local-whatsapp",
        )
        assert_matches_type(LoginListResponse, login, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BeeperDesktop) -> None:
        response = client.bridges.logins.with_raw_response.list(
            "local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(LoginListResponse, login, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BeeperDesktop) -> None:
        with client.bridges.logins.with_streaming_response.list(
            "local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(LoginListResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.logins.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_remove(self, client: BeeperDesktop) -> None:
        login = client.bridges.logins.remove(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
            scope="current-device",
        )
        assert_matches_type(LoginRemoveResponse, login, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: BeeperDesktop) -> None:
        response = client.bridges.logins.with_raw_response.remove(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
            scope="current-device",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = response.parse()
        assert_matches_type(LoginRemoveResponse, login, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: BeeperDesktop) -> None:
        with client.bridges.logins.with_streaming_response.remove(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
            scope="current-device",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = response.parse()
            assert_matches_type(LoginRemoveResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.bridges.logins.with_raw_response.remove(
                login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
                bridge_id="",
                scope="current-device",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_id` but received ''"):
            client.bridges.logins.with_raw_response.remove(
                login_id="",
                bridge_id="local-whatsapp",
                scope="current-device",
            )


class TestAsyncLogins:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        login = await async_client.bridges.logins.retrieve(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
        )
        assert_matches_type(BridgeLogin, login, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.logins.with_raw_response.retrieve(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(BridgeLogin, login, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.logins.with_streaming_response.retrieve(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(BridgeLogin, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.logins.with_raw_response.retrieve(
                login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_id` but received ''"):
            await async_client.bridges.logins.with_raw_response.retrieve(
                login_id="",
                bridge_id="local-whatsapp",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBeeperDesktop) -> None:
        login = await async_client.bridges.logins.list(
            "local-whatsapp",
        )
        assert_matches_type(LoginListResponse, login, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.logins.with_raw_response.list(
            "local-whatsapp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(LoginListResponse, login, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.logins.with_streaming_response.list(
            "local-whatsapp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(LoginListResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.logins.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncBeeperDesktop) -> None:
        login = await async_client.bridges.logins.remove(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
            scope="current-device",
        )
        assert_matches_type(LoginRemoveResponse, login, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.bridges.logins.with_raw_response.remove(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
            scope="current-device",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        login = await response.parse()
        assert_matches_type(LoginRemoveResponse, login, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.bridges.logins.with_streaming_response.remove(
            login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
            bridge_id="local-whatsapp",
            scope="current-device",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            login = await response.parse()
            assert_matches_type(LoginRemoveResponse, login, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.bridges.logins.with_raw_response.remove(
                login_id="ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
                bridge_id="",
                scope="current-device",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_id` but received ''"):
            await async_client.bridges.logins.with_raw_response.remove(
                login_id="",
                bridge_id="local-whatsapp",
                scope="current-device",
            )
