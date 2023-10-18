from config import Settings
# from database import engine
# from src.utils import check_db_connected
# from src.utils import check_db_disconnected
# from fastapi import FastAPI, APIRouter
# from fastapi.staticfiles import StaticFiles
# from webapps.base import api_router as web_app_router
from auth.users import fastapi_users, auth_backend, current_active_user
from fastapi import Depends, FastAPI

from auth.models import User
from auth.schemas import UserCreate, UserRead, UserUpdate

#
def include_router(app):
    app.include_router(
        fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
    )
    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_reset_password_router(),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_verify_router(UserRead),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate),
        prefix="/users",
        tags=["users"],
    )

    @app.get("/authenticated-route")
    async def authenticated_route(user: User = Depends(current_active_user)):
        return {"message": f"Hello {user.email}!"}
#     router = APIRouter()
#     router.include_router(users_router, prefix="/users", tags=["users"])
#     app.include_router(users_router)


# def configure_static(app):
#     app.mount("/static", StaticFiles(directory="static"), name="static")




def start_application():
    app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION)
    include_router(app)
    # configure_static(app)
    return app


app = start_application()


# @app.on_event("startup")
# async def app_startup():
#     await check_db_connected()


# @app.on_event("shutdown")
# async def app_shutdown():
#     await check_db_disconnected()

