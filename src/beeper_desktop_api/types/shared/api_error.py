# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["APIError"]


class APIError(BaseModel):
    code: str

    message: str

    details: Optional[Dict[str, Optional[object]]] = None
