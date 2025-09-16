from pydantic import BaseModel, HttpUrl
from typing import Annotated
from decimal import Decimal
from datetime import datetime


class SupplementExpertiseBase(BaseModel):
    manufacturer_id: int | None = None
    source_id: int | None = None
    label_percent: Decimal | None = None
    expertise_percent: Decimal | None = None
    label_active_g: Decimal | None = None
    expertise_active_g: Decimal | None = None
    label_amount: Decimal | None = None
    expertise_amount: Decimal | None = None
    report_url: HttpUrl | None = None
    comment: str | None = None
    collected_at: datetime | None = None



class SupplementExpertiseCreate(SupplementExpertiseBase):
    supplement_id: int

    model_config = {"extra": "forbid"}


class SupplementExpertiseUpdate(SupplementExpertiseBase):
    model_config = {"extra": "forbid"}

class SupplementExpertiseRead(SupplementExpertiseBase):
    id: int
    supplement_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True