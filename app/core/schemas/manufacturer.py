from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen

class ManufacturerBase(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(255)]
    slug: Annotated[str, MinLen(2), MaxLen(255)]

    model_config = {"extra": "forbid"}

class ManufacturerCreate(ManufacturerBase):
    pass


class ManufacturerUpdate(ManufacturerBase):
    name: Annotated[str | None, MinLen(2), MaxLen(255)] = None
    slug: Annotated[str | None, MinLen(2), MaxLen(255)] = None

    model_config = {"extra": "forbid"} # клиент не сможет подсунуть лишние поля

class ManufacturerRead(ManufacturerBase):
    id: int

    class Config:
        from_attributes = True