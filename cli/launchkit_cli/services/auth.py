import keyring
from typing import Optional
from .api import APIClient

KEYRING_SERVICE = "launchkit-cli"
KEYRING_TOKEN_KEY = "access_token"

class AuthService:
    def __init__(self, api_base_url: str):
        self.api = APIClient(api_base_url)

    def login(self, email: str, password: str) -> str:
        """
        Calls the backend /auth/login endpoint, stores the access token in the keyring, and returns the token
        """
        resp = self.api.post("/auth/login", json={"email": email, "password": password})
        resp.raise_for_status()
        data = resp.json()
        token = data.get("access_token")
        if not token:
            raise RuntimeError("No access_token in response")
        keyring.set_password(KEYRING_SERVICE, KEYRING_TOKEN_KEY, token)
        return token
    
    def get_stored_token(self) -> Optional[str]:
        """
        Retrieve the stored access token (if any).
        """
        return keyring.get_password(KEYRING_SERVICE, KEYRING_TOKEN_KEY)