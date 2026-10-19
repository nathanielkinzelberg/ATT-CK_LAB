import httpx                                 # used to make HTTP requests to the server
import os                                    # used to access environment variables
from dotenv import load_dotenv               # used to load environment variables from a .env file
from shared.logging_config import get_logger # used to get a logger instance

load_dotenv()

logger = get_logger("controller")            # Create a logger instance for the controller
API_TOKEN = os.getenv("ATTACK_PI_API_TOKEN") # Retrieve the API token from environment variables

class AgentClient:
    """Handles all HTTP communication with the agent on the Raspberry Pi."""

    def __init__(self, host: str, port: int = 8000):
        self.base.url = f"http://{host}:{port}"     # example: http://192.168.1.101:8000
        self.headers = {"X-API-TOKEN": API_TOKEN}   # Token sent with every request
        self.timeout = 30                           # seconds before giving up on a request

    def health_check(self) -> dict:
        """Check if the Agent is alive"""
        response = httpx.get(
            f"{self.base_url}/health",
            timeout = self.timeout
        )
        return response.json()  # Returns the JSON response from the agent

    def list_techniques(self) -> dict:
        """Get the list of supported techniques from the agent."""
        response = httpx.get(
            f"{self.base_url}/techniques",
            headers = self.headers,
            timeout = self.timeout
        )
        return response.json()  # Returns the JSON response from the agent

    def execute_technique(self, technique_id: str) -> dict:
        """Request the agent to execute a specific technique."""
        response = httpx.post(
            f"{self.base_url}/techniques/{technique_id}/execute",
            headers = self.headers,
            timeout = self.timeout
        )
        return response.json()  # Returns the JSON response from the agent