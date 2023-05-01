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
    idplayer: Mapped[int] = mapped_column(foreign_key=True)
    player: Mapped[Player] = relationship()


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
async def update_pack(pack_id: int, pack: Pack):
    pack_to_update = session.query(Pack).filter(Pack.idpack == pack_id).first()
    if pack_to_update:
        if pack.Name:
            pack_to_update.Name = pack.Name
        if pack.idplayer:
            pack_to_update.idplayer = pack.idplayer
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

