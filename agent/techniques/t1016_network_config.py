import os
import time
import subprocess
from shared.base import AttackTechnique
from shared.models import TechniqueResult
from shared.logging_config import get_logger

logger = get_logger("t1016")

class NetworkConfigDiscovery(AttackTechnique):
    """T1016 - Discovers network configuration on the target machine."""
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
            results["dns_servers"] = self._get_dns()
            results["routes"] = self._get_routes()
            results["interfaces"] = self._get_interfaces()
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

    def _get_routes(self) -> list:
        """Read routing table from /proc/net/route."""
        routes = []

        with open("/proc/net/route", "r") as f:
            next(f) #skip the header line
            for line in f:
                fields = line.strip().split()
                if len(fields) < 8:
                    continue

                iface = fields[0]
                destination = self._hex_to_ip(fields[1])
                gateway = self._hex_to_ip(fields[2])

                routes.append({
                    "interface": iface,
                    "destination": destination,
                    "gateway": gateway,
                    "is_default": fields[1] == "00000000"
                })

        return routes

    def _hex_to_ip(self, hex_str: str) -> str:
        """Convert a hex string to a dotted IP address."""
        raw = bytes.fromhex(hex_str) #Converts hex string to bytes
        return ".".join(str(b) for b in reversed(raw)) # reverse (little-endian) and format

    def _get_interfaces(self) -> list:
        """Get network interfaces and IP addresses using ip addr."""
        interfaces = []
        current = None
        output = subprocess.check_output(["ip", "addr"], text=True)

        for line in output.splitlines():
            if line and not line.startswith(" "): # interface header line
                parts = line.split(":")
                if len(parts) >= 2:
                    current = {"name": parts[1].strip(), "addresses": []}
                    interfaces.append(current)
            elif current and "inet " in line:       # IPv4 adress line
                parts = line.strip().split()
                current["addresses"].append(parts[1])

        return interfaces