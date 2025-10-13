from typing import Annotated
from pydantic import BaseModel, ConfigDict
from annotated_types import MinLen, MaxLen


class CategoryBase(BaseModel):
    # id генерируется автоматически
    name: Annotated[str, MinLen(2), MaxLen(255)]
    slug: Annotated[str, MinLen(2), MaxLen(255)]


class CategoryCreate(CategoryBase):
    parent_id: int | None = None

    model_config = {"extra": "forbid"}

class CategoryRead(CategoryBase):
    id: int
    parent_id: int | None

    # нужно, чтобы Pydantic мог напрямую превращать SQLAlchemy-объекты в Pydantic-схемы
    model_config = ConfigDict(from_attributes=True)


class CategoryUpdate(CategoryBase):
    name: Annotated[str | None, MinLen(2), MaxLen(255)] = None
    slug: Annotated[str | None, MinLen(2), MaxLen(255)] = None
    parent_id: int | None = None

    model_config = {"extra": "forbid"}