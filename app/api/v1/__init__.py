from fastapi import APIRouter

from app.core.config import settings

from .supplements import router as supplements_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    supplements_router,
    prefix=settings.api.v1.supplements,
)