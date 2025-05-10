from fastapi import FastAPI
from .api.v1.router import api_v1_router

app = FastAPI(
    title="LaunchKit API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(api_v1_router, prefix="/api/v1")