import os
import time
from shared.base import AttackTechnique
from shared.models import TechniqueResult
from shared.logging_config import get_logger

logger = get_logger("t1087")

class AccountDiscovery(AttackTechnique):
    """T1087 - Discovers local user accounts on the target machine."""
    technique_id = "T1087"
    technique_name = "Account Discovery"
    tactic = "Discovery"
    description = "Lists local user accounts including username, UID, home directory, and shell."
    supported_platforms = ["linux"]
    risk_level = "low"
    