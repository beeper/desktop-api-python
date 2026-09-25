# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import AccountListResponse, AccountRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        account = client.accounts.retrieve(
            "accountID",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.accounts.with_raw_response.retrieve(
            "accountID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.accounts.with_streaming_response.retrieve(
            "accountID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: BeeperDesktop) -> None:
        account = client.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BeeperDesktop) -> None:
        response = client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BeeperDesktop) -> None:
        with client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        account = await async_client.accounts.retrieve(
            "accountID",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            "accountID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            "accountID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBeeperDesktop) -> None:
        account = await async_client.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
