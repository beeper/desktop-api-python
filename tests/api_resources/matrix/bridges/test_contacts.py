# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.matrix.bridges import ContactListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BeeperDesktop) -> None:
        contact = client.matrix.bridges.contacts.list(
            bridge_id="bridgeID",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BeeperDesktop) -> None:
        contact = client.matrix.bridges.contacts.list(
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.contacts.with_raw_response.list(
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.contacts.with_streaming_response.list(
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.contacts.with_raw_response.list(
                bridge_id="",
            )


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBeeperDesktop) -> None:
        contact = await async_client.matrix.bridges.contacts.list(
            bridge_id="bridgeID",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        contact = await async_client.matrix.bridges.contacts.list(
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.contacts.with_raw_response.list(
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.contacts.with_streaming_response.list(
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.contacts.with_raw_response.list(
                bridge_id="",
            )
