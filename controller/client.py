import httpx # used to make HTTP requests to the server
import os # used to access environment variables
from dotenv import load_dotenv # used to load environment variables from a .env file
from shared.logging_config import get_logger # used to get a logger instance

load_dotenv()

logger = get_logger("controller") # Create a logger instance for the controller
API_TOKEN = os.getenv("ATTACK_PI_API_TOKEN") # Retrieve the API token from environment variables