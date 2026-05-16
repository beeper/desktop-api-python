# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.matrix.rooms import StateListResponse, StateRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestState:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        state = client.matrix.rooms.state.retrieve(
            state_key="state_key",
            room_id="!636q39766251:example.com",
            event_type="m.room.name",
        )
        assert_matches_type(StateRetrieveResponse, state, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: BeeperDesktop) -> None:
        state = client.matrix.rooms.state.retrieve(
            state_key="state_key",
            room_id="!636q39766251:example.com",
            event_type="m.room.name",
            format="content",
        )
        assert_matches_type(StateRetrieveResponse, state, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.matrix.rooms.state.with_raw_response.retrieve(
            state_key="state_key",
            room_id="!636q39766251:example.com",
            event_type="m.room.name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        state = response.parse()
        assert_matches_type(StateRetrieveResponse, state, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.matrix.rooms.state.with_streaming_response.retrieve(
            state_key="state_key",
            room_id="!636q39766251:example.com",
            event_type="m.room.name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            state = response.parse()
            assert_matches_type(StateRetrieveResponse, state, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            client.matrix.rooms.state.with_raw_response.retrieve(
                state_key="state_key",
                room_id="",
                event_type="m.room.name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_type` but received ''"):
            client.matrix.rooms.state.with_raw_response.retrieve(
                state_key="state_key",
                room_id="!636q39766251:example.com",
                event_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `state_key` but received ''"):
            client.matrix.rooms.state.with_raw_response.retrieve(
                state_key="",
                room_id="!636q39766251:example.com",
                event_type="m.room.name",
            )

    @parametrize
    def test_method_list(self, client: BeeperDesktop) -> None:
        state = client.matrix.rooms.state.list(
            "!636q39766251:example.com",
        )
        assert_matches_type(StateListResponse, state, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BeeperDesktop) -> None:
        response = client.matrix.rooms.state.with_raw_response.list(
            "!636q39766251:example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        state = response.parse()
        assert_matches_type(StateListResponse, state, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BeeperDesktop) -> None:
        with client.matrix.rooms.state.with_streaming_response.list(
            "!636q39766251:example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            state = response.parse()
            assert_matches_type(StateListResponse, state, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            client.matrix.rooms.state.with_raw_response.list(
                "",
            )


class TestAsyncState:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        state = await async_client.matrix.rooms.state.retrieve(
            state_key="state_key",
            room_id="!636q39766251:example.com",
            event_type="m.room.name",
        )
        assert_matches_type(StateRetrieveResponse, state, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        state = await async_client.matrix.rooms.state.retrieve(
            state_key="state_key",
            room_id="!636q39766251:example.com",
            event_type="m.room.name",
            format="content",
        )
        assert_matches_type(StateRetrieveResponse, state, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.rooms.state.with_raw_response.retrieve(
            state_key="state_key",
            room_id="!636q39766251:example.com",
            event_type="m.room.name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        state = await response.parse()
        assert_matches_type(StateRetrieveResponse, state, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.rooms.state.with_streaming_response.retrieve(
            state_key="state_key",
            room_id="!636q39766251:example.com",
            event_type="m.room.name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            state = await response.parse()
            assert_matches_type(StateRetrieveResponse, state, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            await async_client.matrix.rooms.state.with_raw_response.retrieve(
                state_key="state_key",
                room_id="",
                event_type="m.room.name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_type` but received ''"):
            await async_client.matrix.rooms.state.with_raw_response.retrieve(
                state_key="state_key",
                room_id="!636q39766251:example.com",
                event_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `state_key` but received ''"):
            await async_client.matrix.rooms.state.with_raw_response.retrieve(
                state_key="",
                room_id="!636q39766251:example.com",
                event_type="m.room.name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBeeperDesktop) -> None:
        state = await async_client.matrix.rooms.state.list(
            "!636q39766251:example.com",
        )
        assert_matches_type(StateListResponse, state, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.rooms.state.with_raw_response.list(
            "!636q39766251:example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        state = await response.parse()
        assert_matches_type(StateListResponse, state, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.rooms.state.with_streaming_response.list(
            "!636q39766251:example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            state = await response.parse()
            assert_matches_type(StateListResponse, state, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            await async_client.matrix.rooms.state.with_raw_response.list(
                "",
            )
