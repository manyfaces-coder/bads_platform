from .base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Supplement(Base):
    name: Mapped[str] = mapped_column(unique=True)


# id              SERIAL PRIMARY KEY
# name            TEXT NOT NULL
# category_id     INT NOT NULL REFERENCES category(id)
# manufacturer_id INT NULL REFERENCES manufacturer(id)
# comment         TEXT NULL                     -- ручные заметки по продукту
# created_at      TIMESTAMP NOT NULL DEFAULT now()
# updated_at      TIMESTAMP NOT NULL DEFAULT now()