from pydantic import BaseModel, HttpUrl
from decimal import Decimal
from datetime import datetime



class SupplementOfferBase(BaseModel):
    marketplace_id: int | None = None
    url: HttpUrl | None = None
    price: Decimal | None = None
    last_seen_at: datetime | None = None


class SupplementOfferCreate(SupplementOfferBase):
    supplement_id: int

    model_config = {"extra": "forbid"}


class SupplementOfferRead(SupplementOfferBase):
    id: int
    supplement_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class SupplementOfferUpdate(BaseModel):
    # так как модель может разрастись наследуемся от BaseModel и явно указываем все поля
    supplement_id: int | None = None
    marketplace_id: int | None = None
    url: HttpUrl | None = None
    price: Decimal | None = None
    last_seen_at: datetime | None = None

    model_config = {"extra": "forbid"}
