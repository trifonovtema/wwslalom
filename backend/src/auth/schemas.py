import uuid

from fastapi_users import schemas
from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: uuid.UUID
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None


class UserDetailsBase(BaseModel):
    user_id: uuid.UUID
    name: Optional[str] = None
    surname: Optional[str] = None
    middle_name: Optional[str] = None
    telegram: Optional[str] = None

class UserDetailsCreate(UserDetailsBase):
    pass

class UserDetailsRead(UserDetailsBase):
    pass

class UserDetailsUpdate(UserDetailsBase):
    pass