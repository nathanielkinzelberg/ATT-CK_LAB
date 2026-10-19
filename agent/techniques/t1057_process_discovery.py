import os    # built-in Python library — used to list /proc and get system info
import time  # built-in Python library — used to measure how long the technique takes
from shared.base import AttackTechnique    # the base class template from Phase 1
from shared.models import TechniqueResult  # the standard result shape from Phase 1
from shared.logging_config import get_logger  # shared logging setup from Phase 1

logger = get_logger("t1057")  # creates a logger named "t1057"


class ProcessDiscovery(AttackTechnique):
    """T1057 - Discovers running processes on the target machine."""
    technique_id = "T1057"
    technique_name = "Process Discovery"
    tactic = "Discovery"
    description = "Lists running processes including PID, name, and owner."
    supported_platforms = ["linux"]
    risk_level = "low"

    def run(self) -> TechniqueResult:
        """Execute T1057 and return a list of running processes."""
        logger.info("Starting T1057 - Process Discovery")
        start_time = time.time()  # record start time to calculate duration later
        errors = []   # collect any errors — technique continues even if one part fails
        results = {}  # empty dict that gets filled with collected data

        try:
            results["processes"] = self._get_processes()          # list of all processes
            results["process_count"] = len(results["processes"])  # total number of processes found
        except Exception as e:
            errors.append(f"process discovery failed: {str(e)}")

        duration_ms = int((time.time() - start_time) * 1000)  # total time in milliseconds
        success = len(errors) == 0  # success only if zero errors occurred

        logger.info(f"T1057 completed - success={success}, duration={duration_ms}ms")

        return TechniqueResult(  # package everything into the standard result shape
            technique_id=self.technique_id,
            technique_name=self.technique_name,
            tactic=self.tactic,
            host=os.uname().nodename,  # os.uname().nodename is the machine's hostname
            success=success,
            results=results,
            errors=errors,
            duration_ms=duration_ms,
        )

    def _get_processes(self) -> list:
        """Read running processes from /proc."""
        processes = []

        for entry in os.listdir("/proc"):   # list everything inside /proc
            if not entry.isdigit():         # skip non-numeric entries — only numbered folders are processes
                continue

            pid = int(entry)       # the folder name is the PID
            process = {"pid": pid} # start building this process's data

            try:
                # /proc/{pid}/comm contains just the process name as a single line
                with open(f"/proc/{pid}/comm", "r") as f:
                    process["name"] = f.read().strip()
            except Exception:
                process["name"] = "unknown"  # process may have ended between listing and reading

            try:
                # /proc/{pid}/status contains detailed info — we only want the UID
                with open(f"/proc/{pid}/status", "r") as f:
                    for line in f:
                        if line.startswith("Uid:"):
                            uid = int(line.split()[1])  # first number is the real UID
                            process["uid"] = uid
                            break  # found what we need, stop reading
            except Exception:
                process["uid"] = -1  # -1 means UID could not be determined

            processes.append(process)

        return sorted(processes, key=lambda p: p["pid"])  # sort by PID so output is consistent
