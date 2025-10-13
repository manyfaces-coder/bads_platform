from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import MinLen, MaxLen

class ManufacturerBase(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(255)]
    slug: Annotated[str, MinLen(2), MaxLen(255)]


class ManufacturerCreate(ManufacturerBase):
    model_config = {"extra": "forbid"}


class ManufacturerUpdate(ManufacturerBase):
    name: Annotated[str | None, MinLen(2), MaxLen(255)] = None
    slug: Annotated[str | None, MinLen(2), MaxLen(255)] = None

    model_config = {"extra": "forbid"} # клиент не сможет подсунуть лишние поля
                                        # настройка не наследуется от Base класса

class ManufacturerRead(ManufacturerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)