# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AuthListLoginsResponse"]


class AuthListLoginsResponse(BaseModel):
    login_ids: Optional[List[str]] = None
