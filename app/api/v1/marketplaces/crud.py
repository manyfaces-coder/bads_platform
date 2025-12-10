from app.core.models import Marketplace
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import MarketplaceCreate, MarketplaceUpdate
from app.api.v1.base_crud import get_rows, get_row_by_id, create_record



async def get_marketplaces(
        session: AsyncSession
) -> list[Marketplace]:
    return await get_rows(session, Marketplace)


async def get_marketplace_by_id(
        session: AsyncSession,
        marketplace_id: int
) -> Marketplace | None:
    return await get_row_by_id(session, Marketplace, marketplace_id)


async def create_marketplace(
        session: AsyncSession,
        marketplace_in: MarketplaceCreate,
) -> Marketplace:
    return await create_record(session, Marketplace, marketplace_in)


async def update_marketplace(
        session: AsyncSession,
        marketplace: Marketplace,
        marketplace_update: MarketplaceUpdate,
) -> Marketplace:
    for name, value in marketplace_update.model_dump(exclude_unset=True).items():
        setattr(marketplace, name, value)
    await session.commit()
    return marketplace


async def delete_marketplace(
        session: AsyncSession,
        marketplace: Marketplace,
) -> None:
    await session.delete(marketplace)
    await session.commit()