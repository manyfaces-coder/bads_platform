from sqlalchemy import String, ForeignKey

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .mixins.int_id_pk import IntIdPKMixin


class Category(IntIdPKMixin, Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(255), unique=True)
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    # parent_id - делает категорию иерархической — то есть категория может быть «дочерней» у другой категории
    parent_id: Mapped[int|None] = mapped_column(
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True,
    )

    # создание отношения "родитель"
    parent: Mapped["Category"] = relationship(
        "Category",
        # remote_side нужен, чтобы SQLAlchemy понял, к какой стороне относится parent
        remote_side="Category.id", # указывает, что parent_id -> id
        back_populates="children",
    )

    # отношение "дети"
    children: Mapped[list["Category"]] = relationship(
        "Category",
        back_populates="parent",
        passive_deletes=True,
    )