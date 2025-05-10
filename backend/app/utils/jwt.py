import time
from typing import Optional
from jose import jwt

from ..config import settings


def create_access_token(subject: str, expires_delta: Optional[int] = None) -> str:
    to_encode = {"sub": subject}
    expire = time.time() + (expires_delta or settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_token(token: str) -> dict:
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
