# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.matrix import (
    RoomJoinResponse,
    RoomCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRooms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BeeperDesktop) -> None:
        room = client.matrix.rooms.create()
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: BeeperDesktop) -> None:
        room = client.matrix.rooms.create(
            creation_content={"m.federate": False},
            initial_state=[
                {
                    "content": {},
                    "type": "type",
                    "state_key": "state_key",
                }
            ],
            invite=["string"],
            invite_3pid=[
                {
                    "address": "cheeky@monkey.com",
                    "id_access_token": "abc123_OpaqueString",
                    "id_server": "matrix.org",
                    "medium": "email",
                }
            ],
            is_direct=True,
            name="The Grand Duke Pub",
            power_level_content_override={},
            preset="public_chat",
            room_alias_name="thepub",
            room_version="1",
            topic="All about happy hour",
            visibility="public",
        )
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: BeeperDesktop) -> None:
        response = client.matrix.rooms.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: BeeperDesktop) -> None:
        with client.matrix.rooms.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert_matches_type(RoomCreateResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_join(self, client: BeeperDesktop) -> None:
        room = client.matrix.rooms.join(
            room_id_or_alias="!monkeys:matrix.org",
        )
        assert_matches_type(RoomJoinResponse, room, path=["response"])

    @parametrize
    def test_method_join_with_all_params(self, client: BeeperDesktop) -> None:
        room = client.matrix.rooms.join(
            room_id_or_alias="!monkeys:matrix.org",
            via=["string"],
            reason="Looking for support",
            third_party_signed={
                "token": "random8nonce",
                "mxid": "bob",
                "sender": "alice",
                "signatures": {"example.org": {"ed25519:0": "some9signature"}},
            },
        )
        assert_matches_type(RoomJoinResponse, room, path=["response"])

    @parametrize
    def test_raw_response_join(self, client: BeeperDesktop) -> None:
        response = client.matrix.rooms.with_raw_response.join(
            room_id_or_alias="!monkeys:matrix.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert_matches_type(RoomJoinResponse, room, path=["response"])

    @parametrize
    def test_streaming_response_join(self, client: BeeperDesktop) -> None:
        with client.matrix.rooms.with_streaming_response.join(
            room_id_or_alias="!monkeys:matrix.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert_matches_type(RoomJoinResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_join(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id_or_alias` but received ''"):
            client.matrix.rooms.with_raw_response.join(
                room_id_or_alias="",
            )

    @parametrize
    def test_method_leave(self, client: BeeperDesktop) -> None:
        room = client.matrix.rooms.leave(
            room_id="!nkl290a:matrix.org",
        )
        assert_matches_type(object, room, path=["response"])

    @parametrize
    def test_method_leave_with_all_params(self, client: BeeperDesktop) -> None:
        room = client.matrix.rooms.leave(
            room_id="!nkl290a:matrix.org",
            reason="Saying farewell - thanks for the support!",
        )
        assert_matches_type(object, room, path=["response"])

    @parametrize
    def test_raw_response_leave(self, client: BeeperDesktop) -> None:
        response = client.matrix.rooms.with_raw_response.leave(
            room_id="!nkl290a:matrix.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = response.parse()
        assert_matches_type(object, room, path=["response"])

    @parametrize
    def test_streaming_response_leave(self, client: BeeperDesktop) -> None:
        with client.matrix.rooms.with_streaming_response.leave(
            room_id="!nkl290a:matrix.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = response.parse()
            assert_matches_type(object, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_leave(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            client.matrix.rooms.with_raw_response.leave(
                room_id="",
            )


class TestAsyncRooms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.rooms.create()
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.rooms.create(
            creation_content={"m.federate": False},
            initial_state=[
                {
                    "content": {},
                    "type": "type",
                    "state_key": "state_key",
                }
            ],
            invite=["string"],
            invite_3pid=[
                {
                    "address": "cheeky@monkey.com",
                    "id_access_token": "abc123_OpaqueString",
                    "id_server": "matrix.org",
                    "medium": "email",
                }
            ],
            is_direct=True,
            name="The Grand Duke Pub",
            power_level_content_override={},
            preset="public_chat",
            room_alias_name="thepub",
            room_version="1",
            topic="All about happy hour",
            visibility="public",
        )
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.rooms.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert_matches_type(RoomCreateResponse, room, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.rooms.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert_matches_type(RoomCreateResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_join(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.rooms.join(
            room_id_or_alias="!monkeys:matrix.org",
        )
        assert_matches_type(RoomJoinResponse, room, path=["response"])

    @parametrize
    async def test_method_join_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.rooms.join(
            room_id_or_alias="!monkeys:matrix.org",
            via=["string"],
            reason="Looking for support",
            third_party_signed={
                "token": "random8nonce",
                "mxid": "bob",
                "sender": "alice",
                "signatures": {"example.org": {"ed25519:0": "some9signature"}},
            },
        )
        assert_matches_type(RoomJoinResponse, room, path=["response"])

    @parametrize
    async def test_raw_response_join(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.rooms.with_raw_response.join(
            room_id_or_alias="!monkeys:matrix.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert_matches_type(RoomJoinResponse, room, path=["response"])

    @parametrize
    async def test_streaming_response_join(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.rooms.with_streaming_response.join(
            room_id_or_alias="!monkeys:matrix.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert_matches_type(RoomJoinResponse, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_join(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id_or_alias` but received ''"):
            await async_client.matrix.rooms.with_raw_response.join(
                room_id_or_alias="",
            )

    @parametrize
    async def test_method_leave(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.rooms.leave(
            room_id="!nkl290a:matrix.org",
        )
        assert_matches_type(object, room, path=["response"])

    @parametrize
    async def test_method_leave_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        room = await async_client.matrix.rooms.leave(
            room_id="!nkl290a:matrix.org",
            reason="Saying farewell - thanks for the support!",
        )
        assert_matches_type(object, room, path=["response"])

    @parametrize
    async def test_raw_response_leave(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.rooms.with_raw_response.leave(
            room_id="!nkl290a:matrix.org",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        room = await response.parse()
        assert_matches_type(object, room, path=["response"])

    @parametrize
    async def test_streaming_response_leave(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.rooms.with_streaming_response.leave(
            room_id="!nkl290a:matrix.org",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            room = await response.parse()
            assert_matches_type(object, room, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_leave(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `room_id` but received ''"):
            await async_client.matrix.rooms.with_raw_response.leave(
                room_id="",
            )
