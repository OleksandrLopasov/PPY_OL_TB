from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.database import get_async_session
from src.auth.models import truth, pack, truth_pack
from src.auth.auth import current_user
from src.auth.database import User
from src.operations.schemas import TruthCreate, TruthPackCreate

truth_router = APIRouter(
    prefix="/truth",
    tags=["Truth"]
)


# select all truths
@truth_router.get("/get_truths")
async def get_truths(user: User = Depends(current_user),
                     session: AsyncSession = Depends(get_async_session)):
    query = select(truth).where(truth.id_user == user.id)
    result = await session.execute(query)
    return result.mappings().all()


# select truth that contains desired task
@truth_router.get("")
async def get_truths_containing_text(text_to_search: str,
                                     user: User = Depends(current_user),
                                     session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(truth).where(truth.id_user == user.id).where(truth.text.contains(text_to_search))
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.scalars().all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "details": "Unauthorized user"
        })


# add truth
@truth_router.post("/add_truth")
async def add_truth(new_truth: TruthCreate,
                    user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    new_truth.id_user = user.id
    stmt = insert(truth).values(**new_truth.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


# add truth to pack
@truth_router.post("/add_dare_to_pack")
async def add_truth_to_pack(new_truth_pack: TruthPackCreate,
                            user: User = Depends(current_user),
                            session: AsyncSession = Depends(get_async_session)):
    pack_query = select(pack).where(pack.id_user == user.id).where(pack.id_pack == new_truth_pack.id_pack)
    pack_check = await session.execute(pack_query)
    if pack_check is None:
        return {"status": "Not existent pack"}

    truth_query = select(truth).where(truth.id_user == user.id).where(truth.id_truth == new_truth_pack.id_truth)
    truth_check = await session.execute(truth_query)
    if truth_check is None:
        return {"status": "Unknown dare"}

    stmt = insert(truth_pack).values(**new_truth_pack.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}\
