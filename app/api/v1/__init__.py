from fastapi import APIRouter

from app.core.config import settings

# from .supplements import router as supplements_router
from .categories.views import router as categories_router
from .manufacturers.views import router as manufacturers_router
router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    categories_router
)
router.include_router(
    manufacturers_router
)