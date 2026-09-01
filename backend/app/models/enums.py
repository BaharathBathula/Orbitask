from enum import StrEnum


class TaskStatus(StrEnum):
    RECEIVED = "received"
    ANALYZING = "analyzing"
    PLANNING = "planning"
    VALIDATING = "validating"
    WAITING_FOR_APPROVAL = "waiting_for_approval"
    WAITING_FOR_USER = "waiting_for_user"
    EXECUTING = "executing"
    VERIFYING = "verifying"
    RETRYING = "retrying"
    PARTIALLY_COMPLETED = "partially_completed"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    EXPIRED = "expired"


class ActionStatus(StrEnum):
    PENDING = "pending"
    WAITING_FOR_APPROVAL = "waiting_for_approval"
    APPROVED = "approved"
    EXECUTING = "executing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    EXPIRED = "expired"


class ApprovalStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXPIRED = "expired"
    REVOKED = "revoked"


class PolicyDecision(StrEnum):
    ALLOW = "allow"
    REQUIRE_APPROVAL = "require_approval"
    REQUIRE_CLARIFICATION = "require_clarification"
    DENY = "deny"


class RiskLevel(StrEnum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


class IntegrationProvider(StrEnum):
    GOOGLE = "google"
    MICROSOFT = "microsoft"
    BOOKING = "booking"
    PAYMENT = "payment"
