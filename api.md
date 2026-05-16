# Shared Types

```python
from beeper_desktop_api.types import AppStateSnapshot, Attachment, Error, Message, Reaction, User
```

# BeeperDesktop

Types:

```python
from beeper_desktop_api.types import FocusResponse, SearchResponse
```

Methods:

- <code title="post /v1/focus">client.<a href="./src/beeper_desktop_api/_client.py">focus</a>(\*\*<a href="src/beeper_desktop_api/types/client_focus_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/focus_response.py">FocusResponse</a></code>
- <code title="get /v1/search">client.<a href="./src/beeper_desktop_api/_client.py">search</a>(\*\*<a href="src/beeper_desktop_api/types/client_search_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/search_response.py">SearchResponse</a></code>

# Accounts

Types:

```python
from beeper_desktop_api.types import Account, AccountListResponse
```

Methods:

- <code title="get /v1/accounts">client.accounts.<a href="./src/beeper_desktop_api/resources/accounts/accounts.py">list</a>() -> <a href="./src/beeper_desktop_api/types/account_list_response.py">AccountListResponse</a></code>

## Contacts

Types:

```python
from beeper_desktop_api.types.accounts import ContactSearchResponse
```

Methods:

- <code title="get /v1/accounts/{accountID}/contacts/list">client.accounts.contacts.<a href="./src/beeper_desktop_api/resources/accounts/contacts.py">list</a>(account_id, \*\*<a href="src/beeper_desktop_api/types/accounts/contact_list_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/shared/user.py">SyncCursorSearch[User]</a></code>
- <code title="get /v1/accounts/{accountID}/contacts">client.accounts.contacts.<a href="./src/beeper_desktop_api/resources/accounts/contacts.py">search</a>(account_id, \*\*<a href="src/beeper_desktop_api/types/accounts/contact_search_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/accounts/contact_search_response.py">ContactSearchResponse</a></code>

# Bridges

Types:

```python
from beeper_desktop_api.types import BridgeAvailability, BridgeListResponse
```

Methods:

- <code title="get /v1/bridges">client.bridges.<a href="./src/beeper_desktop_api/resources/bridges.py">list</a>() -> <a href="./src/beeper_desktop_api/types/bridge_list_response.py">BridgeListResponse</a></code>

# Chats

Types:

```python
from beeper_desktop_api.types import Chat, ChatCreateResponse, ChatListResponse, ChatStartResponse
```

Methods:

- <code title="post /v1/chats">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">create</a>(\*\*<a href="src/beeper_desktop_api/types/chat_create_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat_create_response.py">ChatCreateResponse</a></code>
- <code title="get /v1/chats/{chatID}">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">retrieve</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/chat_retrieve_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat.py">Chat</a></code>
- <code title="patch /v1/chats/{chatID}">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">update</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/chat_update_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat.py">Chat</a></code>
- <code title="get /v1/chats">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">list</a>(\*\*<a href="src/beeper_desktop_api/types/chat_list_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat_list_response.py">SyncCursorNoLimit[ChatListResponse]</a></code>
- <code title="post /v1/chats/{chatID}/archive">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">archive</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/chat_archive_params.py">params</a>) -> None</code>
- <code title="post /v1/chats/{chatID}/read">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">mark_read</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/chat_mark_read_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat.py">Chat</a></code>
- <code title="post /v1/chats/{chatID}/unread">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">mark_unread</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/chat_mark_unread_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat.py">Chat</a></code>
- <code title="post /v1/chats/{chatID}/notify-anyway">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">notify_anyway</a>(chat_id) -> <a href="./src/beeper_desktop_api/types/chat.py">Chat</a></code>
- <code title="get /v1/chats/search">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">search</a>(\*\*<a href="src/beeper_desktop_api/types/chat_search_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat.py">SyncCursorSearch[Chat]</a></code>
- <code title="post /v1/chats/start">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">start</a>(\*\*<a href="src/beeper_desktop_api/types/chat_start_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat_start_response.py">ChatStartResponse</a></code>

## Reminders

Methods:

- <code title="post /v1/chats/{chatID}/reminders">client.chats.reminders.<a href="./src/beeper_desktop_api/resources/chats/reminders.py">create</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/chats/reminder_create_params.py">params</a>) -> None</code>
- <code title="delete /v1/chats/{chatID}/reminders">client.chats.reminders.<a href="./src/beeper_desktop_api/resources/chats/reminders.py">delete</a>(chat_id) -> None</code>

## Messages

### Reactions

Types:

```python
from beeper_desktop_api.types.chats.messages import ReactionDeleteResponse, ReactionAddResponse
```

Methods:

- <code title="delete /v1/chats/{chatID}/messages/{messageID}/reactions/{reactionKey}">client.chats.messages.reactions.<a href="./src/beeper_desktop_api/resources/chats/messages/reactions.py">delete</a>(reaction_key, \*, chat_id, message_id) -> <a href="./src/beeper_desktop_api/types/chats/messages/reaction_delete_response.py">ReactionDeleteResponse</a></code>
- <code title="post /v1/chats/{chatID}/messages/{messageID}/reactions">client.chats.messages.reactions.<a href="./src/beeper_desktop_api/resources/chats/messages/reactions.py">add</a>(message_id, \*, chat_id, \*\*<a href="src/beeper_desktop_api/types/chats/messages/reaction_add_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chats/messages/reaction_add_response.py">ReactionAddResponse</a></code>

# Messages

Types:

```python
from beeper_desktop_api.types import MessageUpdateResponse, MessageSendResponse
```

Methods:

- <code title="get /v1/chats/{chatID}/messages/{messageID}">client.messages.<a href="./src/beeper_desktop_api/resources/messages.py">retrieve</a>(message_id, \*, chat_id) -> <a href="./src/beeper_desktop_api/types/shared/message.py">Message</a></code>
- <code title="put /v1/chats/{chatID}/messages/{messageID}">client.messages.<a href="./src/beeper_desktop_api/resources/messages.py">update</a>(message_id, \*, chat_id, \*\*<a href="src/beeper_desktop_api/types/message_update_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/message_update_response.py">MessageUpdateResponse</a></code>
- <code title="get /v1/chats/{chatID}/messages">client.messages.<a href="./src/beeper_desktop_api/resources/messages.py">list</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/message_list_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/shared/message.py">SyncCursorNoLimit[Message]</a></code>
- <code title="delete /v1/chats/{chatID}/messages/{messageID}">client.messages.<a href="./src/beeper_desktop_api/resources/messages.py">delete</a>(message_id, \*, chat_id, \*\*<a href="src/beeper_desktop_api/types/message_delete_params.py">params</a>) -> None</code>
- <code title="get /v1/messages/search">client.messages.<a href="./src/beeper_desktop_api/resources/messages.py">search</a>(\*\*<a href="src/beeper_desktop_api/types/message_search_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/shared/message.py">SyncCursorSearch[Message]</a></code>
- <code title="post /v1/chats/{chatID}/messages">client.messages.<a href="./src/beeper_desktop_api/resources/messages.py">send</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/message_send_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/message_send_response.py">MessageSendResponse</a></code>

# Assets

Types:

```python
from beeper_desktop_api.types import (
    AssetDownloadResponse,
    AssetUploadResponse,
    AssetUploadBase64Response,
)
```

Methods:

- <code title="post /v1/assets/download">client.assets.<a href="./src/beeper_desktop_api/resources/assets.py">download</a>(\*\*<a href="src/beeper_desktop_api/types/asset_download_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/asset_download_response.py">AssetDownloadResponse</a></code>
- <code title="get /v1/assets/serve">client.assets.<a href="./src/beeper_desktop_api/resources/assets.py">serve</a>(\*\*<a href="src/beeper_desktop_api/types/asset_serve_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/assets/upload">client.assets.<a href="./src/beeper_desktop_api/resources/assets.py">upload</a>(\*\*<a href="src/beeper_desktop_api/types/asset_upload_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/asset_upload_response.py">AssetUploadResponse</a></code>
- <code title="post /v1/assets/upload/base64">client.assets.<a href="./src/beeper_desktop_api/resources/assets.py">upload_base64</a>(\*\*<a href="src/beeper_desktop_api/types/asset_upload_base64_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/asset_upload_base64_response.py">AssetUploadBase64Response</a></code>

# Info

Types:

```python
from beeper_desktop_api.types import InfoRetrieveResponse
```

Methods:

- <code title="get /v1/info">client.info.<a href="./src/beeper_desktop_api/resources/info.py">retrieve</a>() -> <a href="./src/beeper_desktop_api/types/info_retrieve_response.py">InfoRetrieveResponse</a></code>

# App

Types:

```python
from beeper_desktop_api.types import (
    LoginRegistrationRequiredResponse,
    LoginResponse,
    LoginResponseOutput,
    RecoveryCodeResetResponse,
    StartVerificationResponse,
    StateMutationResponse,
    AppStatusResponse,
)
```

Methods:

- <code title="get /v1/app/status">client.app.<a href="./src/beeper_desktop_api/resources/app/app.py">status</a>() -> <a href="./src/beeper_desktop_api/types/app_status_response.py">AppStatusResponse</a></code>

## Login

Types:

```python
from beeper_desktop_api.types.app import (
    LoginRegisterResponse,
    LoginResponseResponse,
    LoginStartResponse,
)
```

Methods:

- <code title="post /v1/app/login/email">client.app.login.<a href="./src/beeper_desktop_api/resources/app/login.py">email</a>(\*\*<a href="src/beeper_desktop_api/types/app/login_email_params.py">params</a>) -> object</code>
- <code title="post /v1/app/login/register">client.app.login.<a href="./src/beeper_desktop_api/resources/app/login.py">register</a>(\*\*<a href="src/beeper_desktop_api/types/app/login_register_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/app/login_register_response.py">LoginRegisterResponse</a></code>
- <code title="post /v1/app/login/response">client.app.login.<a href="./src/beeper_desktop_api/resources/app/login.py">response</a>(\*\*<a href="src/beeper_desktop_api/types/app/login_response_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/app/login_response_response.py">LoginResponseResponse</a></code>
- <code title="post /v1/app/login/start">client.app.login.<a href="./src/beeper_desktop_api/resources/app/login.py">start</a>() -> <a href="./src/beeper_desktop_api/types/app/login_start_response.py">LoginStartResponse</a></code>

## E2ee

### RecoveryCode

Types:

```python
from beeper_desktop_api.types.app.e2ee import (
    RecoveryCodeMarkBackedUpResponse,
    RecoveryCodeVerifyResponse,
)
```

Methods:

- <code title="post /v1/app/e2ee/recovery-code/mark-backed-up">client.app.e2ee.recovery_code.<a href="./src/beeper_desktop_api/resources/app/e2ee/recovery_code/recovery_code.py">mark_backed_up</a>() -> <a href="./src/beeper_desktop_api/types/app/e2ee/recovery_code_mark_backed_up_response.py">RecoveryCodeMarkBackedUpResponse</a></code>
- <code title="post /v1/app/e2ee/recovery-code/verify">client.app.e2ee.recovery_code.<a href="./src/beeper_desktop_api/resources/app/e2ee/recovery_code/recovery_code.py">verify</a>(\*\*<a href="src/beeper_desktop_api/types/app/e2ee/recovery_code_verify_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/app/e2ee/recovery_code_verify_response.py">RecoveryCodeVerifyResponse</a></code>

#### Reset

Types:

```python
from beeper_desktop_api.types.app.e2ee.recovery_code import (
    ResetCreateResponse,
    ResetConfirmResponse,
)
```

Methods:

- <code title="post /v1/app/e2ee/recovery-code/reset">client.app.e2ee.recovery_code.reset.<a href="./src/beeper_desktop_api/resources/app/e2ee/recovery_code/reset.py">create</a>(\*\*<a href="src/beeper_desktop_api/types/app/e2ee/recovery_code/reset_create_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/app/e2ee/recovery_code/reset_create_response.py">ResetCreateResponse</a></code>
- <code title="post /v1/app/e2ee/recovery-code/reset/confirm">client.app.e2ee.recovery_code.reset.<a href="./src/beeper_desktop_api/resources/app/e2ee/recovery_code/reset.py">confirm</a>(\*\*<a href="src/beeper_desktop_api/types/app/e2ee/recovery_code/reset_confirm_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/app/e2ee/recovery_code/reset_confirm_response.py">ResetConfirmResponse</a></code>

### Verification

Types:

```python
from beeper_desktop_api.types.app.e2ee import (
    VerificationCreateResponse,
    VerificationAcceptResponse,
    VerificationCancelResponse,
)
```

Methods:

- <code title="post /v1/app/e2ee/verification">client.app.e2ee.verification.<a href="./src/beeper_desktop_api/resources/app/e2ee/verification/verification.py">create</a>(\*\*<a href="src/beeper_desktop_api/types/app/e2ee/verification_create_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/app/e2ee/verification_create_response.py">VerificationCreateResponse</a></code>
- <code title="post /v1/app/e2ee/verification/{verificationID}/accept">client.app.e2ee.verification.<a href="./src/beeper_desktop_api/resources/app/e2ee/verification/verification.py">accept</a>(verification_id) -> <a href="./src/beeper_desktop_api/types/app/e2ee/verification_accept_response.py">VerificationAcceptResponse</a></code>
- <code title="post /v1/app/e2ee/verification/{verificationID}/cancel">client.app.e2ee.verification.<a href="./src/beeper_desktop_api/resources/app/e2ee/verification/verification.py">cancel</a>(verification_id, \*\*<a href="src/beeper_desktop_api/types/app/e2ee/verification_cancel_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/app/e2ee/verification_cancel_response.py">VerificationCancelResponse</a></code>

#### Qr

Types:

```python
from beeper_desktop_api.types.app.e2ee.verification import QrConfirmScannedResponse, QrScanResponse
```

Methods:

- <code title="post /v1/app/e2ee/verification/{verificationID}/qr/confirm-scanned">client.app.e2ee.verification.qr.<a href="./src/beeper_desktop_api/resources/app/e2ee/verification/qr.py">confirm_scanned</a>(verification_id) -> <a href="./src/beeper_desktop_api/types/app/e2ee/verification/qr_confirm_scanned_response.py">QrConfirmScannedResponse</a></code>
- <code title="post /v1/app/e2ee/verification/qr/scan">client.app.e2ee.verification.qr.<a href="./src/beeper_desktop_api/resources/app/e2ee/verification/qr.py">scan</a>(\*\*<a href="src/beeper_desktop_api/types/app/e2ee/verification/qr_scan_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/app/e2ee/verification/qr_scan_response.py">QrScanResponse</a></code>

#### Sas

Types:

```python
from beeper_desktop_api.types.app.e2ee.verification import SaConfirmResponse, SaStartResponse
```

Methods:

- <code title="post /v1/app/e2ee/verification/{verificationID}/sas/confirm">client.app.e2ee.verification.sas.<a href="./src/beeper_desktop_api/resources/app/e2ee/verification/sas.py">confirm</a>(verification_id) -> <a href="./src/beeper_desktop_api/types/app/e2ee/verification/sa_confirm_response.py">SaConfirmResponse</a></code>
- <code title="post /v1/app/e2ee/verification/{verificationID}/sas/start">client.app.e2ee.verification.sas.<a href="./src/beeper_desktop_api/resources/app/e2ee/verification/sas.py">start</a>(verification_id) -> <a href="./src/beeper_desktop_api/types/app/e2ee/verification/sa_start_response.py">SaStartResponse</a></code>

# Matrix

## Users

Types:

```python
from beeper_desktop_api.types.matrix import UserRetrieveProfileResponse
```

Methods:

- <code title="get /_matrix/client/v3/profile/{userId}">client.matrix.users.<a href="./src/beeper_desktop_api/resources/matrix/users/users.py">retrieve_profile</a>(user_id) -> <a href="./src/beeper_desktop_api/types/matrix/user_retrieve_profile_response.py">UserRetrieveProfileResponse</a></code>

### AccountData

Methods:

- <code title="get /_matrix/client/v3/user/{userId}/account_data/{type}">client.matrix.users.account_data.<a href="./src/beeper_desktop_api/resources/matrix/users/account_data.py">retrieve</a>(type, \*, user_id) -> object</code>
- <code title="put /_matrix/client/v3/user/{userId}/account_data/{type}">client.matrix.users.account_data.<a href="./src/beeper_desktop_api/resources/matrix/users/account_data.py">update</a>(type, \*, user_id, \*\*<a href="src/beeper_desktop_api/types/matrix/users/account_data_update_params.py">params</a>) -> object</code>

## Rooms

Types:

```python
from beeper_desktop_api.types.matrix import RoomCreateResponse, RoomJoinResponse
```

Methods:

- <code title="post /_matrix/client/v3/createRoom">client.matrix.rooms.<a href="./src/beeper_desktop_api/resources/matrix/rooms/rooms.py">create</a>(\*\*<a href="src/beeper_desktop_api/types/matrix/room_create_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/room_create_response.py">RoomCreateResponse</a></code>
- <code title="post /_matrix/client/v3/join/{roomIdOrAlias}">client.matrix.rooms.<a href="./src/beeper_desktop_api/resources/matrix/rooms/rooms.py">join</a>(room_id_or_alias, \*\*<a href="src/beeper_desktop_api/types/matrix/room_join_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/room_join_response.py">RoomJoinResponse</a></code>
- <code title="post /_matrix/client/v3/rooms/{roomId}/leave">client.matrix.rooms.<a href="./src/beeper_desktop_api/resources/matrix/rooms/rooms.py">leave</a>(room_id, \*\*<a href="src/beeper_desktop_api/types/matrix/room_leave_params.py">params</a>) -> object</code>

### AccountData

Methods:

- <code title="get /_matrix/client/v3/user/{userId}/rooms/{roomId}/account_data/{type}">client.matrix.rooms.account_data.<a href="./src/beeper_desktop_api/resources/matrix/rooms/account_data.py">retrieve</a>(type, \*, user_id, room_id) -> object</code>
- <code title="put /_matrix/client/v3/user/{userId}/rooms/{roomId}/account_data/{type}">client.matrix.rooms.account_data.<a href="./src/beeper_desktop_api/resources/matrix/rooms/account_data.py">update</a>(type, \*, user_id, room_id, \*\*<a href="src/beeper_desktop_api/types/matrix/rooms/account_data_update_params.py">params</a>) -> object</code>

### State

Types:

```python
from beeper_desktop_api.types.matrix.rooms import StateRetrieveResponse, StateListResponse
```

Methods:

- <code title="get /_matrix/client/v3/rooms/{roomId}/state/{eventType}/{stateKey}">client.matrix.rooms.state.<a href="./src/beeper_desktop_api/resources/matrix/rooms/state.py">retrieve</a>(state_key, \*, room_id, event_type, \*\*<a href="src/beeper_desktop_api/types/matrix/rooms/state_retrieve_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/rooms/state_retrieve_response.py">StateRetrieveResponse</a></code>
- <code title="get /_matrix/client/v3/rooms/{roomId}/state">client.matrix.rooms.state.<a href="./src/beeper_desktop_api/resources/matrix/rooms/state.py">list</a>(room_id) -> <a href="./src/beeper_desktop_api/types/matrix/rooms/state_list_response.py">StateListResponse</a></code>

### Events

Types:

```python
from beeper_desktop_api.types.matrix.rooms import EventRetrieveResponse
```

Methods:

- <code title="get /_matrix/client/v3/rooms/{roomId}/event/{eventId}">client.matrix.rooms.events.<a href="./src/beeper_desktop_api/resources/matrix/rooms/events.py">retrieve</a>(event_id, \*, room_id) -> <a href="./src/beeper_desktop_api/types/matrix/rooms/event_retrieve_response.py">EventRetrieveResponse</a></code>

## Bridges

### Auth

Types:

```python
from beeper_desktop_api.types.matrix.bridges import (
    AuthListFlowsResponse,
    AuthListLoginsResponse,
    AuthStartLoginResponse,
    AuthSubmitCookiesResponse,
    AuthSubmitUserInputResponse,
    AuthWaitForStepResponse,
    AuthWhoamiResponse,
)
```

Methods:

- <code title="get /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/login/flows">client.matrix.bridges.auth.<a href="./src/beeper_desktop_api/resources/matrix/bridges/auth.py">list_flows</a>(bridge_id) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/auth_list_flows_response.py">AuthListFlowsResponse</a></code>
- <code title="get /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/logins">client.matrix.bridges.auth.<a href="./src/beeper_desktop_api/resources/matrix/bridges/auth.py">list_logins</a>(bridge_id) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/auth_list_logins_response.py">AuthListLoginsResponse</a></code>
- <code title="post /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/logout/{loginID}">client.matrix.bridges.auth.<a href="./src/beeper_desktop_api/resources/matrix/bridges/auth.py">logout</a>(login_id, \*, bridge_id) -> object</code>
- <code title="post /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/login/start/{flowID}">client.matrix.bridges.auth.<a href="./src/beeper_desktop_api/resources/matrix/bridges/auth.py">start_login</a>(flow_id, \*, bridge_id, \*\*<a href="src/beeper_desktop_api/types/matrix/bridges/auth_start_login_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/auth_start_login_response.py">AuthStartLoginResponse</a></code>
- <code title="post /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/login/step/{loginProcessID}/{stepID}/cookies">client.matrix.bridges.auth.<a href="./src/beeper_desktop_api/resources/matrix/bridges/auth.py">submit_cookies</a>(step_id, \*, bridge_id, login_process_id, \*\*<a href="src/beeper_desktop_api/types/matrix/bridges/auth_submit_cookies_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/auth_submit_cookies_response.py">AuthSubmitCookiesResponse</a></code>
- <code title="post /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/login/step/{loginProcessID}/{stepID}/user_input">client.matrix.bridges.auth.<a href="./src/beeper_desktop_api/resources/matrix/bridges/auth.py">submit_user_input</a>(step_id, \*, bridge_id, login_process_id, \*\*<a href="src/beeper_desktop_api/types/matrix/bridges/auth_submit_user_input_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/auth_submit_user_input_response.py">AuthSubmitUserInputResponse</a></code>
- <code title="post /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/login/step/{loginProcessID}/{stepID}/display_and_wait">client.matrix.bridges.auth.<a href="./src/beeper_desktop_api/resources/matrix/bridges/auth.py">wait_for_step</a>(step_id, \*, bridge_id, login_process_id) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/auth_wait_for_step_response.py">AuthWaitForStepResponse</a></code>
- <code title="get /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/whoami">client.matrix.bridges.auth.<a href="./src/beeper_desktop_api/resources/matrix/bridges/auth.py">whoami</a>(bridge_id) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/auth_whoami_response.py">AuthWhoamiResponse</a></code>

### Contacts

Types:

```python
from beeper_desktop_api.types.matrix.bridges import ContactListResponse
```

Methods:

- <code title="get /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/contacts">client.matrix.bridges.contacts.<a href="./src/beeper_desktop_api/resources/matrix/bridges/contacts.py">list</a>(bridge_id, \*\*<a href="src/beeper_desktop_api/types/matrix/bridges/contact_list_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/contact_list_response.py">ContactListResponse</a></code>

### Users

Types:

```python
from beeper_desktop_api.types.matrix.bridges import UserResolveResponse, UserSearchResponse
```

Methods:

- <code title="get /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/resolve_identifier/{identifier}">client.matrix.bridges.users.<a href="./src/beeper_desktop_api/resources/matrix/bridges/users.py">resolve</a>(identifier, \*, bridge_id, \*\*<a href="src/beeper_desktop_api/types/matrix/bridges/user_resolve_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/user_resolve_response.py">UserResolveResponse</a></code>
- <code title="post /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/search_users">client.matrix.bridges.users.<a href="./src/beeper_desktop_api/resources/matrix/bridges/users.py">search</a>(bridge_id, \*\*<a href="src/beeper_desktop_api/types/matrix/bridges/user_search_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/user_search_response.py">UserSearchResponse</a></code>

### Rooms

Types:

```python
from beeper_desktop_api.types.matrix.bridges import RoomCreateDmResponse, RoomCreateGroupResponse
```

Methods:

- <code title="post /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/create_dm/{identifier}">client.matrix.bridges.rooms.<a href="./src/beeper_desktop_api/resources/matrix/bridges/rooms.py">create_dm</a>(identifier, \*, bridge_id, \*\*<a href="src/beeper_desktop_api/types/matrix/bridges/room_create_dm_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/room_create_dm_response.py">RoomCreateDmResponse</a></code>
- <code title="post /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/create_group/{groupType}">client.matrix.bridges.rooms.<a href="./src/beeper_desktop_api/resources/matrix/bridges/rooms.py">create_group</a>(group_type, \*, bridge_id, \*\*<a href="src/beeper_desktop_api/types/matrix/bridges/room_create_group_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/room_create_group_response.py">RoomCreateGroupResponse</a></code>

### Capabilities

Types:

```python
from beeper_desktop_api.types.matrix.bridges import CapabilityRetrieveResponse
```

Methods:

- <code title="get /_matrix/client/unstable/com.beeper.bridge/{bridgeID}/_matrix/provision/v3/capabilities">client.matrix.bridges.capabilities.<a href="./src/beeper_desktop_api/resources/matrix/bridges/capabilities.py">retrieve</a>(bridge_id) -> <a href="./src/beeper_desktop_api/types/matrix/bridges/capability_retrieve_response.py">CapabilityRetrieveResponse</a></code>
