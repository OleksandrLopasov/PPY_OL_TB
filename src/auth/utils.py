from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from src.config import SECRET

from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, DeclarativeMeta
from fastapi_users.db import SQLAlchemyBaseUserTable
from src.config import DB_HOST, DB_PASS, DB_PORT, DB_USER, DB_NAME

from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, schemas, models, exceptions
from src.auth.database import User, get_user_db

from typing import List
from sqlalchemy import MetaData, ForeignKey, String, Integer
from sqlalchemy.orm import registry, Mapped, mapped_column, relationship

from typing import Optional
from fastapi_users import schemas
