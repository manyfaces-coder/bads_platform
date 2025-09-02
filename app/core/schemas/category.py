from typing import Annotated
from pydantic import BaseModel
from annotated_types import MinLen, MaxLen


class CategoryBase(BaseModel):
    # id генерируется автоматически
    name: Annotated[str, MinLen(2), MaxLen(255)]
    slug: Annotated[str, MinLen(2), MaxLen(255)]


class CategoryCreate(CategoryBase):
    parent_id: int | None = None

class CategoryRead(CategoryBase):
    id: int
    parent_id: int | None = None

    class Config: # нужно, чтобы Pydantic мог напрямую превращать SQLAlchemy-объекты в Pydantic-схемы
        from_attributes = True

