# Safety Model

Astro treats AI-assisted prosthetic control as a **safety-critical human-worn robotics problem**. AI may support inference and adaptation, but it must not bypass deterministic safety checks.

> The core design rule is: **the AI proposes or assists; the safety supervisor constrains, verifies, and can deny execution.**

| Boundary | Required Behavior |
|---|---|
| **Human Override** | The wearer or authorized operator must be able to stop or disable motion. |
| **Fail-Closed Defaults** | Unknown, malformed, conflicting, or low-confidence commands must resolve to safe no-motion or reduced-motion states. |
| **Actuator Limits** | Joint range, velocity, acceleration, force, and torque must remain bounded by conservative configuration. |
| **No Direct AI Actuation** | AI output should never directly command hardware without passing deterministic validation. |
| **Audit Logging** | Safety-relevant decisions should be logged for review. |
| **Limp Over Lock** | Faults should bias toward compliant safe failure rather than rigid lock-up. |

## Non-Goals

This repository does not claim clinical readiness, does not provide medical advice, and does not include production actuator-control code. Any human testing would require independent review, informed consent processes, professional supervision, and compliance with applicable laws and standards.
