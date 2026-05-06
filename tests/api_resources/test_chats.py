# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types import (
    Chat,
    ChatListResponse,
    ChatStartResponse,
    ChatCreateResponse,
)
from beeper_desktop_api._utils import parse_datetime
from beeper_desktop_api.pagination import SyncCursorSearch, AsyncCursorSearch, SyncCursorNoLimit, AsyncCursorNoLimit

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: BeeperDesktop) -> None:
        chat = client.chats.create(
            account_id="accountID",
            participant_ids=["string"],
            type="single",
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: BeeperDesktop) -> None:
        chat = client.chats.create(
            account_id="accountID",
            participant_ids=["string"],
            type="single",
            message_text="messageText",
            title="title",
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.create(
            account_id="accountID",
            participant_ids=["string"],
            type="single",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.create(
            account_id="accountID",
            participant_ids=["string"],
            type="single",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: BeeperDesktop) -> None:
        chat = client.chats.retrieve(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: BeeperDesktop) -> None:
        chat = client.chats.retrieve(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            max_participant_count=100,
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.retrieve(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.retrieve(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.retrieve(
                chat_id="",
            )

    @parametrize
    def test_method_update(self, client: BeeperDesktop) -> None:
        chat = client.chats.update(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: BeeperDesktop) -> None:
        chat = client.chats.update(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            description="description",
            draft={
                "text": "text",
                "attachments": {
                    "foo": {
                        "upload_id": "uploadID",
                        "id": "id",
                        "duration": 0,
                        "file_name": "fileName",
                        "mime_type": "mimeType",
                        "size": {
                            "height": 0,
                            "width": 0,
                        },
                        "type": "image",
                    }
                },
            },
            img_url="imgURL",
            is_archived=True,
            is_low_priority=True,
            is_muted=True,
            is_pinned=True,
            message_expiry_seconds=0,
            title="title",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.update(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.update(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.update(
                chat_id="",
            )

    @parametrize
    def test_method_list(self, client: BeeperDesktop) -> None:
        chat = client.chats.list()
        assert_matches_type(SyncCursorNoLimit[ChatListResponse], chat, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: BeeperDesktop) -> None:
        chat = client.chats.list(
            account_ids=["matrix", "discordgo", "local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc"],
            cursor="1725489123456|c29tZUltc2dQYWdl",
            direction="before",
        )
        assert_matches_type(SyncCursorNoLimit[ChatListResponse], chat, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(SyncCursorNoLimit[ChatListResponse], chat, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(SyncCursorNoLimit[ChatListResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: BeeperDesktop) -> None:
        chat = client.chats.archive(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert chat is None

    @parametrize
    def test_method_archive_with_all_params(self, client: BeeperDesktop) -> None:
        chat = client.chats.archive(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            archived=True,
        )
        assert chat is None

    @parametrize
    def test_raw_response_archive(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.archive(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @parametrize
    def test_streaming_response_archive(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.archive(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.archive(
                chat_id="",
            )

    @parametrize
    def test_method_mark_read(self, client: BeeperDesktop) -> None:
        chat = client.chats.mark_read(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_method_mark_read_with_all_params(self, client: BeeperDesktop) -> None:
        chat = client.chats.mark_read(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_mark_read(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.mark_read(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_mark_read(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.mark_read(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_mark_read(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.mark_read(
                chat_id="",
            )

    @parametrize
    def test_method_mark_unread(self, client: BeeperDesktop) -> None:
        chat = client.chats.mark_unread(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_method_mark_unread_with_all_params(self, client: BeeperDesktop) -> None:
        chat = client.chats.mark_unread(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_mark_unread(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.mark_unread(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_mark_unread(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.mark_unread(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_mark_unread(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.mark_unread(
                chat_id="",
            )

    @parametrize
    def test_method_notify_anyway(self, client: BeeperDesktop) -> None:
        chat = client.chats.notify_anyway(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_notify_anyway(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.notify_anyway(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_notify_anyway(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.notify_anyway(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_notify_anyway(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.with_raw_response.notify_anyway(
                "",
            )

    @parametrize
    def test_method_search(self, client: BeeperDesktop) -> None:
        chat = client.chats.search()
        assert_matches_type(SyncCursorSearch[Chat], chat, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: BeeperDesktop) -> None:
        chat = client.chats.search(
            account_ids=["matrix", "discordgo", "local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc"],
            cursor="1725489123456|c29tZUltc2dQYWdl",
            direction="before",
            inbox="primary",
            include_muted=True,
            last_activity_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_activity_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            query="x",
            scope="titles",
            type="single",
            unread_only=True,
        )
        assert_matches_type(SyncCursorSearch[Chat], chat, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(SyncCursorSearch[Chat], chat, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(SyncCursorSearch[Chat], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: BeeperDesktop) -> None:
        chat = client.chats.start(
            account_id="accountID",
            user={},
        )
        assert_matches_type(ChatStartResponse, chat, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: BeeperDesktop) -> None:
        chat = client.chats.start(
            account_id="accountID",
            user={
                "id": "id",
                "email": "email",
                "full_name": "fullName",
                "phone_number": "phoneNumber",
                "username": "username",
            },
            allow_invite=True,
            message_text="messageText",
        )
        assert_matches_type(ChatStartResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: BeeperDesktop) -> None:
        response = client.chats.with_raw_response.start(
            account_id="accountID",
            user={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatStartResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: BeeperDesktop) -> None:
        with client.chats.with_streaming_response.start(
            account_id="accountID",
            user={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatStartResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.create(
            account_id="accountID",
            participant_ids=["string"],
            type="single",
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.create(
            account_id="accountID",
            participant_ids=["string"],
            type="single",
            message_text="messageText",
            title="title",
        )
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.create(
            account_id="accountID",
            participant_ids=["string"],
            type="single",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.create(
            account_id="accountID",
            participant_ids=["string"],
            type="single",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.retrieve(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.retrieve(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            max_participant_count=100,
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.retrieve(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.retrieve(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.retrieve(
                chat_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.update(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.update(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            description="description",
            draft={
                "text": "text",
                "attachments": {
                    "foo": {
                        "upload_id": "uploadID",
                        "id": "id",
                        "duration": 0,
                        "file_name": "fileName",
                        "mime_type": "mimeType",
                        "size": {
                            "height": 0,
                            "width": 0,
                        },
                        "type": "image",
                    }
                },
            },
            img_url="imgURL",
            is_archived=True,
            is_low_priority=True,
            is_muted=True,
            is_pinned=True,
            message_expiry_seconds=0,
            title="title",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.update(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.update(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.update(
                chat_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.list()
        assert_matches_type(AsyncCursorNoLimit[ChatListResponse], chat, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.list(
            account_ids=["matrix", "discordgo", "local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc"],
            cursor="1725489123456|c29tZUltc2dQYWdl",
            direction="before",
        )
        assert_matches_type(AsyncCursorNoLimit[ChatListResponse], chat, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(AsyncCursorNoLimit[ChatListResponse], chat, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(AsyncCursorNoLimit[ChatListResponse], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.archive(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert chat is None

    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.archive(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            archived=True,
        )
        assert chat is None

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.archive(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.archive(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.archive(
                chat_id="",
            )

    @parametrize
    async def test_method_mark_read(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.mark_read(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_method_mark_read_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.mark_read(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_mark_read(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.mark_read(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_mark_read(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.mark_read(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_mark_read(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.mark_read(
                chat_id="",
            )

    @parametrize
    async def test_method_mark_unread(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.mark_unread(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_method_mark_unread_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.mark_unread(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_mark_unread(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.mark_unread(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_mark_unread(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.mark_unread(
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_mark_unread(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.mark_unread(
                chat_id="",
            )

    @parametrize
    async def test_method_notify_anyway(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.notify_anyway(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_notify_anyway(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.notify_anyway(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_notify_anyway(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.notify_anyway(
            "!NCdzlIaMjZUmvmvyHU:beeper.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_notify_anyway(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.with_raw_response.notify_anyway(
                "",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.search()
        assert_matches_type(AsyncCursorSearch[Chat], chat, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.search(
            account_ids=["matrix", "discordgo", "local-whatsapp_ba_EvYDBBsZbRQAy3UOSWqG0LuTVkc"],
            cursor="1725489123456|c29tZUltc2dQYWdl",
            direction="before",
            inbox="primary",
            include_muted=True,
            last_activity_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_activity_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            query="x",
            scope="titles",
            type="single",
            unread_only=True,
        )
        assert_matches_type(AsyncCursorSearch[Chat], chat, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(AsyncCursorSearch[Chat], chat, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(AsyncCursorSearch[Chat], chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.start(
            account_id="accountID",
            user={},
        )
        assert_matches_type(ChatStartResponse, chat, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        chat = await async_client.chats.start(
            account_id="accountID",
            user={
                "id": "id",
                "email": "email",
                "full_name": "fullName",
                "phone_number": "phoneNumber",
                "username": "username",
            },
            allow_invite=True,
            message_text="messageText",
        )
        assert_matches_type(ChatStartResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.with_raw_response.start(
            account_id="accountID",
            user={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatStartResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.with_streaming_response.start(
            account_id="accountID",
            user={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatStartResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
