from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core import db_helper
from app.core.models import Category
from . import crud
from .schemas import CategoryCreate, CategoryRead, CategoryUpdate
from .dependencies import category_by_id

router = APIRouter(tags=["Categories"], prefix="/categories")


@router.get("/", response_model=list[CategoryRead])
async def get_categories(session: AsyncSession = Depends(db_helper.scoped_session_dependency),):
    return await crud.get_categories(session=session)


@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
async def create_category(category_in: CategoryCreate,
                          session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                          ):
    return await crud.create_category(session=session, category_in=category_in)


@router.get("/{category_id}/", response_model=CategoryRead)
async def get_category(category: Category = Depends(category_by_id), ) -> Category:
    return category


@router.patch("/{category_id}/", response_model=CategoryRead)
async def update_category(
        category_update: CategoryUpdate,
        category: Category = Depends(category_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),):
    return await crud.update_category(
        session=session,
        category=category,
        category_update=category_update)


@router.delete("/{category_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
        category: Category = Depends(category_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_category(category=category, session=session)