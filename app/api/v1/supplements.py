from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.sql.annotation import Annotated

from app.core import db_helper
from app.core.schemas.supplement import SupplementRead, SupplementCreate
from app.crud import supplements as supplements_crud
router = APIRouter(tags=["Supplements"])


@router.get("", response_model=list[SupplementRead])
async def get_supplements(
        # session: AsyncSession = Depends(db_helper.session_getter)
        # второй вариант записи
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    supplements = await supplements_crud.get_all_supplements(session=session)
    return supplements

@router.post("", response_model=SupplementRead)
async def create_supplement(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        supplement_create: SupplementCreate,
):
    supplement = await supplements_crud.create_supplement(
        session=session,
        supplement_create=supplement_create,
    )
    return supplement