from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI
from app.api.router import router
from app.core.config import settings
from app.core.logging import configure_logging


configure_logging(settings.log_level)

logger = structlog.get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logger.info(
        "application_starting",
        app_name=settings.app_name,
        environment=settings.environment,
    )

    yield

    logger.info(
        "application_stopping",
        app_name=settings.app_name,
    )


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    debug=settings.debug,
    lifespan=lifespan,
)


app.include_router(
    router,
    prefix=settings.api_v1_prefix,
)


@app.get("/", tags=["System"])
async def root() -> dict[str, str]:
    return {
        "service": settings.app_name,
        "status": "running",
    }
