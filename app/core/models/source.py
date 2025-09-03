from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from .mixins.int_id_pk import IntIdPKMixin


# Источники, которые проводят исследования/отправляют БАДы на экспертизы
class Source(IntIdPKMixin,Base):

    name: Mapped[str] = mapped_column(String(255), unique=True)
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    url: Mapped[str] = mapped_column(Text, unique=True)
    picture: Mapped[str | None] = mapped_column(Text, nullable=True)
    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
        default="",
    )
