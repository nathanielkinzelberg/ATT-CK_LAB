import sys
import os
from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from shared.logging_config import get_logger
from agent.auth import verify_token

load_dotenv()

logger = get_logger("agent")

app = FastAPI(title="ATT&CK-Pi Lab Agent")


@app.get("/health")
async def health():
    """Returns the agent's status."""
    logger.info("Health check requested")
    return {"status": "ok", "agent": "ATT&CK-Pi Lab"}


@app.get("/techniques")
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
