"""FastAPI application factory."""

from fastapi import FastAPI

from specwright.api.health import router as health_router
from specwright.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version="0.1.0")
    app.include_router(health_router)
    return app


app = create_app()
