import sys
import os
from fastapi import FastAPI, Depends
from shared.logging_config import get_logger

load_dotenv()  # Load environment variables from .env file

logger = get_logger("agent")  # Create a logger for this module
