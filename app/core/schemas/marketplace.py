from pydantic import BaseModel, HttpUrl
from typing import Annotated
from annotated_types import MinLen, MaxLen

class MarketplaceBase(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(255)]
    url: HttpUrl | None = None
    logo: str | None = None


class MarketplaceCreate(MarketplaceBase):
    model_config = {"extra": "forbid"}


class MarketplaceRead(MarketplaceBase):
    id: int

    # Pydantic v1
    # class Config: # позволяет делать SourceRead.model_validate(sa_obj)
    #     from_attributes = True

    #Pydantic v2
    model_config = {"from_attributes": True}


class MarketplaceUpdate(MarketplaceBase):
    name: Annotated[str | None, MinLen(2), MaxLen(255)] = None

    model_config = {"extra": "forbid"}