import pytest
from shared.base import AttackTechnique
from shared.models import TechniqueResult


class FakeTechnique(AttackTechnique):
    """A minimal concrete technique used only for testing the base class."""
    technique_id = "T9999"
    technique_name = "Fake Technique"
    tactic = "Discovery"
    description = "A fake technique for testing."
    supported_platforms = ["linux"]
    risk_level = "low"

    def run(self) -> TechniqueResult:
        return TechniqueResult(
            technique_id=self.technique_id,
            technique_name=self.technique_name,
            tactic=self.tactic,
            host="testhost",
            success=True,
        )


def test_cannot_instantiate_abstract_class():
    """AttackTechnique cannot be used directly — it must be subclassed."""
    with pytest.raises(TypeError):
        AttackTechnique()


def test_concrete_technique_runs():
    """A technique that implements run() should return a valid result."""
    t = FakeTechnique()
    result = t.run()
    assert result.success is True
    assert result.technique_id == "T9999"


def test_metadata_returns_expected_fields():
    """metadata() should return all required fields."""
    t = FakeTechnique()
    m = t.metadata()
    assert m["technique_id"] == "T9999"
    assert m["tactic"] == "Discovery"
    assert m["risk_level"] == "low"
    assert "linux" in m["supported_platforms"]
