from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.database import get_async_session
from src.auth.models import dare
from src.auth.auth import current_user
from src.auth.database import User
from src.operations.schemas import DareCreate

dare_router = APIRouter(
    prefix="/dare",
    tags=["Dare"]
)


# select all truths
@dare_router.get("/get_dares")
async def get_dares(user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    query = select(dare).where(dare.id_user == user.id)
    result = await session.execute(query)
    return result.all()


# select truth that contains desired task
@dare_router.get("/get_dare(s)/{text_to_search}")
async def get_dares(text_to_search: str,
                    user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    query = select(dare).where(dare.id_user == user.id).where(dare.text.contains(text_to_search))
    result = await session.execute(query)
    return result.all()


# add dare
@dare_router.post("/add_dare")
async def add_dare(new_dare: DareCreate,
                   user: User = Depends(current_user),
                   session: AsyncSession = Depends(get_async_session)):
    new_dare.id_user = user.id
    stmt = insert(dare).values(**new_dare.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
