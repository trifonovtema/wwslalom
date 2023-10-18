from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.orm import DeclarativeMeta, declarative_base, sessionmaker, Mapped, mapped_column, declared_attr
from sqlalchemy import String, ForeignKey
from fastapi_users_db_sqlalchemy.generics import GUID
import uuid

Base: DeclarativeMeta = declarative_base()

UUID_ID = uuid.UUID


class User(SQLAlchemyBaseUserTableUUID, Base):
    __table_args__ = {"schema": "wwslalom"}


class UserDetails(Base):
    __table_args__ = {"schema": "wwslalom"}
    __tablename__ = "user_details"

    user_id: Mapped[UUID_ID] = mapped_column(GUID, ForeignKey("wwslalom.user.id", ondelete="cascade"), index=True,
                                             nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=1000), index=True, nullable=True)
    surname: Mapped[str] = mapped_column(String(length=1000), index=True, nullable=True)
    middle_name: Mapped[str] = mapped_column(String(length=1000), index=True, nullable=True)
    telegram: Mapped[str] = mapped_column(String(length=1000), index=True, nullable=True)

