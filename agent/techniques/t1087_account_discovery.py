import os    # built-in Python library — used to get the hostname
import time  # built-in Python library — used to measure how long the technique takes
from shared.base import AttackTechnique    # the base class template from Phase 1
from shared.models import TechniqueResult  # the standard result shape from Phase 1
from shared.logging_config import get_logger  # shared logging setup from Phase 1

logger = get_logger("t1087")  # creates a logger named "t1087"


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
        start_time = time.time()  # record start time to calculate duration later
        errors = []   # collect any errors — technique continues even if one part fails
        results = {}  # empty dict that gets filled with collected data

        try:
            results["accounts"] = self._parse_passwd()           # list of all user accounts
            results["account_count"] = len(results["accounts"])  # total number of accounts found
        except Exception as e:
            errors.append(f"account discovery failed: {str(e)}")

        duration_ms = int((time.time() - start_time) * 1000)  # total time in milliseconds
        success = len(errors) == 0  # success only if zero errors occurred

        logger.info(f"T1087 completed - success={success}, duration={duration_ms}ms")

        return TechniqueResult(  # package everything into the standard result shape
            technique_id=self.technique_id,
            technique_name=self.technique_name,
            tactic=self.tactic,
            host=os.uname().nodename,  # the machine's hostname
            success=success,
            results=results,
            errors=errors,
            duration_ms=duration_ms,
        )

    def _parse_passwd(self) -> list:
        """Read and parse user accounts from /etc/passwd."""
        accounts = []

        with open("/etc/passwd", "r") as f:  # /etc/passwd is readable by all users on Linux
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):  # skip empty lines and comments
                    continue

                fields = line.split(":")  # each field is separated by a colon
                if len(fields) != 7:      # a valid passwd line always has exactly 7 fields
                    continue

                accounts.append({
                    "username": fields[0],  # the account name
                    "uid": int(fields[2]),  # user ID — root is always 0, regular users start at 1000
                    "gid": int(fields[3]),  # group ID
                    "home": fields[5],      # home directory path e.g. /home/nathanielkinzelberg
                    "shell": fields[6],     # login shell e.g. /bin/bash — tells us if account is interactive
                })

        return sorted(accounts, key=lambda a: a["uid"])  # sort by UID so output is consistent
