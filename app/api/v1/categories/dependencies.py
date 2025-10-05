from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models import db_helper, Category

from . import crud

async def category_by_id(category_id: Annotated[int, Path],
                       session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                       ) -> Category:
    category = await crud.get_category(category_id=category_id, session=session)
    if category is not None:
        return category
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Category {category_id} not found",
    )