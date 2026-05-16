# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.matrix import UserRetrieveProfileResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_profile(self, client: BeeperDesktop) -> None:
        user = client.matrix.users.retrieve_profile(
            "@alice:example.com",
        )
        assert_matches_type(UserRetrieveProfileResponse, user, path=["response"])

    @parametrize
    def test_raw_response_retrieve_profile(self, client: BeeperDesktop) -> None:
        response = client.matrix.users.with_raw_response.retrieve_profile(
            "@alice:example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveProfileResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_profile(self, client: BeeperDesktop) -> None:
        with client.matrix.users.with_streaming_response.retrieve_profile(
            "@alice:example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveProfileResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_profile(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.matrix.users.with_raw_response.retrieve_profile(
                "",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_profile(self, async_client: AsyncBeeperDesktop) -> None:
        user = await async_client.matrix.users.retrieve_profile(
            "@alice:example.com",
        )
        assert_matches_type(UserRetrieveProfileResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_profile(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.users.with_raw_response.retrieve_profile(
            "@alice:example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveProfileResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_profile(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.users.with_streaming_response.retrieve_profile(
            "@alice:example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveProfileResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_profile(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.matrix.users.with_raw_response.retrieve_profile(
                "",
            )
