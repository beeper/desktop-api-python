# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AuthListFlowsResponse", "Flow"]


class Flow(BaseModel):
    """An individual login flow which can be used to sign into the remote network."""

    id: str
    """
    An internal ID that is passed to the /login/start call to start a login with
    this flow.
    """

    description: str
    """A human-readable description of the login flow."""

    name: str
    """A human-readable name for the login flow."""


class AuthListFlowsResponse(BaseModel):
    flows: Optional[List[Flow]] = None
