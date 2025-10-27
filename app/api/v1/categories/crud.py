
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models import Category
from .schemas import CategoryCreate, CategoryUpdate
from app.api.v1.base_crud import get_rows, get_row_by_id



async def get_categories(session: AsyncSession) -> list[Category]:
    return await get_rows(session, Category)


async def get_category(
        session: AsyncSession,
        category_id: int
) -> Category | None:
    return await get_row_by_id(session, model=Category, id=category_id)


async def create_category(session: AsyncSession, category_in: CategoryCreate) -> Category:
    category = Category(**category_in.model_dump())
    session.add(category)
    # await session.refresh(category)  # подтянет id
    await session.commit()
    return category


async def update_category(session: AsyncSession,
                          category: Category,
                          category_update: CategoryUpdate) -> Category:
    for name, value in category_update.model_dump(exclude_unset=True).items():
        setattr(category, name, value)
    await session.commit()
    return category


async def delete_category(session: AsyncSession, category: Category) -> None:
    await session.delete(category)
    await session.commit()