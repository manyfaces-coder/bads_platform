from fastapi import APIRouter
from .v1 import router as router_v1
from app.core.config import settings

# from ..core.config import settings

router = APIRouter(
    prefix=settings.api.prefix
)
router.include_router(router_v1)