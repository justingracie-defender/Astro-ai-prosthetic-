from dataclasses import dataclass
from math import isfinite

from .intent import IntentEstimate


@dataclass(frozen=True)
class SafetyLimits:
    min_position_deg: float = -30.0
    max_position_deg: float = 90.0
    max_velocity_deg_s: float = 45.0
    max_torque_nm: float = 5.0
    min_confidence: float = 0.85


@dataclass(frozen=True)
class SafetyDecision:
    allowed: bool
    reason: str


class SafetySupervisor:
    """Deterministic safety gate for proposed prosthetic-limb motion."""

    def __init__(self, limits: SafetyLimits | None = None) -> None:
        self.limits = limits or SafetyLimits()

    def evaluate(self, intent: IntentEstimate) -> SafetyDecision:
        values = [
            intent.target_position_deg,
            intent.target_velocity_deg_s,
            intent.estimated_torque_nm,
            intent.confidence,
        ]
        if not all(isfinite(value) for value in values):
            return SafetyDecision(False, "rejected_non_finite_value")
        if intent.confidence < self.limits.min_confidence:
            return SafetyDecision(False, "rejected_low_confidence")
        if not (self.limits.min_position_deg <= intent.target_position_deg <= self.limits.max_position_deg):
            return SafetyDecision(False, "rejected_position_out_of_range")
        if abs(intent.target_velocity_deg_s) > self.limits.max_velocity_deg_s:
            return SafetyDecision(False, "rejected_velocity_limit")
        if abs(intent.estimated_torque_nm) > self.limits.max_torque_nm:
            return SafetyDecision(False, "rejected_torque_limit")
        return SafetyDecision(True, "allowed_within_configured_limits")
