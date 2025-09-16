from typing import Annotated
from pydantic import BaseModel
from datetime import datetime
from annotated_types import MinLen, MaxLen

class SupplementBase(BaseModel):
    # id генерируется автоматически
    name: Annotated[str, MinLen(2), MaxLen(255)]
    comment: str | None = None
    picture: str | None = None


class SupplementCreate(SupplementBase): #то, что клиент реально указывает при создании
    category_id: int | None = None
    manufacturer_id: int | None = None

    model_config = {"extra": "forbid"}

class SupplementRead(SupplementBase): #то, что клиент получает в ответе
    id: int
    category_id: int | None
    manufacturer_id: int | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SupplementUpdate(SupplementBase):
    name: Annotated[str | None, MinLen(2), MaxLen(255)] = None
    comment: str | None = None
    picture: str | None = None
    category_id: int | None = None
    manufacturer_id: int | None = None

    model_config = {"extra": "forbid"}
