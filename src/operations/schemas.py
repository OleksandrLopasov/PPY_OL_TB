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


# Shared fields for truth and dare
class ComponentBaseModel(BaseModel):
    text: str


# Truth
class TruthRead(ComponentBaseModel):
    pass

    class Config:
        orm_mode = True


class TruthCreate(ComponentBaseModel):
    id_user: int


class TruthUpdate(ComponentBaseModel):
    pass


# Dare
class DareCreate(ComponentBaseModel):
    id_user: int


class DareRead(ComponentBaseModel):
    pass

    class Config:
        orm_mode = True


class DareUpdate(ComponentBaseModel):
    pass


# Shared fields for truth_pack and dare_pack
class ComponentPackBaseModel(BaseModel):
    id_pack: int


# Truth_Pack
class TruthPackCreate(ComponentPackBaseModel):
    id_truth: int

    class Config:
        orm_mode = True


class TruthPackRead(ComponentPackBaseModel):
    id_truth: int


# Dare_Pack
class DarePackCreate(ComponentPackBaseModel):
    id_dare: int

    class Config:
        orm_mode = True


class DarePackRead(ComponentPackBaseModel):
    id_dare: int
