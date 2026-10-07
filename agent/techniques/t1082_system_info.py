import platform  # built-in Python library — reads OS, kernel, architecture, Python version
import socket    # built-in Python library — used to get the hostname
import time      # built-in Python library — used to measure how long the technique takes
from shared.base import AttackTechnique    # the base class template from Phase 1
from shared.models import TechniqueResult  # the standard result shape from Phase 1
from shared.logging_config import get_logger  # shared logging setup from Phase 1

logger = get_logger("t1082")  # creates a logger named "t1082" — shows up in every log line


class SystemInfoDiscovery(AttackTechnique):
    """T1082 - Collects system information from the target machine."""
    technique_id = "T1082"
    technique_name = "System Information Discovery"
    tactic = "Discovery"
    description = "Collects host, OS, kernel, architecture, and hardware information."
    supported_platforms = ["linux"]
    risk_level = "low"

    def run(self) -> TechniqueResult:
        """Execute T1082 and return collected system information."""
        logger.info("Starting T1082 - System Information Discovery")
        start_time = time.time()  # record start time so we can calculate duration later
        errors = []   # collect any errors — technique continues even if one part fails
        results = {}  # empty dict that gets filled with collected data

        try:
            # platform and socket are safe built-in libraries — no shell commands needed
            results["hostname"] = socket.gethostname()        # machine name e.g. "raspberrypi"
            results["os"] = platform.system()                 # e.g. "Linux"
            results["os_version"] = platform.version()        # full OS version string
            results["kernel"] = platform.release()            # kernel version e.g. "6.1.0"
            results["architecture"] = platform.machine()      # e.g. "aarch64" on Raspberry Pi
            results["python_version"] = platform.python_version()  # e.g. "3.11.2"
            results["processor"] = platform.processor()       # processor name
        except Exception as e:
            errors.append(f"platform collection failed: {str(e)}")
            # if this block fails we still continue to the /proc reads below

        try:
            results["cpu_info"] = self._read_proc_cpuinfo()   # reads /proc/cpuinfo
        except Exception as e:
            errors.append(f"cpu_info failed: {str(e)}")

        try:
            results["memory_info"] = self._read_proc_meminfo()  # reads /proc/meminfo
        except Exception as e:
            errors.append(f"memory_info failed: {str(e)}")

        try:
            results["uptime_seconds"] = self._read_proc_uptime()  # reads /proc/uptime
        except Exception as e:
            errors.append(f"uptime_seconds failed: {str(e)}")

        duration_ms = int((time.time() - start_time) * 1000)  # total time in milliseconds
        success = len(errors) == 0  # success only if zero errors occurred

        logger.info(f"T1082 completed - success={success}, duration={duration_ms}ms")

        return TechniqueResult(  # package everything into the standard result shape
            technique_id=self.technique_id,
            technique_name=self.technique_name,
            tactic=self.tactic,
            host=socket.gethostname(),
            success=success,
            results=results,
            errors=errors,
            duration_ms=duration_ms
        )

    def _read_proc_cpuinfo(self) -> dict:
        """Read CPU information from /proc/cpuinfo."""
        cpu = {}
        with open("/proc/cpuinfo", "r") as f:  # open the /proc/cpuinfo virtual file
            for line in f:                      # read it line by line
                if "Model name" in line or "model name" in line:
                    cpu["model"] = line.split(":")[1].strip()    # CPU model name
                if "Hardware" in line:
                    cpu["hardware"] = line.split(":")[1].strip() # hardware platform name
                if "Model" in line and "model" not in line.lower():
                    cpu["pi_model"] = line.split(":")[1].strip() # Raspberry Pi model string
        return cpu


    def _read_proc_meminfo(self) -> dict:
        """Read memory information from /proc/meminfo."""
        mem = {}
        with open("/proc/meminfo", "r") as f:  # open the /proc/meminfo virtual file
            for line in f:                      # read it line by line
                if "MemTotal" in line:
                    mem["total_kb"] = int(line.split()[1])      # total RAM in kilobytes
                if "MemAvailable" in line:
                    mem["available_kb"] = int(line.split()[1])  # available RAM in kilobytes
        return mem