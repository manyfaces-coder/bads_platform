from app.core.models import Manufacturer
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import ManufacturerCreate, ManufacturerUpdate
from app.api.v1.base_crud import get_rows, get_row_by_id


async def get_manufacturers(session: AsyncSession) -> list[Manufacturer]:
    return await get_rows(session, Manufacturer)


async def get_manufacturer(
        session: AsyncSession,
        manufacturer_id: int,
) -> Manufacturer:
    return await get_row_by_id(session, Manufacturer, manufacturer_id)


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


