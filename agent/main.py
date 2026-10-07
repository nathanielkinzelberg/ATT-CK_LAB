import sys
import os
from fastapi import FastAPI, Depends, HTTPException   # FastAPI creates the server, Depends attaches checks to endpoints
from dotenv import load_dotenv         # loads the .env file into memory
from shared.logging_config import get_logger  # shared logging setup from Phase 1
from agent.auth import verify_token    # our token check function from auth.py
from agent.techniques.t1082_system_info import SystemInfoDiscovery  # our T1082 technique implementation 

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

@app.post("/techniques/{technique_id}/execute") # technique_id comed from the URL path, e.g. /techniques/T1082/execute
async def execute_technique(technique_id: str, verified=Depends(verify_token)):
    """Execute a technique by ID and return the result."""
    logger.info(f"Execute request received for {technique_id}")

    techniques = {
        "T1082": SystemInfoDiscovery, # maps the ID to the class
    }

    if technique_id not in techniques:
        logger.warning(f"Rejected unknown technique: {technique_id}")
        raise HTTPException(status_code=404, detail=f"Technique {technique_id} not found")

    technique = techniques[technique_id]() # created an instance of the technique class
    result = technique.run() # run the technique as a dictionary

    logger.info(f"{technique_id} execution complete - success={result.success}")
    return result.to_dict() # return the result as a dictionary to the controller