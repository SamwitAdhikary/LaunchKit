from fastapi import FastAPI
from .api.v1.router import api_v1_router
from fastapi.middleware.cors import CORSMiddleware
import logging

app = FastAPI(
    title="LaunchKit API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS Setup
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)

app.include_router(api_v1_router)
logging.basicConfig(level=logging.INFO)