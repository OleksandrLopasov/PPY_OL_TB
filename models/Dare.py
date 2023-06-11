# router = APIRouter()
#
#
# @router.delete("/dares/deletePack={dare_id}")
# async def delete_dare(dare_id: int):
#     dare_to_delete = session.query(Dare).filter(Dare.idDare == dare_id).first()
#     if dare_to_delete:
#         session.delete(dare_to_delete)
#         return "Dare deleted successfully"
#     raise HTTPException(
#         status_code=404,
#         detail=f"Dare with id {dare_id} does not exist"
#     )
