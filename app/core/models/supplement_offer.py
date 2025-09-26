from .base import Base
from sqlalchemy import ForeignKey, Text, Numeric, UniqueConstraint, DateTime
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from .mixins.int_id_pk import IntIdPKMixin
from .mixins.timestamp import TimestampMixin
from datetime import datetime



# Таблица с ссылкой на БАДы в магазинах/маркетплейсах для примерного сравнения цен
class SupplementOffer(IntIdPKMixin, TimestampMixin, Base):

    supplement_id: Mapped[int] = mapped_column(
        ForeignKey("supplements.id", ondelete="SET NULL"), nullable=False, index=True,
    )
    marketplace_id: Mapped[int] = mapped_column(
        ForeignKey("marketplaces.id", ondelete="SET NULL"), nullable=True, index=True,
    )
    url: Mapped[str] = mapped_column(Text, unique=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=True)
    last_seen_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    #бизнесовое поле: "мы в последний раз видели этот оффер на сайте/через API"

    __table_args__ = (
        UniqueConstraint("supplement_id", "marketplace_id", name="uq_offer_supplement_marketplace"),
    )