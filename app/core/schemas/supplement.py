from pydantic import BaseModel


class SupplementBase(BaseModel):
    # id генерируется автоматически
    name: str


class SupplementCreate(SupplementBase):
    pass

class SupplementRead(SupplementBase):
    id: int