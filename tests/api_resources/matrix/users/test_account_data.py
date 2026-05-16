# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        account_data = client.matrix.users.account_data.retrieve(
            type="org.example.custom.config",
            user_id="@alice:example.com",
        )
        assert_matches_type(object, account_data, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.matrix.users.account_data.with_raw_response.retrieve(
            type="org.example.custom.config",
            user_id="@alice:example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_data = response.parse()
        assert_matches_type(object, account_data, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.matrix.users.account_data.with_streaming_response.retrieve(
            type="org.example.custom.config",
            user_id="@alice:example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_data = response.parse()
            assert_matches_type(object, account_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.matrix.users.account_data.with_raw_response.retrieve(
                type="org.example.custom.config",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.matrix.users.account_data.with_raw_response.retrieve(
                type="",
                user_id="@alice:example.com",
            )

    @parametrize
    def test_method_update(self, client: BeeperDesktop) -> None:
        account_data = client.matrix.users.account_data.update(
            type="org.example.custom.config",
            user_id="@alice:example.com",
            body={"custom_account_data_key": "custom_config_value"},
        )
        assert_matches_type(object, account_data, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: BeeperDesktop) -> None:
        response = client.matrix.users.account_data.with_raw_response.update(
            type="org.example.custom.config",
            user_id="@alice:example.com",
            body={"custom_account_data_key": "custom_config_value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_data = response.parse()
        assert_matches_type(object, account_data, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: BeeperDesktop) -> None:
        with client.matrix.users.account_data.with_streaming_response.update(
            type="org.example.custom.config",
            user_id="@alice:example.com",
            body={"custom_account_data_key": "custom_config_value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_data = response.parse()
            assert_matches_type(object, account_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.matrix.users.account_data.with_raw_response.update(
                type="org.example.custom.config",
                user_id="",
                body={"custom_account_data_key": "custom_config_value"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.matrix.users.account_data.with_raw_response.update(
                type="",
                user_id="@alice:example.com",
                body={"custom_account_data_key": "custom_config_value"},
            )


class TestAsyncAccountData:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        account_data = await async_client.matrix.users.account_data.retrieve(
            type="org.example.custom.config",
            user_id="@alice:example.com",
        )
        assert_matches_type(object, account_data, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.users.account_data.with_raw_response.retrieve(
            type="org.example.custom.config",
            user_id="@alice:example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_data = await response.parse()
        assert_matches_type(object, account_data, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.users.account_data.with_streaming_response.retrieve(
            type="org.example.custom.config",
            user_id="@alice:example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_data = await response.parse()
            assert_matches_type(object, account_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.matrix.users.account_data.with_raw_response.retrieve(
                type="org.example.custom.config",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.matrix.users.account_data.with_raw_response.retrieve(
                type="",
                user_id="@alice:example.com",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBeeperDesktop) -> None:
        account_data = await async_client.matrix.users.account_data.update(
            type="org.example.custom.config",
            user_id="@alice:example.com",
            body={"custom_account_data_key": "custom_config_value"},
        )
        assert_matches_type(object, account_data, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.users.account_data.with_raw_response.update(
            type="org.example.custom.config",
            user_id="@alice:example.com",
            body={"custom_account_data_key": "custom_config_value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_data = await response.parse()
        assert_matches_type(object, account_data, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.users.account_data.with_streaming_response.update(
            type="org.example.custom.config",
            user_id="@alice:example.com",
            body={"custom_account_data_key": "custom_config_value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_data = await response.parse()
            assert_matches_type(object, account_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.matrix.users.account_data.with_raw_response.update(
                type="org.example.custom.config",
                user_id="",
                body={"custom_account_data_key": "custom_config_value"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.matrix.users.account_data.with_raw_response.update(
                type="",
                user_id="@alice:example.com",
                body={"custom_account_data_key": "custom_config_value"},
            )
