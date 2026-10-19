import os
import time
from shared.base import AttackTechnique
from shared.models import TechniqueResult
from shared.logging_config import get_logger

logger = get_logger("t1057")

class ProcessDiscovery(AttackTechnique):
    """T1057 - Discovers running processes on the target machine."""
    technique_id = "T1057"
    technique_name = "Process Discovery"
    tactic = "Discovery"
    description = "Lists running processes including PID, name, and owner."
    supported_platforms = ["linux"]
    risk_level = "low"

    def run(self) -> TechniqueResult
        """Execute T1057 and return a list of running processes."""
        logger.info("Starting T1057 - Process Discovery")
        start_time = time.time()
        errors = []
        results = {}

        try:
            results["processes"] = selt._get_processes()
            results["process_count"] = len(results["processes"])
        except Exception as e:
            errors.append(f"process discovery failed: {str(e)}")

        duration_ms = int((time.time() - start_time) * 1000)
        success = len(errors) == 0

        logger.info(f"T1057 completed - success={success}, duration = {duration_ms}ms")

        return TechniqueResult(
            technique_id=self.technique_id,
            technique_name=self.technique_name
            tactic=self.tactic,
            host=os.uname().nodename,
            success=success,
            results=results,
            errors=errors,
            duration_ms=duration_ms,
        )

    def _get_processes(self) -> list:
        """Read running processes from /proc."""
