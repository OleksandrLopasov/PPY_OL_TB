from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.auth.database import get_async_session
from src.auth.models import dare, pack, dare_pack
from src.auth.auth import current_user
from src.auth.database import User
from src.operations.schemas import DareCreate, DarePackCreate

dare_router = APIRouter(
    prefix="/dare",
    tags=["Dare"]
)


# select all dares
@dare_router.get("/get_dares/")
async def get_dares(user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(dare).where(dare.id_user == user.id).options(selectinload(dare.packs))
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": "Oops! Something went wrong."
        })


# select dare that contains desired task
@dare_router.get("/get_dare(s)/{text_to_search}")
async def get_dares_containing_text(text_to_search: str,
                                    session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(dare).where(dare.text.contains(text_to_search))
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


@dare_router.delete("/delete_dare/{id}")
async def delete_dare(id_dare: int,
                      user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(dare).where(dare.id_dare == id_dare)
        dareToDelete = await session.execute(query)
        await session.delete(dareToDelete)
        return {
            "status": "success",
            "data": "Successfully removed the item",
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "details": "Something went wrong!"
        })


# add dare to pack
@dare_router.post("/add_dare_to_pack")
async def add_dare_to_pack(new_dare_pack: DarePackCreate,
                           user: User = Depends(current_user),
                           session: AsyncSession = Depends(get_async_session)):
    try:
        pack_query = select(pack).filter(user.id).where(pack.id_pack == new_dare_pack.id_pack)
        pack_check = await session.execute(pack_query)
        if pack_check is None:
            raise HTTPException(status_code=404, detail={
                "status": "error",
                "data": None,
                "details": "Pack does not exist"
            })

        dare_query = select(dare).filter(user.id).where(dare.id_dare == new_dare_pack.id_dare)
        dare_check = await session.execute(dare_query)
        if dare_check is None:
            raise HTTPException(status_code=404, detail={
                "status": "error",
                "data": None,
                "details": "Dare does not exist"
            })

        stmt = insert(dare_pack).values(**new_dare_pack.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "details": "Something went wrong!"
        })
