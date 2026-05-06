# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReminderCreateParams", "Reminder"]


class ReminderCreateParams(TypedDict, total=False):
    reminder: Required[Reminder]
    """Reminder configuration"""


class Reminder(TypedDict, total=False):
    """Reminder configuration"""

    remind_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="remindAt", format="iso8601")]]
    """Timestamp when the reminder should trigger."""

    dismiss_on_incoming_message: Annotated[bool, PropertyInfo(alias="dismissOnIncomingMessage")]
    """Cancel reminder if someone messages in the chat"""
