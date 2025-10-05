from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models import Category
from .schemas import CategoryCreate, CategoryUpdate

async def get_categories(session: AsyncSession) -> list[Category]:
    stmt = select(Category).order_by(Category.id)
    result: Result = await session.execute(stmt)
    categories = result.scalars().all()
    return list(categories)


async def get_category(session: AsyncSession, category_id: int) -> Category | None:
    return await session.get(Category, category_id)


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