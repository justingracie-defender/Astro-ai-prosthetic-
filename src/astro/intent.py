from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class IntentEstimate:
    """Represents a proposed user intent before safety validation."""

    target_position_deg: float
    target_velocity_deg_s: float
    estimated_torque_nm: float
    confidence: float


def estimate_intent(sensor_frame: Mapping[str, Any]) -> IntentEstimate:
    """Return a conservative placeholder intent estimate from a sensor frame.

    This function is intentionally simple and simulation-oriented. It should not
    be connected directly to prosthetic hardware.
    """

    return IntentEstimate(
        target_position_deg=float(sensor_frame.get("target_position_deg", 0.0)),
        target_velocity_deg_s=float(sensor_frame.get("target_velocity_deg_s", 0.0)),
        estimated_torque_nm=float(sensor_frame.get("estimated_torque_nm", 0.0)),
        confidence=float(sensor_frame.get("confidence", 0.0)),
    )
