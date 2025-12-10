from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import MarketplaceRead, MarketplaceCreate, MarketplaceUpdate
from app.core import db_helper
from . import crud
from app.core.models import Marketplace
from .dependencies import marketplace_by_id

router = APIRouter(tags=["Marketplaces"], prefix="/marketplaces")


@router.get("/", response_model=list[MarketplaceRead])
async def get_marketplaces(session: AsyncSession = Depends(db_helper.scoped_session_dependency),):
    return await crud.get_marketplaces(session=session)


@router.get("/{marketplace_id}/", response_model=MarketplaceRead)
async def get_marketplace_by_id(
        marketplace: Marketplace = Depends(marketplace_by_id),) -> Marketplace:
    return marketplace


@router.post("/", response_model=MarketplaceRead, status_code=status.HTTP_201_CREATED)
async def create_marketplace(
        marketplace_in: MarketplaceCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
        # marketplace_in: MarketplaceCreate,
):
    return await crud.create_marketplace(session=session, marketplace_in=marketplace_in)


@router.patch("/{marketplace_id}/", response_model=MarketplaceRead)
async def update_marketplace(
        marketplace_update: MarketplaceUpdate,
        marketplace: Marketplace = Depends(marketplace_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_marketplace(
        session=session,
        marketplace=marketplace,
        marketplace_update=marketplace_update,
    )


@router.delete("/{marketplace_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_marketplace(
        marketplace: Marketplace = Depends(marketplace_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    return await crud.delete_marketplace(session=session, marketplace=marketplace)