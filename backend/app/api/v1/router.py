from fastapi import APIRouter
from .endpoints import auth
from fastapi.responses import JSONResponse

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_v1_router.get("/health", tags=["Health"])(lambda: JSONResponse({"status": "ok"}))