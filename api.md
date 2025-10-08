# Shared Types

```python
from beeper_desktop_api.types import Attachment, BaseResponse, Error, Message, Reaction, User
```

# BeeperDesktop

Types:

```python
from beeper_desktop_api.types import DownloadAssetResponse, FocusResponse, SearchResponse
```

Methods:

- <code title="post /v1/download-asset">client.<a href="./src/beeper_desktop_api/_client.py">download_asset</a>(\*\*<a href="src/beeper_desktop_api/types/client_download_asset_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/download_asset_response.py">DownloadAssetResponse</a></code>
- <code title="post /v1/focus">client.<a href="./src/beeper_desktop_api/_client.py">focus</a>(\*\*<a href="src/beeper_desktop_api/types/client_focus_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/focus_response.py">FocusResponse</a></code>
- <code title="get /v1/search">client.<a href="./src/beeper_desktop_api/_client.py">search</a>(\*\*<a href="src/beeper_desktop_api/types/client_search_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/search_response.py">SearchResponse</a></code>

# Accounts

Types:

```python
from beeper_desktop_api.types import Account, AccountListResponse
```

Methods:

- <code title="get /v1/accounts">client.accounts.<a href="./src/beeper_desktop_api/resources/accounts.py">list</a>() -> <a href="./src/beeper_desktop_api/types/account_list_response.py">AccountListResponse</a></code>

# Search

Types:

```python
from beeper_desktop_api.types import SearchContactsResponse
```

Methods:

- <code title="get /v1/search/chats">client.search.<a href="./src/beeper_desktop_api/resources/search.py">chats</a>(\*\*<a href="src/beeper_desktop_api/types/search_chats_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat.py">SyncCursorSearch[Chat]</a></code>
- <code title="get /v1/search/contacts/{accountID}">client.search.<a href="./src/beeper_desktop_api/resources/search.py">contacts</a>(account_id, \*\*<a href="src/beeper_desktop_api/types/search_contacts_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/search_contacts_response.py">SearchContactsResponse</a></code>

# Chats

Types:

```python
from beeper_desktop_api.types import Chat, ChatCreateResponse, ChatListResponse
```

Methods:

- <code title="post /v1/chats">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">create</a>(\*\*<a href="src/beeper_desktop_api/types/chat_create_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat_create_response.py">ChatCreateResponse</a></code>
- <code title="get /v1/chats/{chatID}">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">retrieve</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/chat_retrieve_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat.py">Chat</a></code>
- <code title="get /v1/chats">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">list</a>(\*\*<a href="src/beeper_desktop_api/types/chat_list_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/chat_list_response.py">SyncCursorList[ChatListResponse]</a></code>
- <code title="post /v1/chats/{chatID}/archive">client.chats.<a href="./src/beeper_desktop_api/resources/chats/chats.py">archive</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/chat_archive_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/shared/base_response.py">BaseResponse</a></code>

## Reminders

Methods:

- <code title="post /v1/chats/{chatID}/reminders">client.chats.reminders.<a href="./src/beeper_desktop_api/resources/chats/reminders.py">create</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/chats/reminder_create_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/shared/base_response.py">BaseResponse</a></code>
- <code title="delete /v1/chats/{chatID}/reminders">client.chats.reminders.<a href="./src/beeper_desktop_api/resources/chats/reminders.py">delete</a>(chat_id) -> <a href="./src/beeper_desktop_api/types/shared/base_response.py">BaseResponse</a></code>

# Messages

Types:

```python
from beeper_desktop_api.types import MessageSendResponse
```

Methods:

- <code title="get /v1/chats/{chatID}/messages">client.messages.<a href="./src/beeper_desktop_api/resources/messages.py">list</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/message_list_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/shared/message.py">SyncCursorList[Message]</a></code>
- <code title="get /v1/search/messages">client.messages.<a href="./src/beeper_desktop_api/resources/messages.py">search</a>(\*\*<a href="src/beeper_desktop_api/types/message_search_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/shared/message.py">SyncCursorSearch[Message]</a></code>
- <code title="post /v1/chats/{chatID}/messages">client.messages.<a href="./src/beeper_desktop_api/resources/messages.py">send</a>(chat_id, \*\*<a href="src/beeper_desktop_api/types/message_send_params.py">params</a>) -> <a href="./src/beeper_desktop_api/types/message_send_response.py">MessageSendResponse</a></code>
