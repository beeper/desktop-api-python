# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.chats.messages import ReactionAddResponse, ReactionDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: BeeperDesktop) -> None:
        reaction = client.chats.messages.reactions.delete(
            reaction_key="x",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        )
        assert_matches_type(ReactionDeleteResponse, reaction, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: BeeperDesktop) -> None:
        response = client.chats.messages.reactions.with_raw_response.delete(
            reaction_key="x",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reaction = response.parse()
        assert_matches_type(ReactionDeleteResponse, reaction, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: BeeperDesktop) -> None:
        with client.chats.messages.reactions.with_streaming_response.delete(
            reaction_key="x",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reaction = response.parse()
            assert_matches_type(ReactionDeleteResponse, reaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.reactions.with_raw_response.delete(
                reaction_key="x",
                chat_id="",
                message_id="1343993",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.chats.messages.reactions.with_raw_response.delete(
                reaction_key="x",
                chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
                message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reaction_key` but received ''"):
            client.chats.messages.reactions.with_raw_response.delete(
                reaction_key="",
                chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
                message_id="1343993",
            )

    @parametrize
    def test_method_add(self, client: BeeperDesktop) -> None:
        reaction = client.chats.messages.reactions.add(
            message_id="1343993",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reaction_key="x",
        )
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: BeeperDesktop) -> None:
        reaction = client.chats.messages.reactions.add(
            message_id="1343993",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reaction_key="x",
            transaction_id="transactionID",
        )
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: BeeperDesktop) -> None:
        response = client.chats.messages.reactions.with_raw_response.add(
            message_id="1343993",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reaction_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reaction = response.parse()
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: BeeperDesktop) -> None:
        with client.chats.messages.reactions.with_streaming_response.add(
            message_id="1343993",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reaction_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reaction = response.parse()
            assert_matches_type(ReactionAddResponse, reaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.reactions.with_raw_response.add(
                message_id="1343993",
                chat_id="",
                reaction_key="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.chats.messages.reactions.with_raw_response.add(
                message_id="",
                chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
                reaction_key="x",
            )


class TestAsyncReactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncBeeperDesktop) -> None:
        reaction = await async_client.chats.messages.reactions.delete(
            reaction_key="x",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        )
        assert_matches_type(ReactionDeleteResponse, reaction, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.messages.reactions.with_raw_response.delete(
            reaction_key="x",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reaction = await response.parse()
        assert_matches_type(ReactionDeleteResponse, reaction, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.messages.reactions.with_streaming_response.delete(
            reaction_key="x",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            message_id="1343993",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reaction = await response.parse()
            assert_matches_type(ReactionDeleteResponse, reaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.reactions.with_raw_response.delete(
                reaction_key="x",
                chat_id="",
                message_id="1343993",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.chats.messages.reactions.with_raw_response.delete(
                reaction_key="x",
                chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
                message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reaction_key` but received ''"):
            await async_client.chats.messages.reactions.with_raw_response.delete(
                reaction_key="",
                chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
                message_id="1343993",
            )

    @parametrize
    async def test_method_add(self, async_client: AsyncBeeperDesktop) -> None:
        reaction = await async_client.chats.messages.reactions.add(
            message_id="1343993",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reaction_key="x",
        )
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        reaction = await async_client.chats.messages.reactions.add(
            message_id="1343993",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reaction_key="x",
            transaction_id="transactionID",
        )
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.chats.messages.reactions.with_raw_response.add(
            message_id="1343993",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reaction_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reaction = await response.parse()
        assert_matches_type(ReactionAddResponse, reaction, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.chats.messages.reactions.with_streaming_response.add(
            message_id="1343993",
            chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
            reaction_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reaction = await response.parse()
            assert_matches_type(ReactionAddResponse, reaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.reactions.with_raw_response.add(
                message_id="1343993",
                chat_id="",
                reaction_key="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.chats.messages.reactions.with_raw_response.add(
                message_id="",
                chat_id="!NCdzlIaMjZUmvmvyHU:beeper.com",
                reaction_key="x",
            )
