import os
import time
from shared.base import AttackTechnique
from shared.models import TechniqueResult
from shared.logging_config import get_logger

logger = get_logger("t1016")

class NetworkConfigDiscoery(AttackTechnique):
    """T1016 - Discovers network configuration on the target maching."""
    technique_id = "T1016"
    technique_name = "Network Configuration Discovery"
    tactic = "Discovery"
    description = "Collects network interfaces, IP addresses, routing table, and DNS configuration"
    supported_platforms = ["linux"]
    risk_level = "low"

    def run(self) -> TechniqueResult:
        logger.info("Starting T1016 - Network Configuration Discovery")
        start_time = time.time()
        errors = []
        results = {}

        try:
            results["dns_servers"] = self.get_dns()
        except Exception as e:
            errors.append(f"dns discovery failed: {str(e)}")

        duration_ms = int((time.time() - start_time) * 1000)
        success = len(errors) == 0

        logger.info(f"T1016 completed - success={success}, duration={duration_ms}ms")

        return TechniqueResult(
            technique_id=self.technique_id,
            technique_name=self.technique_name,
            tactic=self.tactic,
            host=os.uname().nodename,
            success=success,
            results=results,
            errors=errors,
            duration_ms=duration_ms,
        )

    def _get_dns(self) -> list:
        """Read DNS server addresses from /etc/resolv.conf"""
        servers = []

        with open("/etc/resolv.conf", "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("nameserver"):
                    parts = line.split()
                    if len(parts) == 2:
                        servers.append(parts[1]) #the IP adress after "nameserver"

        return servers

    