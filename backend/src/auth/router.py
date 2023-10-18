from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from .schemas import UserCreate, UserRead
from database import get_db
# from .users import create_new_user, authenticate_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from users import current_active_user
from fastapi import Depends, FastAPI

from .models import User

# from db.db import create_db_and_tables

router = APIRouter()


#
# @router.post("/users", response_model=UserRead)
# def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
#     user = create_new_user(user_create=user_create, db=db)
#     return user

@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

#
# @app.post("/token", response_model=Token)
# async def login_for_access_token(
#         form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
#         db: Session = Depends(get_db)
# ):
#     user = authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
