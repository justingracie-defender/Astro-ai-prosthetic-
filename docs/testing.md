# Testing Strategy

Testing begins with deterministic unit tests for safety invariants and simulation behavior. The repository should treat test coverage as part of the safety case, not merely a software-quality exercise.

| Test Type | Purpose |
|---|---|
| **Unit Tests** | Verify intent parsing, confidence handling, and limit enforcement. |
| **Boundary Tests** | Confirm that extreme values are clamped or rejected. |
| **Fault-Injection Tests** | Simulate missing sensors, malformed inputs, and conflicting commands. |
| **Simulation Tests** | Evaluate behavior without physical hardware. |
| **Mannequin Tests** | Measure forces against instrumented non-human fixtures before any human contact. |
| **Environmental Tests** | Validate cold, heat, humidity, vibration, battery, and interference behavior. |

## Minimum Initial Invariants

The safety supervisor should reject commands with missing values, non-finite values, excessive velocity, excessive torque, out-of-range position, or confidence below the configured threshold.
