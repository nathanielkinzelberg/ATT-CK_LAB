import platform
import socket
import time
from shared.base import AttackTechnique
from shared.models import TechniqueResult
from shared.logging_config import get_logger

logger = get_logger("t1082")  # creates a logger named "t1082" — shows up in every log line

class SystemInfoDiscovery(AttackTechnique):
    """T1082 - Collects system information from the target machine"""
    technique_id = "T1082"
    technique_name = "System Information Discovery"
    tactic = "Discovery"
    description = "Collects host, OS, kernel, architechture, and hardware information"
    supported_platforms = ["linux"]
    risk_level = "low"