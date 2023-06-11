# router = APIRouter(
#     prefix="/packs",
#     tags=["packs"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not Found"}},
# )
#
#
# @router.get("/")
# async def read_packs():
#     packs = session.query(Pack).all()
#     return packs
#
#
# @router.post("/add_pack")
# async def create_pack(pack: Pack):
#     session.add(pack)
#     return pack
#
#
# @router.put(
#     "/updatePack={pack_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}}
# )
# async def update_pack(pack_id: int, new_name: str):
#     pack_to_update = session.query(Pack).filter(Pack.idpack == pack_id).first()
#     if pack_to_update:
#         pack_to_update.Name = new_name
#         return pack_to_update
#     raise HTTPException(
#         status_code=404,
#         detail=f"Pack with id {pack_id} does not exist"
#     )
#
#
# @router.delete(
#     "/deletePack={pack_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}}
# )
# async def delete_pack(pack_id: int):
#     pack_to_delete = session.query(Pack).filter(Pack.idPack == pack_id).first()
#     if pack_to_delete:
#         session.delete(pack_to_delete)
#         return "Pack deleted successfully"
#     raise HTTPException(
#         status_code=404,
#         detail=f"Pack with id {pack_id} does not exist"
#     )
