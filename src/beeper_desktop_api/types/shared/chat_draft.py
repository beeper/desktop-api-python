# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .draft_attachment import DraftAttachment

__all__ = ["ChatDraft"]


class ChatDraft(BaseModel):
    """Current draft object for this chat, or null when no draft is set."""

    text: str
    """Rich-text draft body as returned by Beeper."""

    attachments: Optional[Dict[str, DraftAttachment]] = None
    """Draft attachments keyed by attachment ID."""
