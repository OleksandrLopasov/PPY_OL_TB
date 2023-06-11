# router = APIRouter(
#     prefix="/truths",
#     tags=["truths"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not Found"}}
# )
#
#
# @router.get("/")
# async def read_truths():
#     truths = session.query(Truth).all()
#     return truths
#
#
# @router.post("/addTruth")
# async def create_truth(truth: Truth):
#     session.add(truth)
#     return truth
#
#
# @router.put(
#     "/updateTruth={truth_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}}
# )
# async def update_truth(truth_id: int, truth: Truth):
#     truth_to_update = session.query(Truth).filter(Truth.idTruth == truth_id).first()
#     if truth_to_update:
#         if truth.Text:
#             truth_to_update.Text = truth.Text
#         return truth_to_update
#     return "Truth not found"
#
#
# @router.delete(
#     "/deleteTruth={truth_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}}
# )
# async def delete_truth(truth_id: int):
#     truth_to_delete = session.query(Truth).filter(Truth.idTruth == truth_id).first()
#     if truth_to_delete:
#         session.delete(truth_to_delete)
#         return "Truth deleted successfully"
#     raise HTTPException(
#         status_code=404,
#         detail=f"Truth with id {truth_id} does not exist"
#     )
