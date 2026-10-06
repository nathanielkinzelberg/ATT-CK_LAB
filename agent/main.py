import sys
import os
from fastapi import FastAPI, Depends   # FastAPI creates the server, Depends attaches checks to endpoints
from dotenv import load_dotenv         # loads the .env file into memory
from shared.logging_config import get_logger  # shared logging setup from Phase 1
from agent.auth import verify_token    # our token check function from auth.py

load_dotenv()  # reads .env and makes ATTACK_PI_API_TOKEN available to os.getenv()

logger = get_logger("agent")  # creates a logger named "agent" — shows up in every log line

app = FastAPI(title="ATT&CK-Pi Lab Agent")  # creates the web server


@app.get("/health")  # no auth required — controller needs to check health without a token
async def health():
    """Returns the agent's status."""
    logger.info("Health check requested")
    return {"status": "ok", "agent": "ATT&CK-Pi Lab"}


@app.get("/techniques")  # auth required — Depends(verify_token) runs the token check first
async def list_techniques(verified=Depends(verify_token)):
    """Returns the list of supported ATT&CK techniques."""
    logger.info("Techniques list requested")
    return {
        "techniques": [
            {
                "technique_id": "T1082",
                "technique_name": "System Information Discovery",
                "tactic": "Discovery",
                "risk_level": "low"
            },
            {
                "technique_id": "T1057",
                "technique_name": "Process Discovery",
                "tactic": "Discovery",
                "risk_level": "low"
            },
            {
                "technique_id": "T1087",
                "technique_name": "Account Discovery",
                "tactic": "Discovery",
                "risk_level": "low"
            },
            {
                "technique_id": "T1016",
                "technique_name": "System Network Configuration Discovery",
                "tactic": "Discovery",
                "risk_level": "low"
            },
            {
                "technique_id": "T1046",
                "technique_name": "Network Service Scanning",
                "tactic": "Discovery",
                "risk_level": "low"
            }
        ]
    }
