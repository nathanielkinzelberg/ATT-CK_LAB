import sys
import os
from fastapi import FastAPI, Depends
from shared.logging_config import get_logger

load_dotenv()                 # Load environment variables from .env file

logger = get_logger("agent")  # Create a logger for this module

app = FastAPI(title="ATT&CK-Pi Lab Agent")              # creates web server

@app.get("/health")           # Tells FastAPI "when someone sends a GET request to /health, run this function"
async def health():
    """Returns the agent's status"""
    logger.info("Health check requested")
    return {"status": "ok", "agent": "ATT&CK-Pi Lab"}   # Sends back JSON response