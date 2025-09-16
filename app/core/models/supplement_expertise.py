from datetime import datetime
from decimal import Decimal
from sqlalchemy import Text, ForeignKey, String, DateTime, Numeric, CheckConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from sqlalchemy.sql import func
from .mixins.timestamp import TimestampMixin
from .mixins.int_id_pk import IntIdPKMixin


# Таблица с результатами экспертиз БАДов
class SupplementExpertise(IntIdPKMixin, TimestampMixin, Base):
    __tablename__ = "supplements_expertise"

    supplement_id: Mapped[int] = mapped_column(
        ForeignKey(
            "supplements.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True, # часто фильтруем по добавке
    )
    manufacturer_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "manufacturers.id",
            ondelete="SET NULL",
        ),
        nullable=True,
        index=True,
    )
    source_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "sources.id",
            ondelete="SET NULL",
        ),
        nullable=True,
        index=True,
    )

    # --- ПРОЦЕНТНАЯ МЕТРИКА (когда есть/можно посчитать %) ---
    label_percent: Mapped[Decimal | None] = mapped_column(Numeric(5, 2), nullable=True)  # % по этикетке
    expertise_percent: Mapped[Decimal | None] = mapped_column(Numeric(5, 2), nullable=True)  # % по экспертизе

    # --- МАССА АКТИВНОГО В ГРАММАХ (когда считаем по массе) ---
    serving_size_g: Mapped[Decimal | None] = mapped_column(Numeric(10, 3), nullable=True)  # масса порции
    label_active_g: Mapped[Decimal | None] = mapped_column(Numeric(10, 3), nullable=True)  # заявлено г в-ва
    expertise_active_g: Mapped[Decimal | None] = mapped_column(Numeric(10, 3), nullable=True) # найдено г в-ва

    # --- УДЕЛЬНЫЕ ЕДИНИЦЫ (витамины/минералы, омега и т.п.) ---
    label_amount: Mapped[Decimal | None] = mapped_column(Numeric(18, 6), nullable=True)
    expertise_amount: Mapped[Decimal | None] = mapped_column(Numeric(18, 6), nullable=True)
    unit_code: Mapped[str | None] = mapped_column(String(8), nullable=True)  # 'iu' | 'mg' | 'ug' | 'g' ...


    report_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    collected_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(), # если не известно когда проводилась экспертиза
        nullable=False,
    )


    __table_args__ = (
        CheckConstraint("label_percent IS NULL OR (label_percent BETWEEN 0 AND 100)", name="ck_label_percent_0_100"),
        CheckConstraint("expertise_percent IS NULL OR (expertise_percent BETWEEN 0 AND 100)",
                        name="ck_expertise_percent_0_100"),
        # быстрые выборки истории по добавке
        Index("ix_expertise_supp_collected", "supplement_id", "collected_at"),
    )