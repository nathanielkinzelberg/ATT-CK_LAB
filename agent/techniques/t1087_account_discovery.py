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

    def run(self) -> TechniqueResult:
        """Execute T1087 and return a list of local user accounts."""
        logger.info("Starting T1087 - Account Discovery")
        start_time = time.time()
        errors = []
        results = {}

        try:
            results["accounts"] = self._parse_passwd()
            results["account_count"] = len(results["accounts"])
        except Exception as e:
            errors.append(f"account discovery failed: {str(e)}")

        duration_ms = int((time.time() - start_time) * 1000)
        success = len(errors) == 0

        logger.info(f"T1087 completed - success={success}, duration={duration_ms}ms")

        return TechniqueResult(
            technique_id=self.technique_id,
            technique_name=self.technique_name,
            tactic=self.tactic,
            host=os.uname().nodename,
            success=success,
            results=results,
            errors=erros,
            duration_ms=duration_ms,
        )