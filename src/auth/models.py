from src.auth.utils import *

metadata = MetaData()
mapper_registry = registry(metadata=metadata)


@mapper_registry.mapped_as_dataclass
class user:
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column("email")
    username: Mapped[str] = mapped_column("username")
    hashed_password: Mapped[str] = mapped_column("hashed_password")

    packs: Mapped[List["pack"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    truths: Mapped[List["truth"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    dares: Mapped[List["dare"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    is_active: Mapped[bool] = mapped_column("is_active", default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column("is_superuser", default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column("is_verified", default=False, nullable=False)


@mapper_registry.mapped_as_dataclass
class pack:
    __tablename__ = "pack"

    id_pack: Mapped[int] = mapped_column(primary_key=True)
    packname: Mapped[str] = mapped_column("packname")
    id_user: Mapped[int] = mapped_column(ForeignKey(user.id))

    truths: Mapped[List["truth"]] = relationship(
        "truth", secondary="truth_pack", back_populates="packs"
    )
    dares: Mapped[List["dare"]] = relationship(
        "dare", secondary="dare_pack", back_populates="packs"
    )

    user: Mapped["user"] = relationship(
        back_populates="packs"
    )


@mapper_registry.mapped_as_dataclass
class dare:
    __tablename__ = "dare"

    id_dare: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))
    id_pack: Mapped[int] = mapped_column(ForeignKey(pack.id_pack), nullable=True)
    id_user: Mapped[int] = mapped_column(ForeignKey(user.id))

    packs: Mapped[List["pack"]] = relationship(
        "pack", secondary="dare_pack", back_populates="dares"
    )
    user: Mapped["user"] = relationship(
        back_populates="dares"
    )


@mapper_registry.mapped_as_dataclass
class dare_pack:
    __tablename__ = "dare_pack"

    id_pack: Mapped[int] = mapped_column(Integer, ForeignKey(pack.id_pack), primary_key=True)
    id_dare: Mapped[int] = mapped_column(Integer, ForeignKey(dare.id_dare), primary_key=True)


@mapper_registry.mapped_as_dataclass
class truth:
    __tablename__ = "truth"

    id_truth: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))
    id_pack: Mapped[int] = mapped_column(ForeignKey(pack.id_pack))
    id_user: Mapped[int] = mapped_column(ForeignKey(user.id))

    packs: Mapped["pack"] = relationship(
        "pack", secondary="truth_pack", back_populates="truths"
    )
    user: Mapped["user"] = relationship(
        back_populates="truths"
    )


@mapper_registry.mapped_as_dataclass
class truth_pack:
    __tablename__ = "truth_pack"

    id_pack: Mapped[int] = mapped_column(Integer, ForeignKey(pack.id_pack), primary_key=True)
    id_truth: Mapped[int] = mapped_column(Integer, ForeignKey(truth.id_truth), primary_key=True)


