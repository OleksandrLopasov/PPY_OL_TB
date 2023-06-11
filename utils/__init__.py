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
