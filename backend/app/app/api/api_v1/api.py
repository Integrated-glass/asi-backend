from fastapi import APIRouter

from app.api.api_v1.endpoints import login, entrepreneur, users, investor

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"], prefix="/login")
api_router.include_router(entrepreneur.router, tags=["entrepreneur"], prefix="/entrepreneur")
api_router.include_router(users.router, tags=["users"], prefix="/users")
api_router.include_router(investor.router, tags=["investor"], prefix="/investors")
# api_router.include_router(users.router, prefix="/users", tags=["users"])
