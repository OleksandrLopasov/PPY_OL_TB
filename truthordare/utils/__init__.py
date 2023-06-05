from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, String, Integer
from sqlalchemy import select, inspect
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.sql import Select
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship
import pydantic
from typing import List
from truthordare.database import connection
from truthordare.models import Dare
from truthordare.models import Pack
from truthordare.models import Player
from truthordare.models import Truth