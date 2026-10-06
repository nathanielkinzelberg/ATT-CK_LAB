from abc import ABC, abstractmethod         # brings in the abstract base class functionality
from shared.models import TechniqueResult   # import the TechniqueResult dataclass from the shared.models module

class AttackTechnique(ABC):
    """Abstract base class that every ATT&CK technique must inherit from."""
    technique_id: str = ""               # the MITRE ATT&CK technique ID
    technique_name: str = ""             # human readable name of the technique
    tactic: str = ""                     # the MITRE ATT&CK tactic that the technique belongs to
    description: str = ""                # plain English description of the technique
    supported_platforms: list[str] = []  # the platforms that the technique supports
    risk_level: str = "low"              # safety level of the technique

    @abstractmethod
    def run(self) -> TechniqueResult:
        """Run the technique and return a TechniqueResult dataclass."""

    def metadata(self) -> dict:
        """Return the technique as a dictionary."""
        return {
            "technique_id": self.technique_id,
            "technique_name": self.technique_name,
            "tactic": self.tactic,
            "description": self.description,
            "supported_platforms": self.supported_platforms,
            "risk_level": self.risk_level
        }