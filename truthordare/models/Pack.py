from truthordare.utils import *

metadata = MetaData()
mapper_registry = registry(metadata=metadata)


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


metadata.create_all(bind=connection.engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=connection.engine)

session = SessionLocal()
app = FastAPI()


@app.get("/packs/")
async def read_packs():
    packs = session.query(Pack).all()
    return packs


@app.post("/packs/")
async def create_pack(pack: Pack):
    session.add(pack)
    session.commit()
    return pack


@app.put("/packs/{pack_id}")
async def update_pack(pack_id: int, new_name: str):
    pack_to_update = session.query(Pack).filter(Pack.idpack == pack_id).first()
    if pack_to_update:
        pack_to_update.Name = new_name
        session.commit()
        return pack_to_update
    raise HTTPException(
        status_code=404,
        detail=f"Pack with id {pack_id} does not exist"
    )


@app.delete("/packs/{pack_id}")
async def delete_pack(pack_id: int):
    pack_to_delete = session.query(Pack).filter(Pack.idPack == pack_id).first()
    if pack_to_delete:
        session.delete(pack_to_delete)
        session.commit()
        return "Pack deleted successfully"
    raise HTTPException(
        status_code=404,
        detail=f"Pack with id {pack_id} does not exist"
    )
