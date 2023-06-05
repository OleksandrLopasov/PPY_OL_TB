from truthordare.utils import *

metadata = MetaData()
mapper_registry = registry(metadata=metadata)


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


metadata.create_all(bind=connection.engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=connection.engine)

session = SessionLocal()
app = FastAPI()


@app.delete("/dares/{dare_id}")
async def delete_dare(dare_id: int):
    dare_to_delete = session.query(Dare).filter(Dare.idDare == dare_id).first()
    if dare_to_delete:
        session.delete(dare_to_delete)
        session.commit()
        return "Dare deleted successfully"
    raise HTTPException(
        status_code=404,
        detail=f"Dare with id {dare_id} does not exist"
    )
