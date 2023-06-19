from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.database import get_async_session
from src.auth.models import pack
from src.auth.auth import current_user
from src.auth.database import User
from src.operations.schemas import PackCreate

pack_router = APIRouter(
    prefix="/pack",
    tags=["Pack"]
)


# select all truths
@pack_router.get("/get_packs")
async def get_packs(user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    query = select(pack).where(pack.id_user == user.id)
    result = await session.execute(query)
    return result.mappings().all()


# add truth
@pack_router.post("/add_pack")
async def add_pack(new_pack: PackCreate,
                   user: User = Depends(current_user),
                   session: AsyncSession = Depends(get_async_session)):
    new_pack.id_user = user.id
    stmt = insert(pack).values(**new_pack.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
