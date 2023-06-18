from typing import List

from pydantic import BaseModel


# Pack
class PackBase(BaseModel):
    packname: str
    id_user: int


class PackRead(PackBase):
    id_pack: int
    truths: List[int] = []
    dares: List[int] = []


class PackCreate(PackBase):
    pass


# Truth
class TruthBase(BaseModel):
    text: str
    id_user: int


class TruthRead(TruthBase):
    id_pack: List[int] = []

    class Config:
        orm_mode = True


class TruthCreate(TruthBase):
    id_pack: int


# Dare
class DareBase(BaseModel):
    text: str
    id_user: int


class DareCreate(DareBase):
    id_pack: int


class DareRead(DareBase):
    id_pack: List[int] = []

    class Config:
        orm_mode = True
