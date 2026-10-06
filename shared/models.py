from dataclasses import dataclass, field    # Bring in the dataclass decorator and field function
from datetime import datetime, timezone     # Generate timestamps for the data
import json                                 # Convert data to and from JSON format

@dataclass
class TechniqueResult: 
    """A dataclass that represents the result of a simulated MITRE ATT&CK technique."""
    technique_id: str       # the MITRE ATT&CK technique ID
    technique_name: str     # human readable name of the technique
    tactic: str             # the MITRE ATT&CK tactic that the technique belongs to
    host: str               # the machine that ran the simulation
    success: bool           # whether the technique was successful or not
    results: dict = field(default_factory=dict)         # the actual results of the technique simulation
    errors: list[str] = field(default_factory=list)     # any errors that occurred during the simulation
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())  # the timestamp of when the simulation was run
    duration_ms: int = 0    # the duration of the simulation in milliseconds

    def to_dict(self) -> dict:
        """Convert the TechniqueResult dataclass to a dictionary."""
        return {
            "technique_id": self.technique_id,
            "technique_name": self.technique_name,
            "tactic": self.tactic,
            "host": self.host,
            "success": self.success,
            "results": self.results,
            "errors": self.errors,
            "timestamp": self.timestamp,
            "duration_ms": self.duration_ms
        }
    
    def to_json(self) -> str:
        """Convert the TechniqueResult dataclass to a JSON string."""
        return json.dumps(self.to_dict(), indent=2)