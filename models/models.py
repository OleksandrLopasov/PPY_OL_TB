from utils import *

metadata = MetaData()
mapper_registry = registry(metadata=metadata)


@mapper_registry.mapped_as_dataclass
class Player:
    __tablename__ = "Player"

    id_player: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column("username")
    password: Mapped[str] = mapped_column("password")

    packs: Mapped[List["Pack"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


@mapper_registry.mapped_as_dataclass
class Pack:
    __tablename__ = "Pack"

    id_pack: Mapped[int] = mapped_column(primary_key=True)
    packname: Mapped[str] = mapped_column()
    id_player: Mapped[int] = mapped_column(ForeignKey("Player.id_player"))

    truths: Mapped[List["Truth"]] = relationship(
        "Truth", secondary="Truth_Pack", back_populates="packs", cascade="all, delete-orphan"
    )
    dares: Mapped[List["Dare"]] = relationship(
        "Dare", secondary="Dare_Pack", back_populates="packs", cascade="all, delete"
    )

    user: Mapped["Player"] = relationship(
        back_populates="packs"
    )


@mapper_registry.mapped_as_dataclass
class Dare:
    __tablename__ = "Dare"

    id_dare: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))
    id_pack: Mapped[int] = mapped_column(ForeignKey("Pack.id_pack"))

    packs: Mapped[List["Pack"]] = relationship(
        "Pack", secondary="Dare_Pack", back_populates="dares", cascade="all, delete-orphan"
    )


@mapper_registry.mapped_as_dataclass
class Dare_Pack:
    __tablename__ = "Dare_Pack"

    id_pack: Mapped[int] = mapped_column(Integer, ForeignKey("Pack.id_pack"), primary_key=True)
    id_dare: Mapped[int] = mapped_column(Integer, ForeignKey("Dare.id_dare"), primary_key=True)


@mapper_registry.mapped_as_dataclass
class Truth:
    __tablename__ = "Truth"

    id_truth: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))
    id_pack: Mapped[int] = mapped_column(ForeignKey("Pack.id_pack"))

    packs: Mapped["Pack"] = relationship(
        "Pack", secondary="Truth_Pack", back_populates="truths", cascade="all, delete-orphan"
    )


@mapper_registry.mapped_as_dataclass
class Truth_Pack:
    __tablename__ = "Truth_Pack"

    id_pack: Mapped[int] = mapped_column(Integer, ForeignKey("Pack.id_pack"), primary_key=True)
    id_truth: Mapped[int] = mapped_column(Integer, ForeignKey("Truth.id_truth", primary_key=True))


