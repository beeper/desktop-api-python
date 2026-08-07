# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "LoginResponseResponse",
    "Success",
    "SuccessMatrix",
    "SuccessSession",
    "SuccessSessionE2EE",
    "SuccessSessionE2EESecrets",
    "SuccessSessionMatrix",
    "SuccessSessionVerification",
    "SuccessSessionVerificationError",
    "SuccessSessionVerificationOtherDevice",
    "SuccessSessionVerificationQr",
    "SuccessSessionVerificationSAS",
    "RegistrationRequired",
    "RegistrationRequiredCopy",
]


class SuccessMatrix(BaseModel):
    """Account credentials for first-party app setup."""

    access_token: str = FieldInfo(alias="accessToken")
    """Beeper account access token. Returned once for first-party app setup."""

    device_id: str = FieldInfo(alias="deviceID")
    """Current device ID."""

    homeserver: str
    """Beeper homeserver URL for this account."""

    user_id: str = FieldInfo(alias="userID")
    """Signed-in Beeper user ID."""


class SuccessSessionE2EESecrets(BaseModel):
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


class SuccessSessionE2EE(BaseModel):
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

    secrets: SuccessSessionE2EESecrets
    """Encrypted messaging keys available on this device."""

    secret_storage: bool = FieldInfo(alias="secretStorage")
    """Whether secure key storage is available."""

    verified: bool
    """Whether this device is trusted for encrypted messages."""

    recovery_key_generated_at: Optional[float] = FieldInfo(alias="recoveryKeyGeneratedAt", default=None)
    """Unix timestamp for when the recovery key was created."""


class SuccessSessionMatrix(BaseModel):
    """Signed-in account details. Omitted until sign-in is complete."""

    device_id: str = FieldInfo(alias="deviceID")
    """Current device ID."""

    homeserver: str
    """Beeper homeserver URL for this account."""

    user_id: str = FieldInfo(alias="userID")
    """Signed-in Beeper user ID."""


class SuccessSessionVerificationError(BaseModel):
    """Verification error details, if verification stopped."""

    code: str
    """Verification error code."""

    reason: str
    """User-facing verification error message."""


class SuccessSessionVerificationOtherDevice(BaseModel):
    """Other device participating in verification."""

    id: str
    """Other device ID."""

    name: Optional[str] = None
    """Other device display name, if known."""


class SuccessSessionVerificationQr(BaseModel):
    """QR verification data."""

    data: str
    """QR code payload to display for verification."""


class SuccessSessionVerificationSAS(BaseModel):
    """Emoji or number comparison data for verification."""

    emojis: str
    """Emoji sequence to compare on both devices."""

    decimals: Optional[str] = None
    """Number sequence to compare on both devices."""


class SuccessSessionVerification(BaseModel):
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

    error: Optional[SuccessSessionVerificationError] = None
    """Verification error details, if verification stopped."""

    other_device: Optional[SuccessSessionVerificationOtherDevice] = FieldInfo(alias="otherDevice", default=None)
    """Other device participating in verification."""

    other_user_id: Optional[str] = FieldInfo(alias="otherUserID", default=None)
    """Other Beeper user participating in verification."""

    qr: Optional[SuccessSessionVerificationQr] = None
    """QR verification data."""

    sas: Optional[SuccessSessionVerificationSAS] = None
    """Emoji or number comparison data for verification."""


class SuccessSession(BaseModel):
    """Current app sign-in and encrypted messaging setup state after sign-in."""

    e2ee: SuccessSessionE2EE
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

    matrix: Optional[SuccessSessionMatrix] = None
    """Signed-in account details. Omitted until sign-in is complete."""

    verification: Optional[SuccessSessionVerification] = None
    """Trusted device verification progress."""


class Success(BaseModel):
    matrix: SuccessMatrix
    """Account credentials for first-party app setup."""

    session: SuccessSession
    """Current app sign-in and encrypted messaging setup state after sign-in."""


class RegistrationRequiredCopy(BaseModel):
    """Copy to display during account creation."""

    submit: Literal["Continue"]
    """Submit button label."""

    terms: Literal["By continuing, you agree to the Terms of Use and acknowledge the Privacy Policy."]
    """Terms and privacy notice to show before account creation."""

    title: Literal["Choose your username"]
    """Title for the username step."""

    username_placeholder: Literal["Username"] = FieldInfo(alias="usernamePlaceholder")
    """Placeholder for the username field."""


class RegistrationRequired(BaseModel):
    copy_: RegistrationRequiredCopy = FieldInfo(alias="copy")
    """Copy to display during account creation."""

    lead_token: str = FieldInfo(alias="leadToken")
    """Registration token returned by Beeper."""

    registration_required: Literal[True] = FieldInfo(alias="registrationRequired")
    """Indicates that the user needs to create a Beeper account."""

    setup_request_id: str = FieldInfo(alias="setupRequestID")
    """Setup request ID to use when creating the account."""

    username_suggestions: Optional[List[str]] = FieldInfo(alias="usernameSuggestions", default=None)
    """Suggested usernames for the new account."""


LoginResponseResponse: TypeAlias = Union[Success, RegistrationRequired]
