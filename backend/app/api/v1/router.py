from fastapi import APIRouter
from fastapi.responses import JSONResponse

api_v1_router = APIRouter()

@api_v1_router.get("/health", tags=["Health"])
async def health():
    """
    Health check endpoint
    """

    return JSONResponse({"status": "ok"})