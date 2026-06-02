# Risk Register

This document tracks foreseeable hazards and mitigations for AI-assisted prosthetic-limb research.

| Risk | Example Hazard | Initial Mitigation |
|---|---|---|
| Unintended motion | Limb moves without wearer intent | Confidence thresholds, human veto, and fail-closed validation. |
| Excessive force or torque | Pain, injury, or device damage | Conservative configured limits and deterministic supervisor checks. |
| Sensor failure | Incorrect intent interpretation | Fault detection, redundancy planning, and no-motion defaults. |
| Model drift | Behavior changes after updates | Versioned models, audit logs, and locked safety envelopes. |
| Locked failure | Rigid arm creates secondary hazard | Limp-over-lock principle and mechanical release planning. |
| Overtrust | User assumes system is clinically ready | Clear documentation, warnings, and review gates. |

The risk register should be updated whenever new hardware, sensors, datasets, or control policies are introduced.
