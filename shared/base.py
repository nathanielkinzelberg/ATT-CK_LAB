from abc import ABC, ABD, abstractmethod         # brings in the abstract base class functionality
from shared.models import TechniqueResult   # import the TechniqueResult dataclass from the shared.models module

class AttackTechnique(ABC):
    """Abstract base class that every ATT&CK technique must inherit from."""
    technique_id: str = ""               # the MITRE ATT&CK technique ID
    technique_name: str = ""             # human readable name of the technique
    tactic: str = ""                     # the MITRE ATT&CK tactic that the technique belongs to
    description: str = ""                # plain English description of the technique
    supported_platforms: list[str] = []  # the platforms that the technique supports
    risk_level: str = "low"              # saftey level of the technique
    