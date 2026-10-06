import json
from shared.models import TechniqueResult


def test_result_has_required_fields():
    """Check that a result contains all expected fields."""
    r = TechniqueResult(
        technique_id="T1082",
        technique_name="System Information Discovery",
        tactic="Discovery",
        host="raspberrypi",
        success=True,
    )
    assert r.technique_id == "T1082"
    assert r.technique_name == "System Information Discovery"
    assert r.tactic == "Discovery"
    assert r.host == "raspberrypi"
    assert r.success is True


def test_timestamp_is_set_automatically():
    """Check that a timestamp is generated without us providing one."""
    r = TechniqueResult(
        technique_id="T1082",
        technique_name="System Information Discovery",
        tactic="Discovery",
        host="raspberrypi",
        success=True,
    )
    assert r.timestamp != ""
    assert "T" in r.timestamp


def test_to_dict_contains_all_keys():
    """Check that to_dict() returns all expected keys."""
    r = TechniqueResult(
        technique_id="T1082",
        technique_name="System Information Discovery",
        tactic="Discovery",
        host="raspberrypi",
        success=True,
    )
    d = r.to_dict()
    for key in ("technique_id", "technique_name", "tactic", "host",
                "timestamp", "success", "duration_ms", "results", "errors"):
        assert key in d


def test_to_json_is_valid_json():
    """Check that to_json() returns a valid JSON string."""
    r = TechniqueResult(
        technique_id="T1082",
        technique_name="System Information Discovery",
        tactic="Discovery",
        host="raspberrypi",
        success=True,
    )
    parsed = json.loads(r.to_json())
    assert parsed["technique_id"] == "T1082"


def test_failed_result():
    """Check that a failed result stores errors correctly."""
    r = TechniqueResult(
        technique_id="T1082",
        technique_name="System Information Discovery",
        tactic="Discovery",
        host="raspberrypi",
        success=False,
        errors=["permission denied"],
    )
    assert r.success is False
    assert "permission denied" in r.errors
