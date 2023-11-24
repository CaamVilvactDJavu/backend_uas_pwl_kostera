from sqlalchemy import Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base


class Kost(Base):
    __tablename__ = "kost"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    specification: Mapped[str] = mapped_column(Text, nullable=True)
    rule: Mapped[str] = mapped_column(Text, nullable=True)
    address: Mapped[str] = mapped_column(Text, nullable=True)
    facility: Mapped[str] = mapped_column(Text, nullable=True)
    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[str] = mapped_column(DateTime)
    updated_at: Mapped[str] = mapped_column(DateTime)
