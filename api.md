# Shared Types

```python
from beeper_desktop_api.types import (
    APIError,
    AppStateSnapshot,
    Attachment,
    Error,
    Message,
    Reaction,
    User,
)
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
from beeper_desktop_api.types import (
    Account,
    AccountBridge,
    AccountRetrieveResponse,
    AccountListResponse,
)
```

Methods:

- <code title="get /v1/accounts/{accountID}">client.accounts.<a href="./src/beeper_desktop_api/resources/accounts/accounts.py">retrieve</a>(account_id) -> <a href="./src/beeper_desktop_api/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
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
from beeper_desktop_api.types import (
    Bridge,
    CookieField,
    DisappearingTimerCapability,
    GroupFieldCapability,
    GroupTypeCapabilities,
    LoginFlow,
    LoginInputField,
    LoginSession,
    ProvisioningCapabilities,
    ResolveIdentifierCapabilities,
    BridgeRetrieveResponse,
    BridgeListResponse,
)
```

Methods:

- <code title="get /v1/bridges/{bridgeID}">client.bridges.<a href="./src/beeper_desktop_api/resources/bridges/bridges.py">retrieve</a>(bridge_id) -> <a href="./src/beeper_desktop_api/types/bridge_retrieve_response.py">BridgeRetrieveResponse</a></code>
- <code title="get /v1/bridges">client.bridges.<a href="./src/beeper_desktop_api/resources/bridges/bridges.py">list</a>() -> <a href="./src/beeper_desktop_api/types/bridge_list_response.py">BridgeListResponse</a></code>
- <code title="get /v1/bridges/{bridgeID}/capabilities">client.bridges.<a href="./src/beeper_desktop_api/resources/bridges/bridges.py">retrieve_capabilities</a>(bridge_id) -> <a href="./src/beeper_desktop_api/types/provisioning_capabilities.py">ProvisioningCapabilities</a></code>

## LoginFlows

Types:

```python
from beeper_desktop_api.types.bridges import LoginFlowListResponse
```

Methods:

- <code title="get /v1/bridges/{bridgeID}/login-flows">client.bridges.login_flows.<a href="./src/beeper_desktop_api/resources/bridges/login_flows.py">list</a>(bridge_id) -> <a href="./src/beeper_desktop_api/types/bridges/login_flow_list_response.py">LoginFlowListResponse</a></code>

## LoginSessions

Types:

```python
from beeper_desktop_api.types.bridges import LoginSessionCancelResponse
```

Methods:

- <code title="post /v1/bridges/{bridgeID}/login-sessions">client.bridges.login_sessions.<a href="./src/beeper_desktop_api/resources/bridges/login_sessions/login_sessions.py">create</a>(bridge_id, \*\*<a href="src/beeper_desktop_api/types/bridges/login_session_create_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/login_session.py">LoginSession</a></code>
- <code title="get /v1/bridges/{bridgeID}/login-sessions/{loginSessionID}">client.bridges.login_sessions.<a href="./src/beeper_desktop_api/resources/bridges/login_sessions/login_sessions.py">retrieve</a>(login_session_id, \*, bridge_id) -> <a href="./src/beeper_desktop_api/types/login_session.py">LoginSession</a></code>
- <code title="delete /v1/bridges/{bridgeID}/login-sessions/{loginSessionID}">client.bridges.login_sessions.<a href="./src/beeper_desktop_api/resources/bridges/login_sessions/login_sessions.py">cancel</a>(login_session_id, \*, bridge_id) -> <a href="./src/beeper_desktop_api/types/bridges/login_session_cancel_response.py">LoginSessionCancelResponse</a></code>

### Steps

Methods:

- <code title="post /v1/bridges/{bridgeID}/login-sessions/{loginSessionID}/steps/{stepID}">client.bridges.login_sessions.steps.<a href="./src/beeper_desktop_api/resources/bridges/login_sessions/steps.py">submit</a>(step_id, \*, bridge_id, login_session_id, \*\*<a href="src/beeper_desktop_api/types/bridges/login_sessions/step_submit_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/login_session.py">LoginSession</a></code>

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
from beeper_desktop_api.types import Verification
```
