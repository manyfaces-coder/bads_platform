from typing import Any, Protocol, TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# Протокол: у модели есть поле id (int/Any важен факт наличия)
class HasId(Protocol):
    id: Any

# Тип-переменная для экземпляров моделей (может быть любой переданной моделью главное HasId)
ModelT = TypeVar("ModelT", bound=HasId)

async def get_rows(
    session: AsyncSession,
    model: type[ModelT],
    order_by: Any | None = None,
) -> list[ModelT]:
    """
    Универсальная выборка всех строк для любой модели.
    По умолчанию сортирует по model.id (если не передан order_by).
    """
    stmt = select(model)
    if order_by is None:
        # если у модели нет id — можно передать order_by явно при вызове
        order_by = getattr(model, "id")
    stmt = stmt.order_by(order_by)

    result = await session.execute(stmt)
    # scalars() — берёт именно объекты моделей, а не строки
    # .all() — превращает результат в список
    return list(result.scalars().all())


# Возвращает одну запись по её id, или None, если не найдена.
async def get_row_by_id(
        session: AsyncSession,
        model: type[ModelT],
        id: int) -> ModelT | None:
    return await session.get(model, id)
