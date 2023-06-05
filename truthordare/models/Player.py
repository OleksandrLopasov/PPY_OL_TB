from truthordare.utils import *


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


metadata.create_all(bind=connection.engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=connection.engine)

session = SessionLocal()
app = FastAPI()


@app.get("/players/")
async def read_players():
    users = session.query(Player).all()
    return users


@app.post("/players/")
async def create_player(player: Player):
    session.add(player)
    session.commit()
    return player


@app.put("/players/{player_id}")
async def update_user(player_id: int, player: Player):
    player_to_update = session.query(Player).filter(Player.id_player == player_id).first()
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
    user_to_delete = session.query(Player).filter(Player.id_player == player_id).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        return "User deleted successfully"
    return "User not found"
