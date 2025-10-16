# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReminders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BeeperDesktop) -> None:
        reminder = client.chats.reminders.create(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reminder={"remind_at_ms": 0},
        )
        assert reminder is None

    @parametrize
    def test_method_create_with_all_params(self, client: BeeperDesktop) -> None:
        reminder = client.chats.reminders.create(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reminder={
                "remind_at_ms": 0,
                "dismiss_on_incoming_message": True,
            },
        )
        assert reminder is None

    @parametrize
    def test_raw_response_create(self, client: BeeperDesktop) -> None:
        response = client.chats.reminders.with_raw_response.create(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reminder={"remind_at_ms": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reminder = response.parse()
        assert reminder is None

    @parametrize
    def test_streaming_response_create(self, client: BeeperDesktop) -> None:
        with client.chats.reminders.with_streaming_response.create(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reminder={"remind_at_ms": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reminder = response.parse()
            assert reminder is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.reminders.with_raw_response.create(
                chat_id="",
                reminder={"remind_at_ms": 0},
            )

    @parametrize
    def test_method_delete(self, client: BeeperDesktop) -> None:
        reminder = client.chats.reminders.delete(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert reminder is None

    @parametrize
    def test_raw_response_delete(self, client: BeeperDesktop) -> None:
        response = client.chats.reminders.with_raw_response.delete(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reminder = response.parse()
        assert reminder is None

    @parametrize
    def test_streaming_response_delete(self, client: BeeperDesktop) -> None:
        with client.chats.reminders.with_streaming_response.delete(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reminder = response.parse()
            assert reminder is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.reminders.with_raw_response.delete(
                "",
            )


class TestAsyncReminders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBeeperDesktop) -> None:
        reminder = await async_client.chats.reminders.create(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reminder={"remind_at_ms": 0},
        )
        assert reminder is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        reminder = await async_client.chats.reminders.create(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reminder={
                "remind_at_ms": 0,
                "dismiss_on_incoming_message": True,
            },
        )
        assert reminder is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.reminders.with_raw_response.create(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reminder={"remind_at_ms": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reminder = await response.parse()
        assert reminder is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.reminders.with_streaming_response.create(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reminder={"remind_at_ms": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reminder = await response.parse()
            assert reminder is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.reminders.with_raw_response.create(
                chat_id="",
                reminder={"remind_at_ms": 0},
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncBeeperDesktop) -> None:
        reminder = await async_client.chats.reminders.delete(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert reminder is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.reminders.with_raw_response.delete(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reminder = await response.parse()
        assert reminder is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.reminders.with_streaming_response.delete(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reminder = await response.parse()
            assert reminder is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.reminders.with_raw_response.delete(
                "",
            )
