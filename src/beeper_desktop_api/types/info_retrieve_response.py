# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["InfoRetrieveResponse", "App", "Endpoints", "EndpointsOAuth", "Platform", "Server"]


class App(BaseModel):
    bundle_id: str
    """App bundle identifier"""

    name: str
    """App name"""

    version: str
    """App version"""


class EndpointsOAuth(BaseModel):
    authorization_endpoint: str
    """OAuth authorization endpoint"""

    introspection_endpoint: str
    """OAuth introspection endpoint"""

    registration_endpoint: str
    """OAuth dynamic client registration endpoint"""

    revocation_endpoint: str
    """OAuth token revocation endpoint"""

    token_endpoint: str
    """OAuth token endpoint"""

    userinfo_endpoint: str
    """OAuth userinfo endpoint"""


class Endpoints(BaseModel):
    mcp: str
    """MCP endpoint"""

    oauth: EndpointsOAuth

    spec: str
    """OpenAPI spec endpoint"""

    ws_events: str
    """WebSocket events endpoint"""


class Platform(BaseModel):
    arch: str
    """CPU architecture"""

    os: str
    """Operating system identifier"""

    release: Optional[str] = None
    """Runtime release version"""


class Server(BaseModel):
    base_url: str
    """Base URL of the Connect server"""

    hostname: str
    """Listening host"""

    mcp_enabled: bool
    """Whether MCP endpoint is enabled"""

    port: int
    """Listening port"""

    remote_access: bool
    """Whether remote access is enabled"""

    status: str
    """Server status"""


class InfoRetrieveResponse(BaseModel):
    app: App

    endpoints: Endpoints

    platform: Platform

    server: Server
