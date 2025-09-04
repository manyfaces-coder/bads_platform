from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, HttpUrl
from typing import Annotated, Optional


class SourceBase(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(255)]
    slug: Annotated[str, MinLen(3), MaxLen(255)]
    url: HttpUrl
    description: Optional[str] = None
    picture: Optional[str] = None

    model_config = {"extra": "forbid"}

class SourceCreate(SourceBase):
    pass


class SourceUpdate(SourceBase):
    name: Annotated[str | None, MinLen(3), MaxLen(255)] = None
    slug: Annotated[str | None, MinLen(3), MaxLen(255)] = None
    url: Optional[HttpUrl] = None
    description: Optional[str] = None
    picture: Optional[str] = None

    model_config = {"extra": "forbid"}


class SourceRead(SourceBase):
    id: int

    class Config: # позволяет делать SourceRead.model_validate(sa_obj)
        from_attributes = True