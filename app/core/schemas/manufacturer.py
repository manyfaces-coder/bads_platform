from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen

class ManufacturerBase(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(255)]
    slug: Annotated[str, MinLen(2), MaxLen(255)]


class ManufacturerCreate(ManufacturerBase):
    pass

class ManufacturerRead(ManufacturerBase):
    id: int

    class Config:
        from_attributes = True