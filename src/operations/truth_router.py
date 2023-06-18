from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.database import get_async_session
from src.auth.models import truth
from src.auth.auth import current_user
from src.auth.database import User
from src.operations.schemas import TruthRead, TruthCreate

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
    return result.all()


# select truth that contains desired task
@truth_router.get("/get_truth(s)/{text_to_search}")
async def get_truths(text_to_search: str,
                     user: User = Depends(current_user),
                     session: AsyncSession = Depends(get_async_session)):
    query = select(truth).where(truth.id_user == user.id).where(truth.text.contains(text_to_search))
    result = await session.execute(query)
    return result.all()


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
