# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from beeper_desktop_api import BeeperDesktop, AsyncBeeperDesktop
from beeper_desktop_api.types.matrix.bridges import (
    AuthWhoamiResponse,
    AuthListFlowsResponse,
    AuthListLoginsResponse,
    AuthStartLoginResponse,
    AuthWaitForStepResponse,
    AuthSubmitCookiesResponse,
    AuthSubmitUserInputResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_flows(self, client: BeeperDesktop) -> None:
        auth = client.matrix.bridges.auth.list_flows(
            "bridgeID",
        )
        assert_matches_type(AuthListFlowsResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_list_flows(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.auth.with_raw_response.list_flows(
            "bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthListFlowsResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_list_flows(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.auth.with_streaming_response.list_flows(
            "bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthListFlowsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_flows(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.list_flows(
                "",
            )

    @parametrize
    def test_method_list_logins(self, client: BeeperDesktop) -> None:
        auth = client.matrix.bridges.auth.list_logins(
            "bridgeID",
        )
        assert_matches_type(AuthListLoginsResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_list_logins(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.auth.with_raw_response.list_logins(
            "bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthListLoginsResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_list_logins(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.auth.with_streaming_response.list_logins(
            "bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthListLoginsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_logins(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.list_logins(
                "",
            )

    @parametrize
    def test_method_logout(self, client: BeeperDesktop) -> None:
        auth = client.matrix.bridges.auth.logout(
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            bridge_id="bridgeID",
        )
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    def test_raw_response_logout(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.auth.with_raw_response.logout(
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    def test_streaming_response_logout(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.auth.with_streaming_response.logout(
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_logout(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.logout(
                login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.logout(
                login_id="",
                bridge_id="bridgeID",
            )

    @parametrize
    def test_method_start_login(self, client: BeeperDesktop) -> None:
        auth = client.matrix.bridges.auth.start_login(
            flow_id="qr",
            bridge_id="bridgeID",
        )
        assert_matches_type(AuthStartLoginResponse, auth, path=["response"])

    @parametrize
    def test_method_start_login_with_all_params(self, client: BeeperDesktop) -> None:
        auth = client.matrix.bridges.auth.start_login(
            flow_id="qr",
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        assert_matches_type(AuthStartLoginResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_start_login(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.auth.with_raw_response.start_login(
            flow_id="qr",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthStartLoginResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_start_login(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.auth.with_streaming_response.start_login(
            flow_id="qr",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthStartLoginResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_start_login(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.start_login(
                flow_id="qr",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.start_login(
                flow_id="",
                bridge_id="bridgeID",
            )

    @parametrize
    def test_method_submit_cookies(self, client: BeeperDesktop) -> None:
        auth = client.matrix.bridges.auth.submit_cookies(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        )
        assert_matches_type(AuthSubmitCookiesResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_submit_cookies(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.auth.with_raw_response.submit_cookies(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSubmitCookiesResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_submit_cookies(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.auth.with_streaming_response.submit_cookies(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSubmitCookiesResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit_cookies(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.submit_cookies(
                step_id="stepID",
                bridge_id="",
                login_process_id="loginProcessID",
                body={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_process_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.submit_cookies(
                step_id="stepID",
                bridge_id="bridgeID",
                login_process_id="",
                body={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.submit_cookies(
                step_id="",
                bridge_id="bridgeID",
                login_process_id="loginProcessID",
                body={"foo": "string"},
            )

    @parametrize
    def test_method_submit_user_input(self, client: BeeperDesktop) -> None:
        auth = client.matrix.bridges.auth.submit_user_input(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        )
        assert_matches_type(AuthSubmitUserInputResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_submit_user_input(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.auth.with_raw_response.submit_user_input(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSubmitUserInputResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_submit_user_input(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.auth.with_streaming_response.submit_user_input(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSubmitUserInputResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit_user_input(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.submit_user_input(
                step_id="stepID",
                bridge_id="",
                login_process_id="loginProcessID",
                body={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_process_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.submit_user_input(
                step_id="stepID",
                bridge_id="bridgeID",
                login_process_id="",
                body={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.submit_user_input(
                step_id="",
                bridge_id="bridgeID",
                login_process_id="loginProcessID",
                body={"foo": "string"},
            )

    @parametrize
    def test_method_wait_for_step(self, client: BeeperDesktop) -> None:
        auth = client.matrix.bridges.auth.wait_for_step(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
        )
        assert_matches_type(AuthWaitForStepResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_wait_for_step(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.auth.with_raw_response.wait_for_step(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthWaitForStepResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_wait_for_step(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.auth.with_streaming_response.wait_for_step(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthWaitForStepResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_wait_for_step(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.wait_for_step(
                step_id="stepID",
                bridge_id="",
                login_process_id="loginProcessID",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_process_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.wait_for_step(
                step_id="stepID",
                bridge_id="bridgeID",
                login_process_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.wait_for_step(
                step_id="",
                bridge_id="bridgeID",
                login_process_id="loginProcessID",
            )

    @parametrize
    def test_method_whoami(self, client: BeeperDesktop) -> None:
        auth = client.matrix.bridges.auth.whoami(
            "bridgeID",
        )
        assert_matches_type(AuthWhoamiResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_whoami(self, client: BeeperDesktop) -> None:
        response = client.matrix.bridges.auth.with_raw_response.whoami(
            "bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthWhoamiResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_whoami(self, client: BeeperDesktop) -> None:
        with client.matrix.bridges.auth.with_streaming_response.whoami(
            "bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthWhoamiResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_whoami(self, client: BeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            client.matrix.bridges.auth.with_raw_response.whoami(
                "",
            )


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_flows(self, async_client: AsyncBeeperDesktop) -> None:
        auth = await async_client.matrix.bridges.auth.list_flows(
            "bridgeID",
        )
        assert_matches_type(AuthListFlowsResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_list_flows(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.auth.with_raw_response.list_flows(
            "bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthListFlowsResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_list_flows(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.auth.with_streaming_response.list_flows(
            "bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthListFlowsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_flows(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.list_flows(
                "",
            )

    @parametrize
    async def test_method_list_logins(self, async_client: AsyncBeeperDesktop) -> None:
        auth = await async_client.matrix.bridges.auth.list_logins(
            "bridgeID",
        )
        assert_matches_type(AuthListLoginsResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_list_logins(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.auth.with_raw_response.list_logins(
            "bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthListLoginsResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_list_logins(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.auth.with_streaming_response.list_logins(
            "bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthListLoginsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_logins(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.list_logins(
                "",
            )

    @parametrize
    async def test_method_logout(self, async_client: AsyncBeeperDesktop) -> None:
        auth = await async_client.matrix.bridges.auth.logout(
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            bridge_id="bridgeID",
        )
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.auth.with_raw_response.logout(
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.auth.with_streaming_response.logout(
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_logout(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.logout(
                login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.logout(
                login_id="",
                bridge_id="bridgeID",
            )

    @parametrize
    async def test_method_start_login(self, async_client: AsyncBeeperDesktop) -> None:
        auth = await async_client.matrix.bridges.auth.start_login(
            flow_id="qr",
            bridge_id="bridgeID",
        )
        assert_matches_type(AuthStartLoginResponse, auth, path=["response"])

    @parametrize
    async def test_method_start_login_with_all_params(self, async_client: AsyncBeeperDesktop) -> None:
        auth = await async_client.matrix.bridges.auth.start_login(
            flow_id="qr",
            bridge_id="bridgeID",
            login_id="bcc68892-b180-414f-9516-b4aadf7d0496",
        )
        assert_matches_type(AuthStartLoginResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_start_login(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.auth.with_raw_response.start_login(
            flow_id="qr",
            bridge_id="bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthStartLoginResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_start_login(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.auth.with_streaming_response.start_login(
            flow_id="qr",
            bridge_id="bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthStartLoginResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_start_login(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.start_login(
                flow_id="qr",
                bridge_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.start_login(
                flow_id="",
                bridge_id="bridgeID",
            )

    @parametrize
    async def test_method_submit_cookies(self, async_client: AsyncBeeperDesktop) -> None:
        auth = await async_client.matrix.bridges.auth.submit_cookies(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        )
        assert_matches_type(AuthSubmitCookiesResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_submit_cookies(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.auth.with_raw_response.submit_cookies(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSubmitCookiesResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_submit_cookies(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.auth.with_streaming_response.submit_cookies(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSubmitCookiesResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit_cookies(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.submit_cookies(
                step_id="stepID",
                bridge_id="",
                login_process_id="loginProcessID",
                body={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_process_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.submit_cookies(
                step_id="stepID",
                bridge_id="bridgeID",
                login_process_id="",
                body={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.submit_cookies(
                step_id="",
                bridge_id="bridgeID",
                login_process_id="loginProcessID",
                body={"foo": "string"},
            )

    @parametrize
    async def test_method_submit_user_input(self, async_client: AsyncBeeperDesktop) -> None:
        auth = await async_client.matrix.bridges.auth.submit_user_input(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        )
        assert_matches_type(AuthSubmitUserInputResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_submit_user_input(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.auth.with_raw_response.submit_user_input(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSubmitUserInputResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_submit_user_input(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.auth.with_streaming_response.submit_user_input(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
            body={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSubmitUserInputResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit_user_input(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.submit_user_input(
                step_id="stepID",
                bridge_id="",
                login_process_id="loginProcessID",
                body={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_process_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.submit_user_input(
                step_id="stepID",
                bridge_id="bridgeID",
                login_process_id="",
                body={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.submit_user_input(
                step_id="",
                bridge_id="bridgeID",
                login_process_id="loginProcessID",
                body={"foo": "string"},
            )

    @parametrize
    async def test_method_wait_for_step(self, async_client: AsyncBeeperDesktop) -> None:
        auth = await async_client.matrix.bridges.auth.wait_for_step(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
        )
        assert_matches_type(AuthWaitForStepResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_wait_for_step(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.auth.with_raw_response.wait_for_step(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthWaitForStepResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_wait_for_step(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.auth.with_streaming_response.wait_for_step(
            step_id="stepID",
            bridge_id="bridgeID",
            login_process_id="loginProcessID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthWaitForStepResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_wait_for_step(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.wait_for_step(
                step_id="stepID",
                bridge_id="",
                login_process_id="loginProcessID",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `login_process_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.wait_for_step(
                step_id="stepID",
                bridge_id="bridgeID",
                login_process_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.wait_for_step(
                step_id="",
                bridge_id="bridgeID",
                login_process_id="loginProcessID",
            )

    @parametrize
    async def test_method_whoami(self, async_client: AsyncBeeperDesktop) -> None:
        auth = await async_client.matrix.bridges.auth.whoami(
            "bridgeID",
        )
        assert_matches_type(AuthWhoamiResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_whoami(self, async_client: AsyncBeeperDesktop) -> None:
        response = await async_client.matrix.bridges.auth.with_raw_response.whoami(
            "bridgeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthWhoamiResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_whoami(self, async_client: AsyncBeeperDesktop) -> None:
        async with async_client.matrix.bridges.auth.with_streaming_response.whoami(
            "bridgeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthWhoamiResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_whoami(self, async_client: AsyncBeeperDesktop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bridge_id` but received ''"):
            await async_client.matrix.bridges.auth.with_raw_response.whoami(
                "",
            )
