# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReminderCreateParams", "Reminder"]


class ReminderCreateParams(TypedDict, total=False):
    chat_id: Required[Annotated[str, PropertyInfo(alias="chatID")]]
    """
    The identifier of the chat to set reminder for (accepts both chatID and local
    chat ID)
    """

    reminder: Required[Reminder]
    """Reminder configuration"""


class Reminder(TypedDict, total=False):
    remind_at_ms: Required[Annotated[float, PropertyInfo(alias="remindAtMs")]]
    """Unix timestamp in milliseconds when reminder should trigger"""

    dismiss_on_incoming_message: Annotated[bool, PropertyInfo(alias="dismissOnIncomingMessage")]
    """Cancel reminder if someone messages in the chat"""
