from typing import List, Optional
from sqlalchemy import MetaData, ForeignKey, String, Integer, Table, Column
from sqlalchemy.orm import registry, Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class user(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column("email")
    username: Mapped[str] = mapped_column("username")
    hashed_password: Mapped[str] = mapped_column("hashed_password")

    packs: Mapped[Optional[List["pack"]]] = relationship(
        "pack", back_populates="user", cascade="all, delete-orphan"
    )
    truths: Mapped[Optional[List["truth"]]] = relationship(
        "truth", back_populates="user", cascade="all, delete-orphan"
    )
    dares: Mapped[Optional[List["dare"]]] = relationship(
        "dare", back_populates="user", cascade="all, delete-orphan"
    )

    is_active: Mapped[bool] = mapped_column("is_active", default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column("is_superuser", default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column("is_verified", default=False, nullable=False)


dare_pack = Table(
    "dare_pack",
    Base.metadata,
    Column("id_pack", ForeignKey("pack.id_pack")),
    Column("id_dare", ForeignKey("dare.id_dare")),
)


class dare(Base):
    __tablename__ = "dare"

    id_dare: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))
    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"))

    packs: Mapped[List["pack"]] = relationship(
        secondary=dare_pack, back_populates="dares"
    )
    user: Mapped["user"] = relationship(
        back_populates="dares"
    )


truth_pack = Table(
    "truth_pack",
    Base.metadata,
    Column("id_pack", ForeignKey("pack.id_pack")),
    Column("id_truth", ForeignKey("truth.id_truth")),
)


class truth(Base):
    __tablename__ = "truth"

    id_truth: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))
    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"))

    packs: Mapped["pack"] = relationship(
        secondary=truth_pack, back_populates="truths"
    )
    user: Mapped["user"] = relationship(
        back_populates="truths"
    )


class pack(Base):
    __tablename__ = "pack"

    id_pack: Mapped[int] = mapped_column(primary_key=True)
    packname: Mapped[str] = mapped_column("packname")
    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"))

    truths: Mapped[List["truth"]] = relationship(
        secondary=truth_pack, back_populates="packs"
    )
    dares: Mapped[List["dare"]] = relationship(
        secondary=dare_pack, back_populates="packs"
    )

    user: Mapped["user"] = relationship(
        back_populates="packs"
    )
