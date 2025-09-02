from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, HttpUrl
from typing import Annotated, Optional


class SourceBase(BaseModel):
    name: Annotated[str, MinLen(3), MaxLen(255)]
    slug: Annotated[str, MinLen(3), MaxLen(255)]
    url: HttpUrl
    description: Optional[str] = None
    picture: Optional[str] = None


class SourceCreate(SourceBase):
    pass


class SourceRead(BaseModel):
    id: int

    class Config: # позволяет делать SourceRead.model_validate(sa_obj)
        from_attributes = True