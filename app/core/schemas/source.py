from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, HttpUrl
from typing import Annotated

# Источник, из которого берутся данные об экспертизах
class SourceBase(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(255)]
    slug: Annotated[str, MinLen(3), MaxLen(255)]
    url: HttpUrl | None = None
    description: str | None = None
    picture: str | None = None


class SourceCreate(SourceBase):
    model_config = {"extra": "forbid"}


class SourceUpdate(SourceBase):
    name: Annotated[str | None, MinLen(3), MaxLen(255)] = None
    slug: Annotated[str | None, MinLen(3), MaxLen(255)] = None
    url: HttpUrl| None = None
    description: str | None = None
    picture: str | None = None

    model_config = {"extra": "forbid"}


class SourceRead(SourceBase):
    id: int

    class Config: # позволяет делать SourceRead.model_validate(sa_obj)
        from_attributes = True