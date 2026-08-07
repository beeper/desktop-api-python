# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "SASConfirmResponse",
    "Session",
    "SessionE2EE",
    "SessionE2EESecrets",
    "SessionMatrix",
    "SessionVerification",
    "SessionVerificationError",
    "SessionVerificationOtherDevice",
    "SessionVerificationQr",
    "SessionVerificationSAS",
    "Verification",
    "VerificationError",
    "VerificationOtherDevice",
    "VerificationQr",
    "VerificationSAS",
]


class SessionE2EESecrets(BaseModel):
    """Encrypted messaging keys available on this device."""

    master_key: bool = FieldInfo(alias="masterKey")
    """Whether the account identity key is available."""

    megolm_backup_key: bool = FieldInfo(alias="megolmBackupKey")
    """Whether the encrypted message backup key is available."""

    recovery_key: bool = FieldInfo(alias="recoveryKey")
    """Whether a recovery key is available."""

    self_signing_key: bool = FieldInfo(alias="selfSigningKey")
    """Whether the device trust key is available."""

    user_signing_key: bool = FieldInfo(alias="userSigningKey")
    """Whether the user trust key is available."""


class SessionE2EE(BaseModel):
    """Encrypted messaging setup status."""

    cross_signing: bool = FieldInfo(alias="crossSigning")
    """Whether this account can verify trusted devices."""

    first_sync_done: bool = FieldInfo(alias="firstSyncDone")
    """Whether the first encrypted message sync is complete."""

    has_backed_up_recovery_key: bool = FieldInfo(alias="hasBackedUpRecoveryKey")
    """Whether the user confirmed that they saved their recovery key."""

    initialized: bool
    """Whether encrypted messaging setup has started."""

    key_backup: bool = FieldInfo(alias="keyBackup")
    """Whether encrypted message backup is available."""

    secrets: SessionE2EESecrets
    """Encrypted messaging keys available on this device."""

    secret_storage: bool = FieldInfo(alias="secretStorage")
    """Whether secure key storage is available."""

    verified: bool
    """Whether this device is trusted for encrypted messages."""

    recovery_key_generated_at: Optional[float] = FieldInfo(alias="recoveryKeyGeneratedAt", default=None)
    """Unix timestamp for when the recovery key was created."""


class SessionMatrix(BaseModel):
    """Signed-in account details. Omitted until sign-in is complete."""

    device_id: str = FieldInfo(alias="deviceID")
    """Current device ID."""

    homeserver: str
    """Beeper homeserver URL for this account."""

    user_id: str = FieldInfo(alias="userID")
    """Signed-in Beeper user ID."""


class SessionVerificationError(BaseModel):
    """Verification error details, if verification stopped."""

    code: str
    """Verification error code."""

    reason: str
    """User-facing verification error message."""


class SessionVerificationOtherDevice(BaseModel):
    """Other device participating in verification."""

    id: str
    """Other device ID."""

    name: Optional[str] = None
    """Other device display name, if known."""


class SessionVerificationQr(BaseModel):
    """QR verification data."""

    data: str
    """QR code payload to display for verification."""


class SessionVerificationSAS(BaseModel):
    """Emoji or number comparison data for verification."""

    emojis: str
    """Emoji sequence to compare on both devices."""

    decimals: Optional[str] = None
    """Number sequence to compare on both devices."""


class SessionVerification(BaseModel):
    """Trusted device verification progress."""

    id: str
    """Verification ID to pass in verification action paths."""

    available_actions: List[Literal["accept", "cancel", "qr.confirmScanned", "sas.start", "sas.confirm"]] = FieldInfo(
        alias="availableActions"
    )
    """Verification actions that are valid for the current state."""

    direction: Literal["incoming", "outgoing"]
    """Whether this device started or received the verification."""

    methods: List[Literal["qr", "sas"]]
    """Verification methods supported for this transaction."""

    purpose: Literal["login", "device"]
    """Why this verification exists."""

    state: Literal["requested", "ready", "sas_ready", "qr_scanned", "done", "cancelled", "error"]
    """Current trusted-device verification state."""

    error: Optional[SessionVerificationError] = None
    """Verification error details, if verification stopped."""

    other_device: Optional[SessionVerificationOtherDevice] = FieldInfo(alias="otherDevice", default=None)
    """Other device participating in verification."""

    other_user_id: Optional[str] = FieldInfo(alias="otherUserID", default=None)
    """Other Beeper user participating in verification."""

    qr: Optional[SessionVerificationQr] = None
    """QR verification data."""

    sas: Optional[SessionVerificationSAS] = None
    """Emoji or number comparison data for verification."""


class Session(BaseModel):
    """Current app sign-in and encrypted messaging setup state."""

    e2ee: SessionE2EE
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
    """
    Current sign-in and encrypted messaging setup state for Beeper Desktop or Beeper
    Server.
    """

    matrix: Optional[SessionMatrix] = None
    """Signed-in account details. Omitted until sign-in is complete."""

    verification: Optional[SessionVerification] = None
    """Trusted device verification progress."""


class VerificationError(BaseModel):
    """Verification error details, if verification stopped."""

    code: str
    """Verification error code."""

    reason: str
    """User-facing verification error message."""


class VerificationOtherDevice(BaseModel):
    """Other device participating in verification."""

    id: str
    """Other device ID."""

    name: Optional[str] = None
    """Other device display name, if known."""


class VerificationQr(BaseModel):
    """QR verification data."""

    data: str
    """QR code payload to display for verification."""


class VerificationSAS(BaseModel):
    """Emoji or number comparison data for verification."""

    emojis: str
    """Emoji sequence to compare on both devices."""

    decimals: Optional[str] = None
    """Number sequence to compare on both devices."""


class Verification(BaseModel):
    """Trusted device verification progress."""

    id: str
    """Verification ID to pass in verification action paths."""

    available_actions: List[Literal["accept", "cancel", "qr.confirmScanned", "sas.start", "sas.confirm"]] = FieldInfo(
        alias="availableActions"
    )
    """Verification actions that are valid for the current state."""

    direction: Literal["incoming", "outgoing"]
    """Whether this device started or received the verification."""

    methods: List[Literal["qr", "sas"]]
    """Verification methods supported for this transaction."""

    purpose: Literal["login", "device"]
    """Why this verification exists."""

    state: Literal["requested", "ready", "sas_ready", "qr_scanned", "done", "cancelled", "error"]
    """Current trusted-device verification state."""

    error: Optional[VerificationError] = None
    """Verification error details, if verification stopped."""

    other_device: Optional[VerificationOtherDevice] = FieldInfo(alias="otherDevice", default=None)
    """Other device participating in verification."""

    other_user_id: Optional[str] = FieldInfo(alias="otherUserID", default=None)
    """Other Beeper user participating in verification."""

    qr: Optional[VerificationQr] = None
    """QR verification data."""

    sas: Optional[VerificationSAS] = None
    """Emoji or number comparison data for verification."""


class SASConfirmResponse(BaseModel):
    session: Session
    """Current app sign-in and encrypted messaging setup state."""

    verification: Optional[Verification] = None
    """Trusted device verification progress."""
