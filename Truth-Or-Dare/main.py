# database
    # connection
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy import select, inspect
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.sql import Select
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship
import pydantic

engine = create_engine('postgresql://postgres:pass@localhost:5432')
connection = engine.connect()

    # tables

        # from connection import *
metadata = MetaData()
mapper_registry = registry(metadata=metadata)

@mapper_registry.mapped_as_dataclass
class Player:
    __tablename__ = "player"

    idplayer: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column("username")
    password: Mapped[str] = mapped_column("password")


@mapper_registry.mapped_as_dataclass
class Truth:
    __tablename__ = "truth"

    idtruth: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column("text")


@mapper_registry.mapped_as_dataclass
class Dare:
    __tablename__ = "dare"

    iddare: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column("text")


@mapper_registry.mapped_as_dataclass
class Pack:
    __tablename__ = "pack"

    idpack: Mapped[int] = mapped_column(primary_key=True)
    packname: Mapped[str] = mapped_column()
    idplayer: Mapped[int] = mapped_column(ForeignKey("player.idplayer"))

@mapper_registry.mapped_as_dataclass
class Truth_Pack:
    __tablename__ = "pack_truth"

    idpack: Mapped[int] = mapped_column(ForeignKey("pack.idpack"), primary_key=True)
    idtruth: Mapped[int] = mapped_column(ForeignKey("truth.idtruth", primary_key=True))


@mapper_registry.mapped_as_dataclass
class Dare_Pack:
    __tablename__ = "dare_pack"

    idpack: Mapped[int] = mapped_column(ForeignKey("pack.idpack"), primary_key=True)
    iddare: Mapped[int] = mapped_column(ForeignKey("dare.iddare"), primary_key=True)


metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()
app = FastAPI()

# models

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


@app.get("/truths/")
async def read_truths():
    truths = session.query(Truth).all()
    return truths


@app.post("/truths/")
async def create_truth(truth: Truth):
    session.add(truth)
    session.commit()
    return truth


@app.put("/truths/{truth_id}")
async def update_truth(truth_id: int, truth: Truth):
    truth_to_update = session.query(Truth).filter(Truth.idTruth == truth_id).first()
    if truth_to_update:
        if truth.Text:
            truth_to_update.Text = truth.Text
        session.commit()
        return truth_to_update
    return "Truth not found"


@app.delete("/truths/{truth_id}")
async def delete_truth(truth_id: int):
    truth_to_delete = session.query(Truth).filter(Truth.idTruth == truth_id).first()
    if truth_to_delete:
        session.delete(truth_to_delete)
        session.commit()
        return "Truth deleted successfully"
    raise HTTPException(
        status_code=404,
        detail=f"Truth with id {truth_id} does not exist"
    )


@app.get("/players/")
async def read_users():
    players = session.query(Player).all()
    return players


@app.post("/players/")
async def create_user(player: Player):
    session.add(player)
    session.commit()
    return player


@app.put("/players/{player_id}")
async def update_user(idplayer: int, player: Player):
    player_to_update = session.query(Player).filter(Player.idplayer == idplayer).first()
    if player_to_update:
        if player.Username:
            player_to_update.Username = player.Username
        if player.Password:
            player_to_update.Password = player.Password
        session.commit()
        return player_to_update
    return "User not found"


@app.delete("/players/{player_id}")
async def delete_user(player_id: int):
    player_to_delete = session.query(Player).filter(Player.idplayer == player_id).first()
    if player_to_delete:
        session.delete(player_to_delete)
        session.commit()
        return "Player deleted successfully"
    raise HTTPException(
        status_code=404,
        detail=f"Truth with id {player_id} does not exist"
    )

@app.get("/dare-packs/")
async def read_dare_packs():
    dare_packs = session.query(Dare_Pack).all()
    return dare_packs


@app.post("/dare-packs/")
async def create_dare_pack(dare_pack: Dare_Pack):
    session.add(dare_pack)
    session.commit()
    return dare_pack


@app.put("/dare-packs/{dare_id}/{pack_id}")
async def update_dare_pack(dare_id: int, pack_id: int, dare_pack: Dare_Pack):
    dare_pack_to_update = session.query(Dare_Pack).filter(Dare_Pack.idDare == dare_id, Dare_Pack.idPack == pack_id).first()
    if dare_pack_to_update:
        if dare_pack.idDare:
            dare_pack_to_update.idDare = dare_pack.idDare
        if dare_pack.idPack:
            dare_pack_to_update.idPack = dare_pack.idPack
        session.commit()
        return dare_pack_to_update
    raise HTTPException(
        status_code=404,
        detail=f"Dare with id {dare_id} does not exist"
    )


@app.delete("/dare-packs/{dare_id}/{pack_id}")
async def delete_dare_pack(dare_id: int, pack_id: int):
    dare_pack_to_delete = session.query(Dare_Pack).filter(Dare_Pack.idDare == dare_id, Dare_Pack.idPack == pack_id).first()
    if dare_pack_to_delete:
        session.delete(dare_pack_to_delete)
        session.commit()
        return "Dare pack deleted successfully"
    return "Dare pack not found"

@app.get("/truth-packs/")
async def read_truth_packs():
    truth_packs = session.query(Truth_Pack).all()
    return truth_packs


@app.post("/truth-packs/")
async def create_truth_pack(truth_pack: Truth_Pack):
    session.add(truth_pack)
    session.commit()
    return truth_pack


@app.put("/truth-packs/{truth_id}/{pack_id}")
async def update_truth_pack(truth_id: int, pack_id: int, truth_pack: Truth_Pack):
    truth_pack_to_update = session.query(Truth_Pack).filter(Truth_Pack.idTruth == truth_id, Truth_Pack.idPack == pack_id).first()
    if truth_pack_to_update:
        if truth_pack.idTruth:
            truth_pack_to_update.idTruth = truth_pack.idTruth
        if truth_pack.idPack:
            truth_pack_to_update.idPack = truth_pack.idPack
        session.commit()
        return truth_pack_to_update
    return "Truth pack not found"


@app.delete("/truth-packs/{truth_id}/{pack_id}")
async def delete_truth_pack(truth_id: int, pack_id: int):
    truth_pack_to_delete = session.query(Truth_Pack).filter(Truth_Pack.idTruth == truth_id, Truth_Pack.idPack == pack_id).first()
    if truth_pack_to_delete:
        session.delete(truth_pack_to_delete)
        session.commit()
        return "Truth pack deleted successfully"
    return "Truth pack not found"

