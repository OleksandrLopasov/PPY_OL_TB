from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.auth.database import get_async_session
from src.auth.models import dare, pack, dare_pack
from src.auth.auth import current_user
from src.auth.database import User
from src.operations.schemas import DareCreate, DarePackCreate, DareUpdate

dare_router = APIRouter(
    prefix="/dare",
    tags=["Dare"]
)


# select all dares
@dare_router.get("/get_dares/")
async def get_dares(user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    query = select(dare).where(dare.id_user == user.id).options(selectinload(dare.packs))
    result = await session.execute(query)
    dares = result.unique().scalars().all()
    return {
        "status": "success",
        "data": list(dares),
        "details": None
    }


# select dare that contains desired task
@dare_router.get("/get_dare(s)/{text_to_search}")
async def get_dares(text_to_search: str,
                    user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(dare).where(dare.id_user == user.id).where(dare.text.contains(text_to_search))
        result = await session.execute(query)
        return result.scalars().all()
    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "details": "Unauthorized user"
        })


# add dare
@dare_router.post("/add_dare")
async def add_dare(new_dare: DareCreate,
                   user: User = Depends(current_user),
                   session: AsyncSession = Depends(get_async_session)):
    try:
        new_dare.id_user = user.id
        stmt = insert(dare).values(**new_dare.dict())
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": new_dare,
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "details": "Unauthorized user"
        })


@dare_router.patch("/update_dare")
async def update_dare(new_dare: DareUpdate,
                      user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    try:
        return
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": "Unauthorized user"
        })


# add dare to pack
@dare_router.post("/add_dare_to_pack")
async def add_dare_to_pack(new_dare_pack: DarePackCreate,
                           user: User = Depends(current_user),
                           session: AsyncSession = Depends(get_async_session)):
    # pack_query = select(pack).where(pack.id_user == user.id).where(pack.id_pack == new_dare_pack.id_pack)
    # try:
    #     await session.execute(pack_query)
    # except Exception:
    #     raise HTTPException(status_code=400, detail={
    #         "status": "error",
    #         "data": None,
    #         "details": "Non-existent object"
    #     })
    #
    # dare_query = select(dare).where(dare.id_user == user.id).where(dare.id_dare == new_dare_pack.id_dare)
    # dare_check = await session.execute(dare_query)
    # if dare_check is None:
    #     return {"status": "Unknown dare"}

    stmt = insert(dare_pack).values(**new_dare_pack.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
