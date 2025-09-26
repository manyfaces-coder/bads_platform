from .base import Base
from .mixins.int_id_pk import IntIdPKMixin
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column



class Marketplace(IntIdPKMixin, Base):

    name: Mapped[str] = mapped_column(String(255), nullable=False,)
    url: Mapped[str | None] = mapped_column(Text, unique=True, nullable=True)
    logo: Mapped[str | None] = mapped_column(Text, unique=True, nullable=True)