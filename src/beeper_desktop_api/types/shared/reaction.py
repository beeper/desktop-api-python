# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Reaction"]


class Reaction(BaseModel):
    id: str
    """Reaction ID.

    When a participant can react more than once, the ID is the participant ID
    concatenated with the reaction key; otherwise it equals the participant ID.
    """

    participant_id: str = FieldInfo(alias="participantID")
    """User ID of the participant who reacted."""

    reaction_key: str = FieldInfo(alias="reactionKey")
    """
    The reaction key: an emoji (😄), a network-specific key, or a shortcode like
    "smiling-face".
    """

    emoji: Optional[bool] = None
    """True if the reactionKey is an emoji."""

    img_url: Optional[str] = FieldInfo(alias="imgURL", default=None)
    """URL to the reaction's image.

    May be temporary or available only on this device; download promptly if durable
    access is needed.
    """
