from sqlalchemy import select, inspect
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.sql import Select
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, create_engine
from sqlalchemy.orm import registry, relationship, sessionmaker
import pydantic
from typing import List, Annotated
from models import Dare
from models import Pack
from models import Player
from models import Truth
from main import *
from fastapi import APIRouter, Depends, HTTPException, FastAPI, Header
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy import Boolean
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeMeta, declarative_base, Mapped, mapped_column
