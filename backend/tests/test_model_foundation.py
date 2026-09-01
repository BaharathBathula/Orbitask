import uuid
from collections.abc import Callable
from datetime import UTC, datetime
from typing import cast

from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.base import TimestampMixin, UUIDPrimaryKeyMixin, utc_now
from app.models.enums import (
    ActionStatus,
    ApprovalStatus,
    IntegrationProvider,
    PolicyDecision,
    RiskLevel,
    TaskStatus,
)


class FoundationModel(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "foundation_model"

    name: Mapped[str] = mapped_column(nullable=False)


def test_uuid_primary_key_generates_uuid_values() -> None:
    id_factory = cast(Callable[[object], uuid.UUID], FoundationModel.__table__.c.id.default.arg)

    generated_id = id_factory(None)

    assert isinstance(generated_id, uuid.UUID)


def test_timestamp_defaults_are_timezone_aware_utc() -> None:
    created_at_factory = cast(
        Callable[[object], datetime],
        FoundationModel.__table__.c.created_at.default.arg,
    )
    updated_at_factory = cast(
        Callable[[object], datetime],
        FoundationModel.__table__.c.updated_at.default.arg,
    )

    created_at = created_at_factory(None)
    updated_at = updated_at_factory(None)

    assert created_at.tzinfo is UTC
    assert updated_at.tzinfo is UTC


def test_utc_now_returns_timezone_aware_utc_timestamp() -> None:
    timestamp = utc_now()

    assert timestamp.tzinfo is UTC


def test_enum_values_are_stable_lowercase_strings() -> None:
    enum_classes = (
        TaskStatus,
        ActionStatus,
        ApprovalStatus,
        PolicyDecision,
        RiskLevel,
        IntegrationProvider,
    )

    for enum_class in enum_classes:
        for member in enum_class:
            assert member.value == member.name.lower()
            assert enum_class(member.value) is member


def test_model_is_registered_with_canonical_metadata() -> None:
    assert FoundationModel.metadata is Base.metadata
    assert Base.metadata.tables["foundation_model"] is FoundationModel.__table__
