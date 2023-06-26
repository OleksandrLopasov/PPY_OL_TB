from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from src.auth.auth import auth_backend
from src.auth.database import User
from src.auth.schemas import UserRead, UserCreate
from src.auth.auth import fastapi_users
from src.auth.auth import current_user

from src.operations.truth_router import truth_router
from src.operations.dare_router import dare_router
from src.operations.pack_router import pack_router
from src.pages.pages_router import pages_router


app = FastAPI(
    title="Gamasters"
)

app.mount("/src/static", StaticFiles(directory="src/static"), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(truth_router)
app.include_router(dare_router)
app.include_router(pack_router)
app.include_router(pages_router)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"
