from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core import db_helper
from app.core.models import Manufacturer

from . import crud

async def manufacturer_by_id(manufacturer_id: Annotated[int, Path],
                       session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                       ) -> Manufacturer:
    manufacturer = await crud.get_manufacturer(manufacturer_id=manufacturer_id, session=session)
    if manufacturer is not None:
        return manufacturer
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Manufacturer {manufacturer_id} not found",
    )