from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import ManufacturerRead, ManufacturerCreate, ManufacturerUpdate
from app.core import db_helper
from . import crud
from app.core.models import Manufacturer
from .dependencies import manufacturer_by_id


router = APIRouter(tags=["Manufacturers"], prefix="/manufacturers")

@router.get("/", response_model=list[ManufacturerRead])
async def get_manufacturers(session: AsyncSession = Depends(db_helper.scoped_session_dependency),):
    return await crud.get_manufacturers(session=session)

@router.post("/", response_model=ManufacturerRead, status_code=status.HTTP_201_CREATED)
async def create_manufacturer(
        manufacturer_in: ManufacturerCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_manufacturer(session=session, manufacturer_in=manufacturer_in)

@router.get("/{manufacturer_id}/", response_model=ManufacturerRead)
async def get_manufacturer(manufacturer: Manufacturer = Depends(manufacturer_by_id), ) -> Manufacturer:
    return manufacturer


@router.patch("/{manufacturer_id}/", response_model=ManufacturerRead)
async def update_manufacturer(
        manufacturer_update: ManufacturerUpdate,
        manufacturer: Manufacturer = Depends(manufacturer_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_manufacturer(
        session=session,
        manufacturer=manufacturer,
        manufacturer_update=manufacturer_update
    )

@router.delete("/{manufacturer_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_manufacturer(
        manufacturer: Manufacturer = Depends(manufacturer_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_manufacturer(session=session, manufacturer=manufacturer)
