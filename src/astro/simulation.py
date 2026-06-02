from .intent import IntentEstimate
from .safety_supervisor import SafetyDecision, SafetySupervisor


def simulate_step(intent: IntentEstimate, supervisor: SafetySupervisor | None = None) -> SafetyDecision:
    """Evaluate one simulated control step without touching hardware."""

    gate = supervisor or SafetySupervisor()
    return gate.evaluate(intent)
