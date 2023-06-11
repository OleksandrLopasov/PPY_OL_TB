# router = APIRouter(
#     prefix="/players",
#     tags=["players"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not Found"}}
# )
#
#
# @router.get("/")
# async def read_players():
#     users = session.query(Player).all()
#     return users
#
#
# @router.post("/addPlayer")
# async def create_player(player: Player):
#     session.add(player)
#     return player
#
#
# @router.put(
#     "/updatePlayer={player_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}}
# )
# async def update_user(player_id: int, player: Player):
#     player_to_update = session.query(Player).filter(Player.id_player == player_id).first()
#     if player_to_update:
#         if player.Username:
#             player_to_update.Username = player.Username
#         if player.Password:
#             player_to_update.Password = player.Password
#         return player_to_update
#     return "User not found"
#
#
# @router.delete(
#     "/deletePlayer={player_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}}
# )
# async def delete_user(player_id: int):
#     user_to_delete = session.query(Player).filter(Player.id_player == player_id).first()
#     if user_to_delete:
#         session.delete(user_to_delete)
#         return "User deleted successfully"
#     return "User not found"
