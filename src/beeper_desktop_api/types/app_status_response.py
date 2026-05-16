# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AppStatusResponse", "E2ee", "E2eeSecrets", "Matrix", "Verification", "VerificationError", "VerificationSas"]


class E2eeSecrets(BaseModel):
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


class E2ee(BaseModel):
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

    secrets: E2eeSecrets
    """Encrypted messaging keys available on this device."""

    secret_storage: bool = FieldInfo(alias="secretStorage")
    """Whether secure key storage is available."""

    verified: bool
    """Whether this device is trusted for encrypted messages."""

    recovery_code_generated_at: Optional[float] = FieldInfo(alias="recoveryCodeGeneratedAt", default=None)
    """Unix timestamp for when the recovery key was created."""


class Matrix(BaseModel):
    """Signed-in account details. Omitted until sign-in is complete."""

    device_id: str = FieldInfo(alias="deviceID")
    """Current device ID."""

    homeserver: str
    """Beeper server URL for this account."""

    user_id: str = FieldInfo(alias="userID")
    """Signed-in Beeper user ID."""


class VerificationError(BaseModel):
    """Verification error details, if verification stopped."""

    code: str
    """Verification error code."""

    reason: str
    """User-facing verification error message."""


class VerificationSas(BaseModel):
    """Emoji or number comparison data for verification."""

    decimals: str
    """Number sequence to compare on both devices."""

    emojis: str
    """Emoji sequence to compare on both devices."""


class Verification(BaseModel):
    """Trusted-device verification progress."""

    available_actions: List[
        Literal["create", "qr.scan", "accept", "cancel", "qr.confirmScanned", "sas.start", "sas.confirm"]
    ] = FieldInfo(alias="availableActions")
    """Verification actions that are valid for the current state."""

    state: Literal["idle", "requested", "ready", "sas_ready", "qr_scanned", "done", "cancelled", "error"]
    """Current trusted-device verification state."""

    error: Optional[VerificationError] = None
    """Verification error details, if verification stopped."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """User ID that started verification."""

    from_device: Optional[str] = FieldInfo(alias="fromDevice", default=None)
    """Device that started verification."""

    other_device: Optional[str] = FieldInfo(alias="otherDevice", default=None)
    """Other device participating in verification."""

    qr_data: Optional[str] = FieldInfo(alias="qrData", default=None)
    """QR code payload to display for verification."""

    sas: Optional[VerificationSas] = None
    """Emoji or number comparison data for verification."""

    supports_sas: Optional[bool] = FieldInfo(alias="supportsSAS", default=None)
    """Whether emoji comparison is available."""

    supports_scan_qr_code: Optional[bool] = FieldInfo(alias="supportsScanQRCode", default=None)
    """Whether QR code verification is available."""

    verification_id: Optional[str] = FieldInfo(alias="verificationID", default=None)
    """Verification ID to pass in verification action paths."""


class AppStatusResponse(BaseModel):
    e2ee: E2ee
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

    matrix: Optional[Matrix] = None
    """Signed-in account details. Omitted until sign-in is complete."""

    verification: Optional[Verification] = None
    """Trusted-device verification progress."""
