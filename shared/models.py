from dataclasses import dataclass, field    # Bring in the dataclass decorator and field function
from datetime import datetime, timezone     # Generate timestamps for the data
import json                                 # Convert data to and from JSON format

@dataclass
class TechniqueResult:
    technique_id: str       # the MITRE ATT&CK technique ID
    technique_name: str     # human readable name of the technique
    tactic: str             # the MITRE ATT&CK tactic that the technique belongs to
    host: str               # the machine that ran the simulation
    success: bool           # whether the technique was successful or not
    results: dict = field(default_factory=dict)         # the actual results of the technique simulation
    errors: list[str] = field(default_factory=list)     # any errors that occurred during the simulation
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())  # the timestamp of when the simulation was run
    duration_ms: int = 0    # the duration of the simulation in milliseconds
