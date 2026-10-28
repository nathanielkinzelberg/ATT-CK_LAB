import os
import time
import socket
from concurrent.futures import ThreadPoolExecutor
from shared.base import AttackTechnique
from shared.models import TechniqueResult
from shared.logging_config import get_logger

logger = get_logger("t1046")

TOP_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139,
    143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, 
    8443, 8888, 27017, 5432, 6379, 11211, 2181, 9200, 5601, 4444
]

PORT_NAMES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 111: "RPC", 135: "MSRPC", 139: "NetBIOS",
    143: "IMAP", 443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
    1723: "PPTP", 3306: "MySQL", 3389: "RDP", 5900: "VNC", 8080: "HTTP-Alt",
    8443: "HTTPS-Alt", 8888: "HTTP-Alt", 27017: "MongoDB", 5432: "PostgreSQL",
    6379: "Redis", 11211: "Memcached", 2181: "Zookeeper", 9200: "Elasticsearch",
    5601: "Kibana", 4444: "Metasploit"
}

class NetworkServiceScan(AttackTechnique):
    """T1046 - Scans for open network services on the target machine."""
    technique_id = "T1046"
    technique_name = "Network Service Scanning"
    tactic = "Discovery"
    description = "Scans common ports on the target host to find open services"
    supported_platforms = ["linux"]
    risk_level = "low"

    def run(self) -> TechniqueResult:
        logger.info("Starting T1046 - Network Service Scanning")
        start_time = time.time()
        errors = []
        results = {}

        duration_ms = int((time.time() - start_time) * 1000)
        success = len(errors) == 0

        logger.info(f"T1046 completed - success={success}, duration={duration_ms}ms")

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

    def _scan_port(self, host: str, port: int) -> dict | None:
        """Try to connect to a single port. Returns result dict if open, None if closed."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((host,port))
            s.close()
            if result == 0:
                return {
                    "port": port,
                    "service": PORT_NAMES.get(port, "unknown"),
                    "state": "open"
                }
        except Exception:
            pass
        return None