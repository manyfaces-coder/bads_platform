from app.core.models import Manufacturer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from .schemas import ManufacturerCreate, ManufacturerUpdate


async def get_manufacturers(session: AsyncSession) -> list[Manufacturer]:
    stmt = select(Manufacturer).order_by(Manufacturer.id)
    result: Result = await session.execute(stmt)
    manufacturers = result.scalars().all()
    return list(manufacturers)


async def get_manufacturer(
        session: AsyncSession,
        manufacturer_id: int
) -> Manufacturer | None:
    return await session.get(Manufacturer, manufacturer_id)


async def create_manufacturer(
        session: AsyncSession,
        manufacturer_in: ManufacturerCreate
) -> Manufacturer:
    # model_dump сериализует модель данных в словарь
    manufacturer = Manufacturer(**manufacturer_in.model_dump())
    session.add(manufacturer)
    await session.commit()
    return manufacturer


async def update_manufacturer(
        session: AsyncSession,
        manufacturer: Manufacturer,
        manufacturer_update: ManufacturerUpdate
) -> Manufacturer:
    # exclude_unset ужен для исключения полей, которые не были явно заданы
    for name, value in manufacturer_update.model_dump(exclude_unset=True).items():
        setattr(manufacturer, name, value)
    await session.commit()
    return manufacturer

async def delete_manufacturer(
        session: AsyncSession,
        manufacturer: Manufacturer
) -> None:
    await session.delete(manufacturer)
    await session.commit()


