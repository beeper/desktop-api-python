# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.matrix.rooms import EventRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        event = client.matrix.rooms.events.retrieve(
            event_id="$asfDuShaf7Gafaw:matrix.org",
            room_id="!636q39766251:matrix.org",
        )
        assert_matches_type(EventRetrieveResponse, event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.matrix.rooms.events.with_raw_response.retrieve(
            event_id="$asfDuShaf7Gafaw:matrix.org",
            room_id="!636q39766251:matrix.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventRetrieveResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.matrix.rooms.events.with_streaming_response.retrieve(
            event_id="$asfDuShaf7Gafaw:matrix.org",
            room_id="!636q39766251:matrix.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventRetrieveResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            client.matrix.rooms.events.with_raw_response.retrieve(
                event_id="$asfDuShaf7Gafaw:matrix.org",
                room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.matrix.rooms.events.with_raw_response.retrieve(
                event_id="",
                room_id="!636q39766251:matrix.org",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        event = await async_client.matrix.rooms.events.retrieve(
            event_id="$asfDuShaf7Gafaw:matrix.org",
            room_id="!636q39766251:matrix.org",
        )
        assert_matches_type(EventRetrieveResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.rooms.events.with_raw_response.retrieve(
            event_id="$asfDuShaf7Gafaw:matrix.org",
            room_id="!636q39766251:matrix.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventRetrieveResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.rooms.events.with_streaming_response.retrieve(
            event_id="$asfDuShaf7Gafaw:matrix.org",
            room_id="!636q39766251:matrix.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventRetrieveResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            await async_client.matrix.rooms.events.with_raw_response.retrieve(
                event_id="$asfDuShaf7Gafaw:matrix.org",
                room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.matrix.rooms.events.with_raw_response.retrieve(
                event_id="",
                room_id="!636q39766251:matrix.org",
            )
