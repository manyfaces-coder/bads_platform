from pydantic import BaseModel
from typing import Annotated
from annotated_types import MinLen, MaxLen

class ManufacturerBase(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(2)]
    slug: Annotated[str, MinLen(2), MaxLen(2)]


class ManufacturerCreate(ManufacturerBase):
    pass

class ManufacturerUpdate(ManufacturerBase):
    id: int

    class Config:
        from_attributes = True