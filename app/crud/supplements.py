from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import Supplement
from app.core.schemas.supplement import SupplementCreate


async def get_all_supplements(
        session: AsyncSession,
) -> Sequence[Supplement]:
    stmt = select(Supplement).order_by(Supplement.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_supplement(
        session: AsyncSession,
        supplement_create: SupplementCreate,
) -> Supplement:
    supplement = Supplement(**supplement_create.model_dump())
    session.add(supplement)
    await session.commit()
    await session.refresh(supplement)
    return supplement