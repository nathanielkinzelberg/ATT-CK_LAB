import os
from fastapi import Header, HTTPException
from dotenv import load_dotenv

load_dotenv()   # Reads the .env file and loads the token into memory

API_TOKEN = os.getenv("ATTACK_PI_API_TOKEN")            # Retrieve the token from the environment variable

async def verify_token(x_api_token: str = Header(...)): # async = funcition works with FastAPI's async system
    """Check that the request includes the correct API token."""
    if x_api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")