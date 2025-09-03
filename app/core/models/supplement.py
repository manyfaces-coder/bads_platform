from datetime import datetime

from .base import Base
from sqlalchemy import ForeignKey, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .mixins.int_id_pk import IntIdPKMixin
from .mixins.timestamp import TimestampMixin


# БАД
class Supplement(IntIdPKMixin, TimestampMixin, Base):
    # id, created_at и updated_at генерируется автоматически
    name: Mapped[str] = mapped_column(unique=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True,
    )
    manufacturer_id: Mapped[int] = mapped_column(
        ForeignKey("manufacturers.id", ondelete="SET NULL"),
        nullable=True,
    )
    comment: Mapped[str | None] = mapped_column(Text, nullable=True, default="",)
    picture: Mapped[str | None] = mapped_column(Text, nullable=True)




# id              SERIAL PRIMARY KEY
# name            TEXT NOT NULL
# category_id     INT NOT NULL REFERENCES category(id)
# manufacturer_id INT NULL REFERENCES manufacturer(id)
# comment         TEXT NULL                     -- ручные заметки по продукту
# created_at      TIMESTAMP NOT NULL DEFAULT now()
# updated_at      TIMESTAMP NOT NULL DEFAULT now()