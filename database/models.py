from datetime import datetime
import enum

from sqlalchemy import Enum, ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Engine(enum.Enum):
    diesel = 'diesel'
    electric = 'electric'
    gasoline = 'gasoline'


class Base(DeclarativeBase):
    pass


class Car(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    brand: Mapped[str] = mapped_column(String(255))
    price: Mapped[float]
    engine_type: Mapped[Enum] = mapped_column(Enum(Engine), nullable=False)


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    orders: Mapped["Order"] = relationship(back_populates="user")


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    creation_date: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("cars.id"))
    user: Mapped["User"] = relationship(back_populates="orders")
