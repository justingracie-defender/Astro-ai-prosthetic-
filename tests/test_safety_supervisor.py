from math import inf

from astro.intent import IntentEstimate
from astro.safety_supervisor import SafetySupervisor


def test_allows_command_inside_limits():
    supervisor = SafetySupervisor()
    intent = IntentEstimate(10.0, 5.0, 1.0, 0.95)
    decision = supervisor.evaluate(intent)
    assert decision.allowed is True


def test_rejects_low_confidence():
    supervisor = SafetySupervisor()
    intent = IntentEstimate(10.0, 5.0, 1.0, 0.20)
    decision = supervisor.evaluate(intent)
    assert decision.allowed is False
    assert decision.reason == "rejected_low_confidence"


def test_rejects_position_out_of_range():
    supervisor = SafetySupervisor()
    intent = IntentEstimate(120.0, 5.0, 1.0, 0.95)
    decision = supervisor.evaluate(intent)
    assert decision.allowed is False
    assert decision.reason == "rejected_position_out_of_range"


def test_rejects_non_finite_values():
    supervisor = SafetySupervisor()
    intent = IntentEstimate(inf, 5.0, 1.0, 0.95)
    decision = supervisor.evaluate(intent)
    assert decision.allowed is False
    assert decision.reason == "rejected_non_finite_value"
