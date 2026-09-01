from datetime import UTC, datetime

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["System"])
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "autonomous-ai-assistant",
        "timestamp": datetime.now(UTC).isoformat(),
    }
