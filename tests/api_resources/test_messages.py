# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import (
    MessageSendResponse,
)
from beeper_desktop_api._utils import parse_datetime
from beeper_desktop_api.pagination import SyncCursorSearch, AsyncCursorSearch, SyncCursorSortKey, AsyncCursorSortKey
from beeper_desktop_api.types.shared import Message

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: BeeperDesktop) -> None:
        message = client.messages.list(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(SyncCursorSortKey[Message], message, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BeeperDesktop) -> None:
        message = client.messages.list(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            cursor="1725489123456|c29tZUltc2dQYWdl",
            direction="before",
        )
        assert_matches_type(SyncCursorSortKey[Message], message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BeeperDesktop) -> None:
        response = client.messages.with_raw_response.list(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncCursorSortKey[Message], message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BeeperDesktop) -> None:
        with client.messages.with_streaming_response.list(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncCursorSortKey[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.messages.with_raw_response.list(
                chat_id="",
            )

    @parametrize
    def test_method_search(self, client: BeeperDesktop) -> None:
        message = client.messages.search()
        assert_matches_type(SyncCursorSearch[Message], message, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: BeeperDesktop) -> None:
        message = client.messages.search(
            account_ids=[
                "whatsapp",
                "local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
                "local-instagram_ba_eRfQMmnSNy_p7Ih7HL7RduRpKFU",
            ],
            chat_ids=["!NCdzlIaMjZUmvmvyHU:beeper.com", "1231073"],
            chat_type="group",
            cursor="1725489123456|c29tZUltc2dQYWdl",
            date_after=parse_datetime("2025-08-01T00:00:00Z"),
            date_before=parse_datetime("2025-08-31T23:59:59Z"),
            direction="before",
            exclude_low_priority=True,
            include_muted=True,
            limit=20,
            media_types=["any"],
            query="dinner",
            sender="me",
        )
        assert_matches_type(SyncCursorSearch[Message], message, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: BeeperDesktop) -> None:
        response = client.messages.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncCursorSearch[Message], message, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: BeeperDesktop) -> None:
        with client.messages.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncCursorSearch[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send(self, client: BeeperDesktop) -> None:
        message = client.messages.send(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    def test_method_send_with_all_params(self, client: BeeperDesktop) -> None:
        message = client.messages.send(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reply_to_message_id="replyToMessageID",
            text="text",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    def test_raw_response_send(self, client: BeeperDesktop) -> None:
        response = client.messages.with_raw_response.send(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_send(self, client: BeeperDesktop) -> None:
        with client.messages.with_streaming_response.send(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.messages.with_raw_response.send(
                chat_id="",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncBeeperDesktop) -> None:
        message = await async_client.messages.list(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(AsyncCursorSortKey[Message], message, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        message = await async_client.messages.list(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            cursor="1725489123456|c29tZUltc2dQYWdl",
            direction="before",
        )
        assert_matches_type(AsyncCursorSortKey[Message], message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.messages.with_raw_response.list(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncCursorSortKey[Message], message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.messages.with_streaming_response.list(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncCursorSortKey[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.messages.with_raw_response.list(
                chat_id="",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncBeeperDesktop) -> None:
        message = await async_client.messages.search()
        assert_matches_type(AsyncCursorSearch[Message], message, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        message = await async_client.messages.search(
            account_ids=[
                "whatsapp",
                "local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc",
                "local-instagram_ba_eRfQMmnSNy_p7Ih7HL7RduRpKFU",
            ],
            chat_ids=["!NCdzlIaMjZUmvmvyHU:beeper.com", "1231073"],
            chat_type="group",
            cursor="1725489123456|c29tZUltc2dQYWdl",
            date_after=parse_datetime("2025-08-01T00:00:00Z"),
            date_before=parse_datetime("2025-08-31T23:59:59Z"),
            direction="before",
            exclude_low_priority=True,
            include_muted=True,
            limit=20,
            media_types=["any"],
            query="dinner",
            sender="me",
        )
        assert_matches_type(AsyncCursorSearch[Message], message, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.messages.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncCursorSearch[Message], message, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.messages.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncCursorSearch[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send(self, async_client: AsyncBeeperDesktop) -> None:
        message = await async_client.messages.send(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        message = await async_client.messages.send(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reply_to_message_id="replyToMessageID",
            text="text",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.messages.with_raw_response.send(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.messages.with_streaming_response.send(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.messages.with_raw_response.send(
                chat_id="",
            )
