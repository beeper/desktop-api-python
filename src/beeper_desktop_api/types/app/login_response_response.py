# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "LoginResponseResponse",
    "UnionMember0",
    "UnionMember0AppState",
    "UnionMember0AppStateE2ee",
    "UnionMember0AppStateE2eeSecrets",
    "UnionMember0AppStateMatrix",
    "UnionMember0AppStateVerification",
    "UnionMember0AppStateVerificationError",
    "UnionMember0AppStateVerificationSas",
    "UnionMember0DesktopAPI",
    "UnionMember0Matrix",
    "UnionMember1",
    "UnionMember1Copy",
]


class UnionMember0AppStateE2eeSecrets(BaseModel):
    """Encrypted messaging keys available on this device."""

    master_key: bool = FieldInfo(alias="masterKey")
    """Whether the account identity key is available."""

    megolm_backup_key: bool = FieldInfo(alias="megolmBackupKey")
    """Whether the encrypted message backup key is available."""

    recovery_code: bool = FieldInfo(alias="recoveryCode")
    """Whether a recovery key is available."""

    self_signing_key: bool = FieldInfo(alias="selfSigningKey")
    """Whether the device trust key is available."""

    user_signing_key: bool = FieldInfo(alias="userSigningKey")
    """Whether the user trust key is available."""


class UnionMember0AppStateE2ee(BaseModel):
    """Encrypted messaging setup status."""

    cross_signing: bool = FieldInfo(alias="crossSigning")
    """Whether this account can verify trusted devices."""

    first_sync_done: bool = FieldInfo(alias="firstSyncDone")
    """Whether the first encrypted message sync is complete."""

    has_backed_up_code: bool = FieldInfo(alias="hasBackedUpCode")
    """Whether the user confirmed that they saved their recovery key."""

    initialized: bool
    """Whether encrypted messaging setup has started."""

    key_backup: bool = FieldInfo(alias="keyBackup")
    """Whether encrypted message backup is available."""

    secrets: UnionMember0AppStateE2eeSecrets
    """Encrypted messaging keys available on this device."""

    secret_storage: bool = FieldInfo(alias="secretStorage")
    """Whether secure key storage is available."""

    verified: bool
    """Whether this device is trusted for encrypted messages."""

    recovery_code_generated_at: Optional[float] = FieldInfo(alias="recoveryCodeGeneratedAt", default=None)
    """Unix timestamp for when the recovery key was created."""


class UnionMember0AppStateMatrix(BaseModel):
    """Signed-in account details. Omitted until sign-in is complete."""

    device_id: str = FieldInfo(alias="deviceID")
    """Current device ID."""

    homeserver: str
    """Beeper server URL for this account."""

    user_id: str = FieldInfo(alias="userID")
    """Signed-in Beeper user ID."""


class UnionMember0AppStateVerificationError(BaseModel):
    """Verification error details, if verification stopped."""

    code: str
    """Verification error code."""

    reason: str
    """User-facing verification error message."""


class UnionMember0AppStateVerificationSas(BaseModel):
    """Emoji or number comparison data for verification."""

    decimals: str
    """Number sequence to compare on both devices."""

    emojis: str
    """Emoji sequence to compare on both devices."""


class UnionMember0AppStateVerification(BaseModel):
    """Trusted-device verification progress."""

    available_actions: List[
        Literal["create", "qr.scan", "accept", "cancel", "qr.confirmScanned", "sas.start", "sas.confirm"]
    ] = FieldInfo(alias="availableActions")
    """Verification actions that are valid for the current state."""

    state: Literal["idle", "requested", "ready", "sas_ready", "qr_scanned", "done", "cancelled", "error"]
    """Current trusted-device verification state."""

    error: Optional[UnionMember0AppStateVerificationError] = None
    """Verification error details, if verification stopped."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """User ID that started verification."""

    from_device: Optional[str] = FieldInfo(alias="fromDevice", default=None)
    """Device that started verification."""

    other_device: Optional[str] = FieldInfo(alias="otherDevice", default=None)
    """Other device participating in verification."""

    qr_data: Optional[str] = FieldInfo(alias="qrData", default=None)
    """QR code payload to display for verification."""

    sas: Optional[UnionMember0AppStateVerificationSas] = None
    """Emoji or number comparison data for verification."""

    supports_sas: Optional[bool] = FieldInfo(alias="supportsSAS", default=None)
    """Whether emoji comparison is available."""

    supports_scan_qr_code: Optional[bool] = FieldInfo(alias="supportsScanQRCode", default=None)
    """Whether QR code verification is available."""

    verification_id: Optional[str] = FieldInfo(alias="verificationID", default=None)
    """Verification ID to pass in verification action paths."""


class UnionMember0AppState(BaseModel):
    """Current onboarding state after sign-in."""

    e2ee: UnionMember0AppStateE2ee
    """Encrypted messaging setup status."""

    state: Literal[
        "needs-login",
        "initializing",
        "needs-cross-signing-setup",
        "needs-verification",
        "needs-secrets",
        "needs-first-sync",
        "ready",
    ]
    """Current onboarding state for Beeper Desktop."""

    matrix: Optional[UnionMember0AppStateMatrix] = None
    """Signed-in account details. Omitted until sign-in is complete."""

    verification: Optional[UnionMember0AppStateVerification] = None
    """Trusted-device verification progress."""


class UnionMember0DesktopAPI(BaseModel):
    """Desktop API credentials for the signed-in app session."""

    access_token: str = FieldInfo(alias="accessToken")
    """Desktop API access token for this app session."""

    scope: Literal["read write"]
    """Granted Desktop API scopes."""

    token_type: Literal["Bearer"] = FieldInfo(alias="tokenType")
    """Access token type."""


class UnionMember0Matrix(BaseModel):
    """Account credentials for first-party app setup."""

    access_token: str = FieldInfo(alias="accessToken")
    """Account access token. Returned once for first-party app setup."""

    device_id: str = FieldInfo(alias="deviceID")
    """Current device ID."""

    homeserver: str
    """Beeper server URL for this account."""

    user_id: str = FieldInfo(alias="userID")
    """Signed-in Beeper user ID."""


class UnionMember0(BaseModel):
    app_state: UnionMember0AppState = FieldInfo(alias="appState")
    """Current onboarding state after sign-in."""

    desktop_api: UnionMember0DesktopAPI = FieldInfo(alias="desktopAPI")
    """Desktop API credentials for the signed-in app session."""

    matrix: UnionMember0Matrix
    """Account credentials for first-party app setup."""


class UnionMember1Copy(BaseModel):
    """Copy to display during account creation."""

    submit: Literal["Continue"]
    """Submit button label."""

    terms: Literal["By continuing, you agree to the Terms of Use and acknowledge the Privacy Policy."]
    """Terms and privacy notice to show before account creation."""

    title: Literal["Choose your username"]
    """Title for the username step."""

    username_placeholder: Literal["Username"] = FieldInfo(alias="usernamePlaceholder")
    """Placeholder for the username field."""


class UnionMember1(BaseModel):
    copy_: UnionMember1Copy = FieldInfo(alias="copy")
    """Copy to display during account creation."""

    lead_token: str = FieldInfo(alias="leadToken")
    """Registration token returned by Beeper."""

    registration_required: Literal[True] = FieldInfo(alias="registrationRequired")
    """Indicates that the user needs to create a Beeper account."""

    request: str
    """Login request ID to use when creating the account."""

    username_suggestions: Optional[List[str]] = FieldInfo(alias="usernameSuggestions", default=None)
    """Suggested usernames for the new account."""


LoginResponseResponse: TypeAlias = Union[UnionMember0, UnionMember1]
