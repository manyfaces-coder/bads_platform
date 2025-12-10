from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core import db_helper
from app.core.models import Marketplace

from . import crud

async def marketplace_by_id(marketplace_id: Annotated[int, Path],
                            session: AsyncSession = Depends(db_helper.scoped_session_dependency),
                            ) -> Marketplace:
    marketplace = await crud.get_marketplace_by_id(marketplace_id=marketplace_id, session=session)
    if marketplace is not None:
        return marketplace
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Marketplace {marketplace_id} not found",
    )