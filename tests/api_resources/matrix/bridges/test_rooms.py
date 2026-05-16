# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.matrix.bridges import (
    RoomCreateDmResponse,
    RoomCreateGroupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRooms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_dm(self, client: BeeperDesktop) -> None:
        room = client.matrix.bridges.rooms.create_dm(
            identifier="identifier",
            bridge_id="bridgeID",
        )
        assert_matches_type(RoomCreateDmResponse, room, path=["response"])

    @parametrize
    def test_method_create_dm_with_all_params(self, client: BeeperDesktop) -> None:
        room = client.matrix.bridges.rooms.create_dm(
            identifier="identifier",
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        assert_matches_type(RoomCreateDmResponse, room, path=["response"])

    @parametrize
    def test_raw_response_create_dm(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.rooms.with_raw_response.create_dm(
            identifier="identifier",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert_matches_type(RoomCreateDmResponse, room, path=["response"])

    @parametrize
    def test_streaming_response_create_dm(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.rooms.with_streaming_response.create_dm(
            identifier="identifier",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert_matches_type(RoomCreateDmResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_dm(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.rooms.with_raw_response.create_dm(
                identifier="identifier",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.matrix.bridges.rooms.with_raw_response.create_dm(
                identifier="",
                bridge_id="bridgeID",
            )

    @parametrize
    def test_method_create_group(self, client: BeeperDesktop) -> None:
        room = client.matrix.bridges.rooms.create_group(
            group_type="groupType",
            bridge_id="bridgeID",
        )
        assert_matches_type(RoomCreateGroupResponse, room, path=["response"])

    @parametrize
    def test_method_create_group_with_all_params(self, client: BeeperDesktop) -> None:
        room = client.matrix.bridges.rooms.create_group(
            group_type="groupType",
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            avatar={"url": "url"},
            disappear={
                "timer": 0,
                "type": "type",
            },
            name={"name": "name"},
            parent={},
            participants=["string"],
            room_id="room_id",
            topic={"topic": "topic"},
            type="channel",
            username="username",
        )
        assert_matches_type(RoomCreateGroupResponse, room, path=["response"])

    @parametrize
    def test_raw_response_create_group(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.rooms.with_raw_response.create_group(
            group_type="groupType",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert_matches_type(RoomCreateGroupResponse, room, path=["response"])

    @parametrize
    def test_streaming_response_create_group(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.rooms.with_streaming_response.create_group(
            group_type="groupType",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert_matches_type(RoomCreateGroupResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_group(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.rooms.with_raw_response.create_group(
                group_type="groupType",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_type` but received ''"):
            client.matrix.bridges.rooms.with_raw_response.create_group(
                group_type="",
                bridge_id="bridgeID",
            )


class TestAsyncRooms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_dm(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.bridges.rooms.create_dm(
            identifier="identifier",
            bridge_id="bridgeID",
        )
        assert_matches_type(RoomCreateDmResponse, room, path=["response"])

    @parametrize
    async def test_method_create_dm_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.bridges.rooms.create_dm(
            identifier="identifier",
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        assert_matches_type(RoomCreateDmResponse, room, path=["response"])

    @parametrize
    async def test_raw_response_create_dm(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.rooms.with_raw_response.create_dm(
            identifier="identifier",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert_matches_type(RoomCreateDmResponse, room, path=["response"])

    @parametrize
    async def test_streaming_response_create_dm(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.rooms.with_streaming_response.create_dm(
            identifier="identifier",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert_matches_type(RoomCreateDmResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_dm(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.rooms.with_raw_response.create_dm(
                identifier="identifier",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.matrix.bridges.rooms.with_raw_response.create_dm(
                identifier="",
                bridge_id="bridgeID",
            )

    @parametrize
    async def test_method_create_group(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.bridges.rooms.create_group(
            group_type="groupType",
            bridge_id="bridgeID",
        )
        assert_matches_type(RoomCreateGroupResponse, room, path=["response"])

    @parametrize
    async def test_method_create_group_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.bridges.rooms.create_group(
            group_type="groupType",
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            avatar={"url": "url"},
            disappear={
                "timer": 0,
                "type": "type",
            },
            name={"name": "name"},
            parent={},
            participants=["string"],
            room_id="room_id",
            topic={"topic": "topic"},
            type="channel",
            username="username",
        )
        assert_matches_type(RoomCreateGroupResponse, room, path=["response"])

    @parametrize
    async def test_raw_response_create_group(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.rooms.with_raw_response.create_group(
            group_type="groupType",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert_matches_type(RoomCreateGroupResponse, room, path=["response"])

    @parametrize
    async def test_streaming_response_create_group(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.rooms.with_streaming_response.create_group(
            group_type="groupType",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert_matches_type(RoomCreateGroupResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_group(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.rooms.with_raw_response.create_group(
                group_type="groupType",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_type` but received ''"):
            await async_client.matrix.bridges.rooms.with_raw_response.create_group(
                group_type="",
                bridge_id="bridgeID",
            )
